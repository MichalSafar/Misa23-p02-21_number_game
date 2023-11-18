import random

class TwentyOneGame():
  def __init__(self):
    self.game_list = []

  def add_numbers_up_to_four(self, number):
    if type(number) == int or type(number) == float:
      if int(number) > 4:
        internal_number = 4
      else:
        internal_number = number
    else:
      print("Game accepts only integers or floats!")
      return -1
    o = 1
    while o <= internal_number:
      try:
        self.game_list.append(self.game_list[-1] + 1)
      except:
        self.game_list.extend([1.2])
      o += 1
    return 1
    
  def consecutive_numbers(self, consec_num):
    i = 1
    if len(self.game_list) < 2:
      return "Not enough numbers."
    while i <= consec_num:
      if self.game_list[-1] - self.game_list[-2] != 1:
        return False
      else:
        i += 1
    return True
  
  def computers_game_pass(self):
    comp_number = random.randint(1, 4)
    self.add_numbers_up_to_four(comp_number)
    print(f"Computer wants to add {comp_number} numbers.")
    return comp_number
  
  def player_game_pass(self):
    player_numbers = input("How many numbers would you like to add (up to 4)?")
    self.add_numbers_up_to_four(player_numbers)
    print(f"You asked to add {player_numbers} numbers.")
    print(f"The numbers are: {self.game_list}")
    return player_numbers

  def game(self):
    player_first_or_second = input("Would you like to play first (F) or second (S)?")
    player_first_or_second.lower()
    if player_first_or_second == "f" or player_first_or_second == "first":
      player_would_like_to_be = "first"
    elif player_first_or_second == "s" or player_first_or_second == "second":
      player_would_like_to_be = "second"
    print(f"You entered the game as a {player_would_like_to_be} player.")
    my_game = self.game_list
    while my_game[-1] <= 21:
      if my_game[-1] == 21:
        print("We are sorry, you lost the game. We wish you good luck and strategy next time.")
        break
      elif my_game[-1] == 20:
        print("You won the game!")
        break
      if player_would_like_to_be == "first":
        player_numbers = self.player_game_pass()
        player_numbers
        if len(my_game) < 2 and player_numbers == 1:
          my_game.append(1)
        elif len(my_game) < 2 and player_numbers == 2:
          my_game.extend([1, 2])
        else:
          self.add_numbers_up_to_four(player_numbers)
        print(f"The numbers are: {my_game}")
      elif player_first_or_second == "second":
        computer_pass = self.computers_game_pass()
        print(f"The numbers are: {my_game}")
        self.player_game_pass()

    
  