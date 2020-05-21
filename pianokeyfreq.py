from enum import Enum


def one_semitone_up(freq, amount=1):
    """
    Returns the key, one semitone up
    :param freq: the frequency in hz
    :param amount: the amount of semitones up
    :return: the frequency one tone up in hz
    """
    return freq * 2 ** (amount / 12)


def one_semitone_down(freq, amount=1):
    """
    Returns the key, one tone down
    :param freq: the frequency in hz
    :param amount: the amount of semitones down
    :return: the frequency one semitone up in hz
    """
    return freq / 2 ** (amount / 12)


def one_tone_up(freq, amount=1):
    """
    Returns the key, one tone up
    :param freq: the frequency in hz
    :param amount: the amount of tones up
    :return: the frequency one tone up in hz
    """
    return freq * 2 ** (2 * amount / 12)


def one_tone_down(freq, amount=1):
    """
    Returns the key, one tone down
    :param freq: the frequency in hz
    :param amount: the amount of tones down
    :return: the frequency one tone up in hz
    """
    return freq / 2 ** (2 * amount / 12)


def _create_notes():
    s = 'C C#D D#E F F#G G#A A#B'
    transl = {'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb'}
    l = [('A0', 27.5), ('A#0', one_semitone_up(27.5)), ('Bb0', one_semitone_up(27.5)), ('B0', one_tone_up(27.5))]
    a0 = 27.5
    for octave in range(1, 8):
        for note in range(0, 12):
            if octave < 8 or note == 0:
                l.append(
                    (s[2 * note:2 * note + 2].strip() + str(octave), one_semitone_up(a0, 3 + (octave - 1) * 12 + note)))
    for i in range(1,8):
        for a, b in transl.items():
            l.append((b+str(i), next((x for x in l if a+str(i) == x[0]))[1]))
    return Enum('Notes', l)


# PianoNotes is an enum that includes all of the notes available on a standard piano
PianoNotes = _create_notes()
