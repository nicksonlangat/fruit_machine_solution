import unittest
from app import check_adjacent_slots, check_colors

class TestRandomColors(unittest.TestCase):

    def test_has_won_jackpot(self):
        my_random_choices = ['yellow', 'yellow', 'yellow', 'yellow']
        result = check_colors(my_random_choices)
        self.assertEqual(result, True)

    def test_has_not_won_jackpot(self):
        my_random_choices = ['yellow', 'black', 'green', 'yellow']
        result = check_colors(my_random_choices)
        self.assertEqual(result, False)

    def test_has_adjacent_same_colors(self):
        my_random_choices = ['yellow', 'black', 'yellow', 'yellow']
        result = check_adjacent_slots(my_random_choices)
        self.assertEqual(result, True)

    def test_has_no_adjacent_same_colors(self):
        my_random_choices = ['yellow', 'black', 'green', 'yellow']
        result = check_adjacent_slots(my_random_choices)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
