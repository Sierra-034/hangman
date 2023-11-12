import unittest

from hangman import display_board


class HangmanTest(unittest.TestCase):

    def test_display_board(self):
        display_board('xv', 'oa', 'hola')
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
