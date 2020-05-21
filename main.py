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


def main():
    # winsound.Beep(19950, 1000)
    # winsound.PlaySound(sine_wave(64, 1/440, 44100, 16), flags=winsound.SND_MEMORY)
    print('Main')
    sinewave = sine_wave()
    sinewave2 = sine_wave()
    print("Sine wave:", list(itertools.islice(sinewave, 44100//440)))
    print("Added waves:", list(itertools.islice(add_waves(sinewave, sinewave2), 44100//440)))
    print("Mono:", len([list(i) for i in create_samples((sinewave,), 44100)]))
    print("Stereo:", len([list(i) for i in create_samples((sinewave, sinewave), 44100)]))
    # wav = write_wave(tempfile.mktemp(), create_samples((sinewave,), 44100), 44100)
    # wav2 = write_wave(tempfile.mktemp(), create_samples((sine_wave(0.5, 130.8128),), 44100), 44100)
    # winsound.PlaySound(wav, flags=winsound.SND_FILENAME)
    # winsound.PlaySound(wav2, flags=winsound.SND_FILENAME)

    # Play the C scale, starting from C3
    base = 130.8128
    x = 'TTSTTTS'  # Major scale
    for i in range(8):
        wav = write_wave(tempfile.mktemp(), create_samples((sine_wave(0.25, base), sine_wave(0.25, base)), 44100), 44100)
        winsound.PlaySound(wav, flags=winsound.SND_FILENAME)
        if i == 7:
            continue
        if x[i] == 'T':
            base = one_tone_up(base)
        else:
            base = one_semitone_up(base)
    for i in range(6, -2, -1):
        wav = write_wave(tempfile.mktemp(), create_samples((sine_wave(0.25, base), sine_wave(0.25, base)), 44100),
                         44100)
        winsound.PlaySound(wav, flags=winsound.SND_FILENAME)
        if i == -1:
            continue
        if x[i] == 'T':
            base = one_tone_down(base)
        else:
            base = one_semitone_down(base)


if __name__ == '__main__':
    main()
