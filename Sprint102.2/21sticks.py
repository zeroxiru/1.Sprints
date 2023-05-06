def main():
  # Your code here
  num_sticks = 21
  total_num_sticks_player1 = 0
  total_num_sticks_player2 = 0

  while num_sticks > 0:
      print(f"Wellcome to the sticks of pile Game.")
      print(f"{num_sticks} sticks in the pile.")
      input_line_for_player1 = int(input("Player one takes(1 -3 sticks): "))
      num_sticks -= input_line_for_player1
      #print(f'{num_sticks} are remaining in the pile')
      if num_sticks == 0:
          print("Player 2 wins")
          break
      else:
          print(f"{num_sticks} sticks are remaining in the pile.")

      while input_line_for_player1 not in [1, 2, 3]:
          input_line_for_player1 = int (input("Invalid input. Please enter a value between 1-3: "))

      input_line_for_player2 = int(input("Player two takes(1 -3 sticks): "))
      num_sticks -= input_line_for_player2
      if num_sticks == 0:
          print("Player 1 Wins")
          break
      else:
          print(f"{num_sticks} sticks in the pile.")
      while input_line_for_player2 not in [1, 2, 3]:
          input_line_for_player2 = int (input("Invalid input.Please enter a value between 1-3:"))








if __name__ == "__main__":
  main()
