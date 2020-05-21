import struct
import sys

if sys.platform != 'win32':
    print('Currently only Windows is supported.')
    exit()

import winsound
import itertools
from wavehelper import *
from pianokeyfreq import *

import tempfile


def play_freq(waves, secs, file=tempfile.mktemp()):
    wav = write_wave(file, create_samples(waves, 44100 * secs), 44100 * secs)
    winsound.PlaySound(wav, flags=winsound.SND_FILENAME)


def main():
    # winsound.Beep(19950, 1000)
    # winsound.PlaySound(sine_wave(64, 1/440, 44100, 16), flags=winsound.SND_MEMORY)
    print('Main')
    sinewave = sine_wave()
    sinewave2 = sine_wave()
    print("Sine wave:", list(itertools.islice(sinewave, 44100 // 440)))
    print("Added waves:", list(itertools.islice(add_waves(sinewave, sinewave2), 44100 // 440)))
    print("Mono:", len([list(i) for i in create_samples((sinewave,), 44100)]))
    print("Stereo:", len([list(i) for i in create_samples((sinewave, sinewave), 44100)]))
    # wav = write_wave(tempfile.mktemp(), create_samples((sinewave,), 44100), 44100)
    # wav2 = write_wave(tempfile.mktemp(), create_samples((sine_wave(0.5, 130.8128),), 44100), 44100)
    # winsound.PlaySound(wav, flags=winsound.SND_FILENAME)
    # winsound.PlaySound(wav2, flags=winsound.SND_FILENAME)

    # Play the C scale, starting from C3
    # base = 130.8128
    # x = 'TTSTTTS'  # Major scale
    # for i in range(8):
    #     wav = write_wave(tempfile.mktemp(), create_samples((sine_wave(0.25, base), sine_wave(0.25, base)), 44100), 44100)
    #     winsound.PlaySound(wav, flags=winsound.SND_FILENAME)
    #     if i == 7:
    #         continue
    #     if x[i] == 'T':
    #         base = one_tone_up(base)
    #     else:
    #         base = one_semitone_up(base)
    # for i in range(6, -2, -1):
    #     wav = write_wave(tempfile.mktemp(), create_samples((sine_wave(0.25, base), sine_wave(0.25, base)), 44100),
    #                      44100)
    #     winsound.PlaySound(wav, flags=winsound.SND_FILENAME)
    #     if i == -1:
    #         continue
    #     if x[i] == 'T':
    #         base = one_tone_down(base)
    #     else:
    #         base = one_semitone_down(base)

    print('Playing Cmaj 3 seconds, merged with E4 for the first second, merged with C4 in the third second.')
    # Create Cmaj
    cmaj = avg_waves(sine_wave(frequency=PianoNotes.C3.value), sine_wave(frequency=PianoNotes.E3.value),
                     sine_wave(frequency=PianoNotes.G2.value))
    cmaj_sample = create_samples((cmaj,), 44100 * 3)
    # Create E
    e = sine_wave(frequency=PianoNotes.E4.value)
    e_sample = create_samples((e,), 44100)
    # Create C sample
    c = sine_wave(frequency=PianoNotes.C4.value)
    c_sample = create_samples((c,), 44100)
    # Prepend 2 seconds of blank sound to the C sample
    chained = add_delay(c_sample, 1, 2)
    # Merge them all together
    merged = merge_samples((cmaj_sample, e_sample, chained), 1)
    # Create WAV file and play
    w = write_wave(tempfile.mktemp(), merged, 44100 * 2)
    winsound.PlaySound(w, flags=winsound.SND_FILENAME)


if __name__ == '__main__':
    main()
