def main():
    num_sticks = 21
    total_num_sticks_player1 = 0
    total_num_sticks_player2 = 0

    print(f"Welcome to the sticks of pile Game.")
    print(f"{num_sticks} sticks in the pile.")

    while num_sticks > 0:

        input_line_for_player1 = int(input("Player one takes(1 -3 sticks): "))
        while input_line_for_player1 not in [1, 2, 3]:
            input_line_for_player1 = int(input("Invalid input. Please enter a value between 1-3: "))
        num_sticks -= input_line_for_player1
        total_num_sticks_player1 += input_line_for_player1
        print(f"{num_sticks} sticks are remaining in the pile.")
        if num_sticks == 0:
            #print("Player 2 wins")
           # print(f"Total number of sticks taken by Player 1: {total_num_sticks_player1}")
           # print(f"Total number of sticks taken by Player 2: {total_num_sticks_player2}")
            if total_num_sticks_player1 > total_num_sticks_player2:
                print("Player 1 is the winner!")
            elif total_num_sticks_player2 > total_num_sticks_player1:
                print("Player 2 is the winner!")
            else:
                print("The game is tied!")
            break

        input_line_for_player2 = int(input("Player two takes(1 -3 sticks): "))
        while input_line_for_player2 not in [1, 2, 3]:
            input_line_for_player2 = int (input("Invalid input. Please enter a value between 1-3:"))
        num_sticks -= input_line_for_player2
        total_num_sticks_player2 += input_line_for_player2
        print(f"{num_sticks} sticks are remaining in the pile.")
        if num_sticks == 0:
            #print("Player 1 Wins")
            #print(f"Total number of sticks taken by Player 1: {total_num_sticks_player1}")
            #print(f"Total number of sticks taken by Player 2: {total_num_sticks_player2}")
            if total_num_sticks_player1 > total_num_sticks_player2:
                print("Player 1 is the winner!")
            elif total_num_sticks_player2 > total_num_sticks_player1:
                print("Player 2 is the winner!")
            else:
                print("The game is tied!")
            break

if __name__ == "__main__":
    main()
