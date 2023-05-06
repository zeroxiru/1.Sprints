def islandPerimeter(grid):
    perimeter = 0  # initialize the variable perimeter to 0
    row, col = len(grid), len(grid[0])  # get the number of rows and columns in the grid
    for i in range(row):  # iterate over each row in the grid
        for j in range(col):  # iterate over each column in the grid
            if grid[i][j] == 1:  # if the current cell is land
                if i == 0 or grid[i-1][j] == 0:  # if the cell to the north is water or out of bounds
                    perimeter += 1  # increment the perimeter
                if j == 0 or grid[i][j-1] == 0:  # if the cell to the west is water or out of bounds
                    perimeter += 1  # increment the perimeter
                if i == row-1 or grid[i+1][j] == 0:  # if the cell to the south is water or out of bounds
                    perimeter += 1  # increment the perimeter
                if j == col-1 or grid[i][j+1] == 0:  # if the cell to the east is water or out of bounds
                    perimeter += 1  # increment the perimeter
    return perimeter  # return the final perimeter of the island
