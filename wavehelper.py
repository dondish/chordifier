import math
import wave
import itertools
import struct

def add_waves(*waves):
    """
    Adds an indefinite amount of waves together.
    :param waves: an iterator of waves
    :return: a wave
    """
    return map(sum, zip(*waves))


def sine_wave(amplitude=0.5, frequency=440., sample_rate=44100.):
    """
    Calculates a sine-wave
    :param amplitude: the amplitude of the wave
    :param frequency: the frequency of the wave
    :param sample_rate: the sample rate of the wave
    :return: an infinite iterator of the sine wave
    """
    increment = (2 * math.pi) / (sample_rate / frequency)
    return itertools.cycle(amplitude*math.sin(x*increment) for x in range(int(sample_rate / frequency)))


def create_samples(channels, nsamples=-1):
    """
    Creates samples out of multiple channels
    :param channels: a list of iterators containing a wave data
    :param nsamples: the width of each sample
    :return: an iterator of samples
    """
    return itertools.islice(zip(*channels), nsamples)


def grouper(n, iterable, fillvalue=None):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


def write_wave(file, samples, nframes=-1, nchannels=2, sampwidth=2, framerate=44100, bufsize=2048):
    """
    Writes the samples to a wave file.
    :param file: can be a filename, or a file object.
    :param samples: the samples
    :param nframes: the number of frames
    :param nchannels: the number of channels
    :param sampwidth: the width of the sample in bytes
    :param framerate: the frame rate
    :param bufsize: the size of the buffer to write into the file
    :return: file
    """
    w = wave.open(file, 'wb')
    w.setparams((nchannels, sampwidth, framerate, nframes, 'NONE', 'not compressed'))

    max_amplitude = float(int((2 ** (sampwidth * 8)) / 2) - 1)

    # split the samples into chunks (to reduce memory consumption and improve performance)
    for chunk in grouper(bufsize, samples):
        frames = b''.join(
            b''.join(struct.pack('h', int(max_amplitude * sample)) for sample in channels) for channels in chunk if
            channels is not None)
        w.writeframesraw(frames)

    w.close()

    return file