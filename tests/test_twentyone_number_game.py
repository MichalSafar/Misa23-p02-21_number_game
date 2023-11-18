import unittest
from unittest.mock import patch
from twentyone_number_game import TwentyOneGame
class Tests21Game(unittest.TestCase):
    def test_add_numbers_to_4_will_return_number(self):
        three_numbers = TwentyOneGame()
        three_numbers.add_numbers_up_to_four(number = 3)
        self.assertEqual(three_numbers.game_list, [3])
    
    def test_add_numbers_up_to_4_will_return_whole_number_only(self):
        non_whole_number = TwentyOneGame()
        non_whole_number.add_numbers_up_to_four(number = 1.4)
        self.assertEqual(non_whole_number.game_list, [1])

    def test_add_numbers_up_to_4_will_max_number_is_4(self):
        max_is_four = TwentyOneGame()
        max_is_four.add_numbers_up_to_four(number = 11.4)
        self.assertEqual(max_is_four.game_list, [4])

    def test_add_numbers_extends_game_numbers(self):
        my_game = TwentyOneGame()
        my_game.add_numbers_up_to_four([1,2,3])
        self.assertEqual(my_game.game_list, [1,2,3])

    def test_not_enought_numbers(self):
        my_game = TwentyOneGame()
        self.assertEqual(my_game.consecutive_numbers(3), "Not enough numbers.")

    #@patch('twentyone_number_game.TwentyOneGame.game', return_value = 2)
    #def test_game_asks_for_number(self, input):
    #    my_game = TwentyOneGame()
    #    self.assertEqual(my_game.game(), "You asked to add 2 numbers.")