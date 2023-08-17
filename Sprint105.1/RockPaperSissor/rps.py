import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player():
    """
    Base class for all the players in the game.
    """

    def __init__(self):
        self.opponent_last_move = None
    def move(self):
        """
        This players  should be implemented by subclasses to define the player's move.
        """
        return [moves]

    def learn(self, my_move, their_move):
        """
        Learn and process the moves of the players after each round.
        """
        self.opponent_last_move = their_move
class RockPlayer(Player):
    def move(self):
        return 'rock'

class RandomPlayer(Player):
    """
        Represents a player who makes random moves.
        """
    def move(self):
        """
        choose a random moves from the list of the available moves.
        """
        return random.choice(moves)

class HumanPlayer(Player):
    """
    It represents a human player who enter the moves from user input.
    """

    def move(self):

        """
        get the moves from the user input.
        """
        while True:
            user_choice = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
            if user_choice == "q":
                break
            if user_choice not in moves:
                print("Invalid input. Please choose Rock, Paper, or Scissors.")
                continue
            return user_choice

class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.opponent_last_move = None

    def move(self):
       if self.opponent_last_move is None:
           return random.choice(moves)
       return self.opponent_last_move

    def learn(self, my_move, their_move):
        self.opponent_last_move = their_move

class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move_index = -1

    def move(self):
        self.last_move_index = (self.last_move_index + 1) % len(moves)
        return moves[self.last_move_index]


class Game():
    # noinspection GrazieInspection
    """
        It describes the rock, paper, scissors game.
        """
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_player1 = 0
        self.score_player2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if self.beats(move1, move2):
            self.score_player1 += 1
            print("\033[91mPlayer 1 wins the round\033[0m")  # Red color for winner
        elif self.beats(move2, move1):
            self.score_player2 += 1
            print("\033[91mPlayer 2 wins the round\033[0m")  # Red color for winner
        else:
            print("It's a tie")
        # Call  the learn method on each player to inform them about the opponent's move
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)


    def beats(self, one, two):
        """
        Determine if the second moves beat the first move.
        """
        winning_combination = {
            'paper': 'rock',
            'rock': 'scissors',
            'scissors': 'paper'
        }
        return two == winning_combination[one]


    def play_game(self):
        """
        Play the full game.
        """


        self.rounds = 3

        print("Game Start")
        for round in range(self.rounds):
            print(f"Round {round +1}")
            self.play_round()
        print("\033[91m______________*****************______________\033[0m")
        print("\033[91mGame is Finished\033[0m")
        if self.score_player1 > self.score_player2:
            print("\033[91mPlayer one wins the Game\033[0m")  # Red color for winner
        elif self.score_player2 > self.score_player1:
            print("\033[91mPlayer two wins the Game\033[0m")  # Red color for winner
        else:
            print("Its a tie!!!")



if __name__ == "__main__":
    #user_input = input

    try:
        game = Game(HumanPlayer(), RockPlayer())
        game.play_game()
    except Exception as e:
        print(f"An error occur: {e}")

    try:
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    except Exception as e:
        print(f"An error occur: {e}")

    try:
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game()
    except Exception as e:
        print(f"An error occur: {e}")

    try:

        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()
    except Exception as e:
        print(f"An error occur: {e}")



