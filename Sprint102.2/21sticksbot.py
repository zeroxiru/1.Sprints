
import random


def main():
    num_sticks = 21
    total_num_sticks_bot = 0
    total_num_sticks_player1 = 0

    print(f"Welcome to the sticks of pile game.")
    print(f"{num_sticks} sticks in the pile.")

    # Bot plays first and always removes a random number of sticks between 1 and 3.
    bot_input = random.randint(1, 3)
    num_sticks -= bot_input
    total_num_sticks_bot += bot_input
    print(f"The bot removed {bot_input} sticks.\n{num_sticks} sticks are remaining in the pile.")

    # Check if the game is over after the bot's move.
    if num_sticks == 0:
        if total_num_sticks_bot > total_num_sticks_player1:
            print("The bot wins!")
        elif total_num_sticks_player1 > total_num_sticks_bot:
            print("You win!")
        else:
            print("The game is tied!")
        return

    while num_sticks > 0:
        # Player 2 inputs the number of sticks they want to remove.
        player1_input = int(input("You take (1-3) sticks: "))

        # Ensure valid input from Player 2.
        while player1_input not in [1, 2, 3]:
            player1_input = int(input("Invalid input. Please enter a value between 1-3: "))
        num_sticks -= player1_input
        total_num_sticks_player1 += player1_input
        print(f"{num_sticks} sticks are remaining in the pile.")

        # Check if the game is over after Player 2's move.
        if num_sticks == 0:
            if total_num_sticks_bot > total_num_sticks_player1:
                print("The bot wins!")
            elif total_num_sticks_player1 > total_num_sticks_bot:
                print("You win!")
            else:
                print("The game is tied!")
            break

        # Bot plays next and removes sticks such that the total number of remaining sticks
        # is a multiple of 4. If the remaining sticks are already a multiple of 4, it removes
        # a random number of sticks between 1 and 3.
        if num_sticks % 4 == 0:
            bot_input = random.randint(1, 3)
        else:
            bot_input = num_sticks % 4
        num_sticks -= bot_input
        total_num_sticks_bot += bot_input
        print(f"The bot removed {bot_input} sticks. {num_sticks} sticks are remaining in the pile.")

        # Check if the game is over after the bot's move.
        if num_sticks == 0:
            if total_num_sticks_bot > total_num_sticks_player1:
                print("The bot wins!")
            elif total_num_sticks_player1 > total_num_sticks_bot:
                print("You win!")
            else:
                print("The game is tied!")
            break


if __name__ == "__main__":
    main()