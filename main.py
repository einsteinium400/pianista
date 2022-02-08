import json
# for generate random note
import os
import random
from kivy.animation import Animation
# for note compare
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
import time
import wave
import simpleaudio as sa
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
<<<<<<< HEAD
=======
from kivy.uix.progressbar import ProgressBar
>>>>>>> 2a3242f946e2f87988ca780fb70658e2dd193e02
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import *
from kivy.app import App
from time import sleep
from kivy.clock import mainthread
from kivy.uix.image import Image, AsyncImage
import threading
from AbsoluteHearingMode import AbsoluteHearingMode
from NoteReadingPractice import NoteReadingPractice


class OpenWindow(Screen):

    def __init__(self, **kwargs):
        super(OpenWindow, self).__init__(**kwargs)
<<<<<<< HEAD

        # animation of logo
        self.logo = Image(source='images/pianista.png', opacity=0)
        animated_icon = Animation(opacity=0.25)+Animation(opacity=0.5) +Animation(opacity=0.75)+ Animation(opacity=1)
        self.add_widget(self.logo)
        animated_icon.start(self.logo)
        # go to next page after 10 seconds
        Clock.schedule_once(self.callNext,10)
=======
        # sound open song
        filename = 'wav_files/open_song.wav'
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        play_obj.is_playing()
        # animation of logo
        self.logo = Image(source='images/pianista.png', opacity=0)
        animated_icon = Animation(opacity=0.5) + Animation(opacity=1)
        self.add_widget(self.logo)
        animated_icon.start(self.logo)
        # go to next page after 4 seconds
        Clock.schedule_once(self.callNext, 4)
>>>>>>> 2a3242f946e2f87988ca780fb70658e2dd193e02

    def callNext(self, dt):
        self.manager.current = 'main'



class MainWindow(Screen, FloatLayout):
    experty = 0
    """
    A class used to link between the GUi and the games.
    Attributes:
    experty (int): The experty the user chose.
    """
    def __init__(self, **kwargs):
        MainWindow.experty = 0
        super().__init__(**kwargs)

    def change_experty(self, num):
        MainWindow.experty=num
        print(MainWindow.experty)


class BeginnerWindow(Screen):

    """
    A class used to create Beginner Window.
    """
    pass


class IntermediateWindow(Screen):
    """
    A class used to create Intermediate Window.
    """
    pass


class ExpertWindow(Screen):
    """
    A class used to create Expert Window.
    """
    pass


class WindowManager(ScreenManager):
    """
    A class used to create Window Manager.
    """
    pass


class AbsoluteHearing(Screen):
    """
    A class used to link between the GUi and the AbsoluteHearing game.
    Attributes:
    ah (AbsoluteHearing object): Instance's game.
   Methods:
   note_clicked(self, instance)
        Gets the note the user selected from the GUI, compare and return feedback.
   generate_random_note(self)
       On_click the 'Hear Again' button- the generate note will be play again.
   get_answer(self)
        On_click the 'Answer' button- the answer will be displayed by animation.
   start(self)
        On_click the 'Start' button- the game will start and all the buttons will become available.
   init_button(self, num1)
        Turning buttons unavailable to available and oppositely.
    """

    def __init__(self, **kw):
        self.ah = AbsoluteHearingMode()
        super().__init__(**kw)
        # this item holds object of class notereadingpractice

    def note_clicked(self, instance):
        """
        Gets the note the user selected from the GUI.
        compare between the notes and return feedback.
        If the user is right- Sound of success will be heard and the game will continue.
        Else- Sound will be played accordingly and the note button will turn off.

        Attributes:
        result (int): The result of note_compare().
        """

        self.ah.detected_note = instance.text
        # check the answer
        result = self.ah.note_compare()
        # if user is right
        if result:

            # reset the note bottoms's disables
            for i in range(1, 8):
                if self.ids[str(i)].disabled:
                    self.init_button(i)
            # play correct answer
<<<<<<< HEAD
            self.ah.sound_note('wav_files/correct.wav')
=======
            self.ah.sound_note('mp3/correct.wav')
