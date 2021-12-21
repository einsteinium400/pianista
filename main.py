import wave
import json
# for generate random note
import os
import random

# import required module
import simpleaudio as sa

# for note compare
import time
import math
import wave
import struct
import numpy as np

# for note record
import sounddevice as sd
import scipy.io.wavfile as wav
from scipy.io.wavfile import write
import kivy
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import *
from kivy.app import App
from kivy.lang import Builder
from time import sleep

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import mainthread

import threading
import time

from AbsoluteHearingMode import AbsoluteHearingMode
from NoteReadingPractice import NoteReadingPractice


class MainWindow(Screen, FloatLayout):
    def __init__(self, **kwargs):
        self.experty = 0
        super().__init__(**kwargs)


class BeginnerWindow(Screen):
    pass


class IntermediateWindow(Screen):
    pass


class ExpertWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class CountDown(ProgressBar):

    def count(self):
        self.ids.pb.value = 60
        seconds = 60

        def count_it(seconds):
            if seconds == 0:
                return
            seconds -= 1
            self.ids.pb.value = seconds
            Clock.schedule_once(lambda dt: count_it(seconds), 1)

        Clock.schedule_once(lambda dt: count_it(60), 1)


class AbsoluteHearing(Screen):

    def __init__(self, **kw):
        self.ah = AbsoluteHearingMode()
        super().__init__(**kw)
        self.ah.generate_random_note()
        # this item holds object of class notereadingpractice

    def note_clicked(self, instance):

        self.ah.detected_note = instance.text
        result = self.ah.note_compare()
        # if user is right
        if result:

            # audio of success sound
            self.ah.generate_random_note()


            # Resets the notes buttons
            for i in range(1, 8):
                self.ids[str(i)].disabled = False
            # define an object to play
            wave_object = sa.WaveObject.from_wave_file('mp3/correct.wav')
            # define an object to control the play
            play_object = wave_object.play()
            play_object.wait_done()
            self.ah.sound_note()


        else:
            instance.disabled = True
            # define an object to play
            wave_object = sa.WaveObject.from_wave_file('mp3/wrong.wav')

            # define an object to control the play
            play_object = wave_object.play()
            play_object.is_playing()

    def play_generate_note(self):
        # play the generate note on_press
        self.ah.sound_note()
        if 'start' in self.ids:
            self.ids['start'].disabled = True


class NoteReading(Screen):

    def __init__(self, **kwargs):
        self.barspace = 20  # Space between lines
        self.barheight = 1.5  # Height (size) of lines
        self.notewidth = 64  # Width of a note
        self.noteheight = self.barspace + self.barheight  # 39 - Height of a note
        self.barwidth = self.notewidth + 20  # Width of bar near note

        self.topline_treble = 244  # Distance from top of screen to first line of treble
        self.bottomline_treble = self.topline_treble + self.barspace * 4  # Distance from top to last line of treble

        self.topline_bass = self.bottomline_treble + self.barspace * 2
        self.bottomline_bass = self.topline_bass + self.barspace * 4

        self.notes = []

        # this item holds object of class notereadingpractice
        self.notespractice = NoteReadingPractice(0)
        super().__init__(**kwargs)

        threading.Thread(target=self.notedisplaylogic).start()

        # event to make sure thread waits for click of "record"

    #   self.event_obj = threading.Event()

    def notedisplaylogic(self):
        while (True):

            self.notespractice.generate_random_note()

            # display the note generates
            self.display_note(self.notespractice.current_note, "black")
            # time.sleep(5)

            # record user
            user_success = False
            while not user_success:
                self.notespractice.record_note()
                path = os.getcwd()
                file_name = path + "\\wav files\\current.wav"
                audio_file = wave.open(file_name)
                # detect the note the user pressed
                self.notespractice.detect_note(audio_file)
                user_success = self.notespractice.note_compare()
                if user_success:
                    self.display_note(self.notespractice.detected_note, "green")
                    sleep(4)
                    continue

                else:
                    self.display_note(self.notespractice.detected_note, "red")

            self.remove_notes()
            # sleep(3)
            print("new session begins in 6 seconds")
            # time.sleep(5)

    @mainthread
    def display_note(self, note, color):
        newNote = InstructionGroup()

        x_position = int(note["pos_x"])
        y_position = int(note["pos_y"])

        image_address = "images/" + color + ".png"
        newNote.add(
            Rectangle(
                color="black",
                source=image_address,
                pos=(x_position, y_position),
                size=(18, 18),
            )
        )

        # add hash if note is a black key
        if "#" in note["name"]:
            newNote.add(
                Rectangle(
                    color="black",
                    source="images/sharp_symbol.png",
                    pos=(x_position - 15, y_position),
                    size=(15, 15),
                )
            )

        self.notes.append(newNote)
        self.canvas.after.add(newNote)

    @mainthread
    def remove_notes(self):
        for i in self.notes:
            print("shit")
            self.canvas.after.remove(i)
        self.notes = []


# the Base Class of our Kivy App
class MyApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    MyApp().run()
