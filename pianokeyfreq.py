def one_semitone_up(freq):
    """
    Returns the key, one semitone up
    :param freq: the frequency in hz
    :return: the frequency one semitone up in hz
    """
    return freq * 1.059463


def one_semitone_down(freq):
    """
    Returns the key, one semitone down
    :param freq: the frequency in hz
    :return: the frequency one semitone down in hz
    """
    return freq / 1.059463


def one_tone_up(freq):
    """
    Returns the key, one tone up
    :param freq: the frequency in hz
    :return: the frequency one tone up in hz
    """
    return freq * 1.122462


def one_tone_down(freq):
    """
    Returns the key, one tone down
    :param freq: the frequency in hz
    :return: the frequency one tone down in hz
    """
    return freq / 1.122462
