
# add more tests here, call your function
def print_triangle(n):
    # Print upper triangle with  loop over each row
    for i in range(1, n+1):
        row = ""
        # loop over each number in the row
        for j in range(1, i+1):
            # Add the number to the row string, followed by a space
            row += str(j) + " "
        # # Printin the row  string , with left-justified with a total of n*2 chacracters
        print(row.ljust(n*2))

    #Print lower triangle with  loop over each row (excluding the first row, which has already been printed)
    for i in range(n-1, 0, -1):
        row = ""
        # loop over the each numbe rof the row
        for j in range(1, i+1):
            # Add the number to the row string, followed by a space
            row += str(j) + " "
        # Print the row string, left-justified with a total width of n*2 characters
        print(row.ljust(n*2))
def print_multiplication_table(n):
    header_row = " ".join(str(i) for i in range(1, n+1))
    print(" " + header_row)

    # print the table rows
    for i in range(1, n+1):
        row = ""

        for j in range(1, n+1):
             row += str(i * j) + " "
        print(str(i) + " " + row)


#print_triangle(7)
#print_multiplication_table(5)

def main():
    while True:
        n = int(input("Enter a number (-1 to exit): "))
        if n == -1:
            print("Bye!")
            break

        command = input("Enter a command (traingle or mp): ")

        if command == "traingle":
            print_triangle(n)
        elif command == "mp":
             print_multiplication_table(n)
        else:
             print("Invalid cmmand")





if __name__ == "__main__":
  main()