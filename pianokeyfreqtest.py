from pianokeyfreq import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_notes(self):
        self.assertEqual(PianoNotes.A1.value, 55, 'A1 is 55Hz')
        self.assertEqual(PianoNotes.A0.value, 27.5, 'A0 is 27.5Hz')
        self.assertAlmostEqual(PianoNotes.C3.value, 130.8128, 4, 'C3 is roughly 130.8128Hz')  # Float equality
        self.assertAlmostEqual(PianoNotes.E3.value, 164.8138, 4, 'E3 is roughly 164.8138Hz')  # Float equality
        self.assertAlmostEqual(PianoNotes.B6.value, 1975.533, 3, 'E3 is roughly 1975.533Hz')  # Float equality

    def test_black_keys_equality(self):
        self.assertEqual(PianoNotes['A#0'], PianoNotes['Bb0'], 'A# is Bb')
        self.assertEqual(PianoNotes['C#1'], PianoNotes['Db1'], 'C# is Db')
        self.assertEqual(PianoNotes['D#1'], PianoNotes['Eb1'], 'D# is Eb')
        self.assertEqual(PianoNotes['F#1'], PianoNotes['Gb1'], 'F# is Gb')
        self.assertEqual(PianoNotes['G#1'], PianoNotes['Ab1'], 'G# is Ab')


if __name__ == '__main__':
    unittest.main()
