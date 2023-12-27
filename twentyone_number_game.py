import random

class TwentyOneGame():
  def __init__(self, player, another_player):
    self.game_list = []
    self.player = player
    self.another_player = another_player

  def add_numbers_up_to_four(self, number):
    if type(number) == int or type(number) == float:
      if int(number) > 4:
        internal_number = 4
      else:
        internal_number = int(number)
    else:
      print("Game accepts only integers or floats!")
      return -1
    o = 1
    while o <= internal_number:
      try:
        self.game_list.append(self.game_list[-1] + 1)
      except:
        self.game_list.extend([1])
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
    print(f"The numbers are: {self.game_list}")
    return True
  
  def player_game_pass(self, computer_or_another_player, player):
    if computer_or_another_player == "computer":
      player_numbers_raw = input("How many numbers would you like to add (up to 4)?")
    else:
      player_numbers_raw = input(f"{player}. How many numbers would you like to add (up to 4)?")
    player_numbers = int(player_numbers_raw)
    print(f"{player} asked to add {player_numbers} numbers.")
    add_player_numbers = self.add_numbers_up_to_four(player_numbers)
    add_player_numbers
    if add_player_numbers == -1:
      exit()
    else:
      pass
    return player_numbers
  
  def winning_number(self, player):
    if self.game_list[-1] >= 21 and player == "player":
      print("You won the game!")
      exit()
    elif self.game_list[-1] >= 21:
      print(f"{player} won the game!")
      exit()
    
  def loosing_number(self):
    if self.game_list[-1] >= 21:
      print("We are sorry, you lost the game. We wish you good luck and strategy next time.")
      exit()

  def computer_player_game(self, player_would_like_to_be, computer_or_another_player, player):
    r = 1
    round = 1
    while r <= 21:
      print(f"Round {round}")
      if player_would_like_to_be == "first":
        self.player_game_pass(computer_or_another_player, player = self.player)
        print(f"The numbers are: {self.game_list}")
        self.winning_number(self.player)
        self.computers_game_pass()
        print(f"The numbers are: {self.game_list}")
        self.loosing_number()
        r = self.game_list[-1]
      elif player_would_like_to_be == "second":
        self.computers_game_pass()
        print(f"The numbers are: {self.game_list}")
        self.loosing_number()
        self.player_game_pass(computer_or_another_player, player = self.player)
        print(f"The numbers are: {self.game_list}")
        self.winning_number(self.player)
        r = self.game_list[-1]
      round += 1
    
  def two_players_game(self, player_would_like_to_be, computer_or_another_player, player1, player2):
    r = 1
    round = 1
    while r <= 21:
      print(f"Round {round}")
      if player_would_like_to_be == "first":
        self.player_game_pass(computer_or_another_player, self.player)
        print(f"The numbers are: {self.game_list}")
        self.winning_number(self.player)
        self.player_game_pass(computer_or_another_player, self.another_player)
        print(f"The numbers are: {self.game_list}")
        self.winning_number(self.another_player)
        r = self.game_list[-1]
      elif player_would_like_to_be == "second":
        self.player_game_pass(computer_or_another_player, self.player)
        print(f"The numbers are: {self.game_list}")
        self.winning_number(self.player)
        self.player_game_pass(computer_or_another_player, self.another_player)
        print(f"The numbers are: {self.game_list}")
        self.winning_number(self.another_player)
        r = self.game_list[-1]
      round += 1

  def game(self):
    print("Hello. You are welcomed in our game. At the beginning we will ask some absolutelly necessary questions.")
    print("It is enough to answer only in one small letter that is at the beginning of the word.")
    print("Wheater you are playing against computer or a player, the answers for a winning or a loosing will be to you and not to another player.")
    computer_or_another_player = input("Would you like to play against computer (c) or against a player (p)?")
    computer_or_another_player = computer_or_another_player.lower()
    if computer_or_another_player == "p" or computer_or_another_player == "player":
      computer_or_another_player = "player"
    elif computer_or_another_player == "c" or computer_or_another_player == "computer":
      computer_or_another_player = "computer"
    else:
      print("I did not understand your answer. So you will play against a computer.")
      computer_or_another_player = "computer"
    player_first_or_second = input("Would you like to play first (f) or second (s)?")
    player_first_or_second = player_first_or_second.lower()
    if player_first_or_second == "f" or player_first_or_second == "first":
      player_would_like_to_be = "first"
    elif player_first_or_second == "s" or player_first_or_second == "second":
      player_would_like_to_be = "second"
    else:
      guess_enter = random.randint(0,1)
      if guess_enter == 0:
        player_would_like_to_be = "first"
        print("I do not understand your answer, but I guess you want to enter the game as a first player.")
      else:
        player_would_like_to_be = "second"
        print("I do not understand your answer, but I guess you want to enter the game as a second player.")
    print(f"You entered the game as a {player_would_like_to_be} player.")
    if computer_or_another_player == "computer":
      self.computer_player_game(player_would_like_to_be, computer_or_another_player, self.player)
    else:
      self.player = input("What will be the name of player1?  ")
      self.another_player = input("what will be the name of player2?  ") 
      self.two_players_game(player_would_like_to_be, computer_or_another_player, self.player, self.another_player)
    
my_game = TwentyOneGame("player1", "player2")
my_game.game()  
