import struct
import wave

from waves import *


# Heavily inspired by https://zach.se/generate-audio-with-python/


def create_samples(channels, nsamples=-1):
    """
    Creates samples out of multiple channels
    :param channels: a list of iterators containing a wave data
    :param nsamples: the width of each sample
    :return: an iterator of samples
    """
    return itertools.islice(zip(*channels), nsamples)


def expand_channels(channel, nchannels):
    """
    Expand one channel to multiple
    :param channel: the channel to expand
    :param nchannels: the amount of channels
    :return: the sample
    """
    return map(lambda x: (x for i in range(nchannels)), channel)


def add_delay(sample, nchannels=2, seconds=1, sample_rate=44100):
    """
    Adds delay to the sample.
    :param sample: the sample
    :param nchannels: channel count
    :param seconds: seconds of delay
    :param sample_rate: sample rate
    :return: a sample with delay
    """
    return chain_samples((itertools.islice(expand_channels(sine_wave(amplitude=0), nchannels), sample_rate * seconds),
                          sample))


def __weighted_avg(samples, weight_table, n):
    """
    Averages by weight
    :param samples: the samples to average
    :param weight_table: the weight table, if None it's a normal average
    :param n: the number of samples
    :return: the average
    """
    return sum(x * (weight_table[i] if weight_table is not None else 1 / n) for i, x in enumerate(samples))


def merge_samples(samples, nchannels, weight_table=None):
    """
    Merges two samples
    :param samples: the samples, must have the same sample rate and channel count
    :param nchannels: the number of channels
    :param weight_table: adds a specific weight to each sample when merging the sound
    :return: the merged sample
    """
    zipped = itertools.zip_longest(*samples, fillvalue=(0 for _ in range(nchannels)))
    mapped = map(lambda x:
                 (__weighted_avg(itertools.islice(itertools.chain(*x), c, len(samples), nchannels), weight_table,
                                 len(samples)) for c in range(nchannels)),
                 zipped)
    return mapped


def chain_samples(samples):
    """
    Chains two samples
    :param samples: the samples, must have the same sample rate and channel count
    :return: the merged sample
    """
    return itertools.chain(*samples)


def grouper(n, iterable, fillvalue=None):
    """grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n
    return itertools.zip_longest(fillvalue=fillvalue, *args)


def write_wav(file, samples, nframes=-1, nchannels=2, sampwidth=2, framerate=44100, bufsize=2048):
    """
    Writes the samples to a wav file.
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
