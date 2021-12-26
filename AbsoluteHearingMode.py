from Game import Game
import simpleaudio as sa

import random


class AbsoluteHearingMode(Game):
    def __init__(self):
        # initialize game's class
        # super(AbsoluteHearing, self).__init__(self)
        Game.__init__(self)

        # insert into array only notes that have an audio file
        # inserts all relevant files into array
        for i in self.data:
            if i["audio_file"] is not None:
                self.arr.append(i)

        self.noteamount = len(self.arr)

    def generate_random_note(self):
        randnum = random.randint(0, self.noteamount - 1)
        self.current_note = self.arr[randnum]
        print(self.arr[randnum])
        return self.arr[randnum]

    def note_compare(self):
        if self.detected_note.upper() in self.current_note["name"]:
            return True
        return False

    def sound_note(self, sound=''):
        if sound:
            filename = sound
        else:
            filename = self.current_note["audio_file"]
        wave_obj = sa.WaveObject.from_wave_file(filename)
        play_obj = wave_obj.play()
        if filename == 'mp3/correct.wav':
            play_obj.wait_done()  # Wait until sound has finished playing
        else:
            play_obj.is_playing()  # Not wait until sound has finished playing
