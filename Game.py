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
    """
   A class containing the common attributes and methods of the games for inheritance.

   Attributes:

   data (array): Contains all notes.
   arr (array): Contains only the notes that are relevant for the
   experty level or the current modety level or the current mode.
   current_note (array): The current note the system generated.
   detected_note (array): The current note the user chose.

   Methods:

   generate_random_note(self)
       Return generate random note from array of notes
   note_compare(self)
       Compare between the notes and return True or False.
    """

    def __init__(self):
        f = open('myfile.json', "r")
        self.data = json.loads(f.read())
        self.arr = []
        self.current_note = 0
        self.detected_note = 0

    def generate_random_note(self):
        """
        Returns:
            Return generate random note from array of notes.
        """
        pass

    def note_compare(self):
        """
              Compare between the notes.

              Returns:
                  Return: Bool True or False.
              """
        pass
