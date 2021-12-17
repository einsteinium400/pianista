import json

#for generate random note
import os
import random

#for note compare
import time
import math
import wave
import struct
import numpy as np

#for note record
import sounddevice as sd
import scipy.io.wavfile as wav
from scipy.io.wavfile import write

class NoteReadingPractice:

    def __init__(self, experty):
        self.experty = experty
        f = open('myfile.json',"r")

        # this array contains all notes
        self.data = json.loads(f.read())

        #this array contains only the notes that are relevant for the experty level
        self.arr=[]
        self.detected_note=0 #will hold the current note that has been generated

        #beginner mode
        if (experty==0):
            for i in self.data:
                if (i["octave"] == "one-line" or i["octave"] == "two-line"):
                    self.arr.append(i)

        #intermediate mode
        if (experty==1):
            for i in self.data:
                if (i["octave"] == "one-line" or i["octave"] == "two-line" or i["octave"] == "small" or i["octave"] == "great"):
                    self.arr.append(i)

        self.noteamount=len(self.arr)


    #this method generates a random note and places it in current_note
    def generate_random_note(self):
        randnum=random.randint(0, self.noteamount-1)
        self.current_note=self.arr[randnum]
        print (self.arr[randnum])
        return self.arr[randnum]

    def display_note(self):
        print (self.current_note)


    def record_note(self):
        fs = 44100
        duration = 5  # seconds
        myrecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='int16')
        print("Recording Audio")
        sd.wait()
        #print("Audio recording complete , Play Audio")
        #sd.play(myrecording, fs)
        #sd.wait()
        write("wav files/current.wav", fs, myrecording)
        #print("Play Audio Complete")


    def detect_note(self, audio_file):
        file_length = audio_file.getnframes()
        f_s = audio_file.getframerate()  # sampling frequency
        sound = np.zeros(file_length)  # blank array

        for i in range(file_length):
            wdata = audio_file.readframes(1)
            data = struct.unpack("<h", wdata)
            sound[i] = int(data[0])

        sound = np.divide(sound, float(2 ** 15))  # scaling it to 0 - 1
        counter = audio_file.getnchannels()  # number of channels mono/sterio
        # -------------------------------------------

        # fourier transformation from numpy module
        fourier = np.fft.fft(sound)
        fourier = np.absolute(fourier)
        imax = np.argmax(fourier[0:int(file_length / 2)])  # index of max element

        # peak detection
        i_begin = -1
        threshold = 0.3 * fourier[imax]
        for i in range(0, imax + 100):
            if fourier[i] >= threshold:
                if (i_begin == -1):
                    i_begin = i
            if (i_begin != -1 and fourier[i] < threshold):
                break
        i_end = i
        imax = np.argmax(fourier[0:i_end + 100])

        freq = (imax * f_s) / (file_length * counter)  # formula to convert index into sound frequency

        note = 0
        # searching for matched frequencies in data json array
        for i in range(len(self.data)-1):
            if (freq < self.data[i]["fq"]):
                note = self.data[i]
                break
            if (freq > self.data[-1]["fq"]):
                note = self.data[-1]
                break
            if freq >=self.data[i]["fq"] and self.data[i+1]["fq"] >= freq:
                if freq - self.data[i]["fq"] < (self.data[i+1]["fq"] - self.data[i]["fq"]) / 2:
                    note = self.data[i]
                else:
                    note =self.data[i+1]
                break

        self.detected_note=note #the note detected
        print("detected note is: ", end="")
        print (self.detected_note)

    def feedback(self):
        print(self.note_compare())

    def note_compare(self):


        if (self.detected_note==self.current_note):
            return True
        else:
            return False


# while (1):
#     p=NoteReadingPractice(1)
#     p.generate_random_note()
#     p.display_note()
#     time.sleep(10)
#     p.record_note()
#    # time.sleep(4)
#
#     path = os.getcwd()
#     file_name = path + "\\wav files\\current.wav"
#     audio_file = wave.open(file_name)
#
#     p.detect_note(audio_file)
#     p.feedback()
#     print("new session begins in 6 seconds")
#     time.sleep(5)