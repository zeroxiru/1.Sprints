import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return [moves]

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def __init__(self, user_input):
        self.user_input = user_input

    def move(self):
        while True:
            user_choice = self.user_input("Type Rock/Paper/Scissors or Q to quit: ").lower()
            if user_choice not in moves:
                print("Invalid input. Please choose Rock, Paper, or Scissors.")
                continue
            return user_choice



def beats(one, two):
    # return ((one == 'rock' and two == 'scissors') or
    #         (one == 'scissors' and two == 'paper') or
    #         (one == 'paper' and two == 'rock'))
    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    return one == winning_combinations[two]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score_p1 += 1
            print("Player 1 wins the round")
        elif beats(move2, move1):
            self.score_p2 += 1
            print("Player2 wins the round")
        else:
            print("Its a tie")


    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round +1}:")
            self.play_round()
        if self.score_p1 > self.score_p2:
            print("Player 1 win the game")
        elif self.score_p2 > self.score_p1:
            print("Player 2 wins the game")
        else:
            print("It's a tie!")
        print("Game over!")



if __name__ == '__main__':
    user_input = input()
    game = Game(HumanPlayer(user_input), RandomPlayer())
    game.play_game()