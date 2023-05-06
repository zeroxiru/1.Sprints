def islandPerimeter(grid):
    perimeter = 0
    row, col = len(grid), len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if i == row-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == col-1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
perimeter = islandPerimeter(grid)
print(perimeter)

