# for generate random note
import json
import os
import random

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
import Game


class Game:
    def __init__(self):
        f = open('myfile.json', "r")

        # this array contains all notes
        self.data = json.loads(f.read())

        # this array contains only the notes that are relevant for the experty level or the current mode
        self.arr = []

        # the current note the system generated
        self.current_note = 0
        # the current note the user chose
        self.detected_note = 0


    def generate_random_note(self):
        pass

    def note_compare(self):
        pass
