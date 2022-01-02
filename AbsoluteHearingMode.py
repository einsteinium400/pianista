from Game import Game
import simpleaudio as sa

import random


class AbsoluteHearingMode(Game):
    """
    A class used to create the logic of Absolute Game.

    Attributes:
        
    A child of Game class- means it has the attributes and methods of Game

    Methods:

    generate_random_note(self)
        Return generate random note from array of notes
    note_compare(self)
        Compare between the notes and return True or False.
    sound_note(self, sound='')
        Play sound of file wav.
    """
    def __init__(self):
        # initialize game's class
        # super(AbsoluteHearing, self).__init__(self)
        Game.__init__(self)
        """
        Parameters:
        arr (array): Array of only relevant note from json
        noteamount (int): The length of the notes array.
        data (array): Array of all the notes from json.
        """

        # Inserts into array only notes relevant.
        for i in self.data:
            if i["audio_file"] is not None:
                self.arr.append(i)

        self.noteamount = len(self.arr)

    def generate_random_note(self):
        """
        Generate number in range 0,noteamount-1 (length of arr).

        Parameters:
        current_note (array): The generate note.
        randnum (int): Random number in range 0,noteamount-1 (length of arr)
        Returns:
            array:Index of the arr in the generate number.
        """
        randnum = random.randint(0, self.noteamount - 1)
        self.current_note = self.arr[randnum]
        print(self.arr[randnum])
        return self.arr[randnum]

    def note_compare(self):
        """
        Check if the name of the note that selected by the user is the same name of the note that generated by the
        program.
        The comparison does not refer to numbers in the names of the generated notes.

        Parameters:
        detected_note (array): The note selected by the user.
        current_note (array): The note generated by the program.

        Returns:
            Return: Bool True or False.
        """
        if self.detected_note.upper() in self.current_note["name"]:
            return True
        return False

    def sound_note(self, sound=''):
        """
        If sound_note receive sound it play it.
        else it plat the current_note.

        Parameters:
        filename (str): Path of sound's file.
        sound (str): Path of sound's file.
        current_note (array): The note generated by the program.
        """
        if sound:
            filename = sound
        else:
            filename = self.current_note["audio_file"]
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        if filename == 'mp3/correct.wav':
            # Help to do little delay.
            play_obj.wait_done()  # Wait until sound has finished playing
        else:
            play_obj.is_playing()  # Not wait until sound has finished playing
