import itertools
import math
import random


def add_waves(*waves):
    """
    Adds waves together.
    :param waves: an iterator of waves
    :return: a wave
    """
    return map(sum, zip(*waves))


def avg_waves(*waves):
    """
    Create the average wave.
    :param waves: an iterator of waves
    :return: a wave
    """
    return map(lambda x: x / len(waves), add_waves(*waves))


def mul_wave(wave, scalar: float = 1.):
    """
    Multiply the wave by a scalar
    :param wave: the wave
    :param scalar: a scalar to multiply the wave with
    :return:the new wave
    """
    return map(lambda x: x * scalar, wave)


def sine_wave(amplitude=0.5, frequency=440., sample_rate=44100.):
    """
    Calculates a sine-wave
    :param amplitude: the amplitude of the wave
    :param frequency: the frequency of the wave
    :param sample_rate: the sample rate of the wave
    :return: an infinite iterator of the sine wave
    """
    increment = (2 * math.pi) / (sample_rate / frequency)
    return itertools.cycle(amplitude * math.sin(x * increment) for x in range(int(sample_rate / frequency)))


def square_wave(amplitude=0.5, frequency=440., sample_rate=44100.):
    """
    Calculates a square-wave
    :param amplitude: the amplitude of the wave
    :param frequency: the frequency of the wave
    :param sample_rate: the sample rate of the wave
    :return: an infinite iterator of the square wave
    """
    return map(lambda x: 0 if x == 0 else (amplitude if x > 0 else -amplitude),
               sine_wave(amplitude, frequency, sample_rate))


def sawtooth_wave(amplitude=0.0125, frequency=440., sample_rate=44100.):
    """
    Calculates a sawtooth-wave
    :param amplitude: the amplitude of the wave
    :param frequency: the frequency of the wave
    :param sample_rate: the sample rate of the wave
    :return: an infinite iterator of the square wave
    """
    return itertools.cycle(
        -amplitude + 2 * amplitude * x / (sample_rate / frequency) for x in range(int(sample_rate / frequency)))


def triangle_wave(amplitude=0.5, frequency=440., sample_rate=44100.):
    """
    Calculates a triangle-wave
    :param amplitude: the amplitude of the wave
    :param frequency: the frequency of the wave
    :param sample_rate: the sample rate of the wave
    :return: an infinite iterator of the triangle wave
    """
    return itertools.cycle(
        4 * amplitude * (x / (sample_rate / frequency) - 0.25 if x / (sample_rate / frequency) <= 1 / 2
                         else 0.75 - x / (sample_rate / frequency))
        for x in range(int(sample_rate / frequency)))


def white_noise(amplitude=0.0125):
    """
    Calculates a white-noise
    :param amplitude: the amplitude of the noise
    :return: an infinite iterator of the white-noise
    """

    def __white_noise():
        while True:
            yield random.uniform(-1, 1) * amplitude

    return __white_noise()