>>>>>>> 2a3242f946e2f87988ca780fb70658e2dd193e02
            # time.sleep(1)
            self.ah.generate_random_note()
            self.ah.sound_note()
        else:
            instance.disabled = True
            self.ids[str(50)].text = "Attempts:" + str(self.ah.failure_count) + "/10"
            # play wrong answer
<<<<<<< HEAD
            self.ah.sound_note('wav_files/wrong.wav')
=======
            self.ah.sound_note('mp3/wrong.wav')
>>>>>>> 2a3242f946e2f87988ca780fb70658e2dd193e02
            if self.ah.failure_count == 0:
                self.manager.current = 'GameOver'
                self.end_game()

    def play_generate_note(self):
        """

        On_click the 'Hear Again' button- the generate note will be play again by AbsoluteHearingMode function.

        """
        # play the generate note on_press
        self.ah.sound_note()

    def get_answer(self):
        """

        First we find the button of the answer and then the animation will be done.

        Attributes:

        id_b (str): Answer button's id.

        anim (kivy.animation.Sequence): Animated action
        """
        # Find the button's answer id
        for i in range(1, 8):
            if self.ah.current_note['name'][0].lower() in self.ids[str(i)].text:
                id_b = str(i)
        # animation on the right answer that color the note
        anim = Animation(background_color=[0, 0, 0, 0]) + Animation(
            background_color=[212 / 255, 186 / 255, 154 / 255, 1])
        print(type(anim))
        anim.start(self.ids[id_b])

    def start(self):
        """
        On_click the 'Start' button- the game will start and all the buttons will become available.
        """
        self.ids[str(50)].text = "Attempts:" + str(self.ah.failure_count) + "/10"
        self.ah.generate_random_note()
        self.play_generate_note()
        # Make the buttons available
        for i in range(1, 11):
            self.init_button(i)

    # num1 and num2 is the range of id's bottoms we want to change their disabled
    def init_button(self, num1):
        """
        Turning buttons unavailable to available and oppositely.
        """

        if self.ids[str(num1)].disabled:
            self.ids[str(num1)].disabled = False
        else:
            self.ids[str(num1)].disabled = True
        return

    def end_game(self):
        """
        Init the game after exit from it.
        """
        for i in range(1, 10):
            self.ids[str(i)].disabled = True
        self.ids[str(10)].disabled = False
        self.ids[str(50)].text = "Attempts:" + str(self.ah.failure_count) + "/10"
        if self.ah.failure_count != 0:
            self.manager.current = 'main'
        self.ah.failure_count = 10


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
        self.thread_kill=1
        # this item holds object of class notereadingpractice
        super().__init__(**kwargs)
        self.t=threading.Thread(target=self.notedisplaylogic,daemon=True)
        self.t.start()

        # t.start() #############
    def start_game_thread(self):
        # self.notespractice = NoteReadingPractice(MainWindow.experty)
        print("start")
        self.thread_kill=0

    def join_game_thread(self):
        self.thread_kill=1
        self.remove_notes()
        del self.notespractice

    def notedisplaylogic(self):

        while True:
            if (self.thread_kill==1):
                #we dont want to kill the thread, just hold it
                while True:
                    #thread is sleeping
                    if (self.thread_kill == 0):
                        #revive thread with desired experty level
                        self.notespractice = NoteReadingPractice(MainWindow.experty)
                        break

            # print("fuck everything")
            self.notespractice.generate_random_note()

            # display the note generates
            self.display_note(self.notespractice.current_note, "black")

            # record user
            user_success = False
            while not user_success :
                if self.thread_kill==1:
                    break
                try:
                    self.notespractice.record_note()
                except:
                    pass

                try:
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
                        print(self.notespractice.detected_note)
                        print(self.notespractice.detected_note)
                        if self.notespractice.detected_note["pos_x"].isnumeric():
                            self.display_note(self.notespractice.detected_note, "red")

                except:
                    pass


            self.remove_notes()

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
            self.canvas.after.remove(i)
        self.notes = []


class GameOver(Screen):
    pass


# the Base Class of our Kivy App
class MyApp(App):
    icon = 'images/icon.png'
    title = 'Pianista'

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        screen=Screen(name='MainWindow')
        sm.switch_to(screen, direction='right')

if __name__ == '__main__':
    app = MyApp()
    app.run()
    app.root_window.close()
