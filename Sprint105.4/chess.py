import numpy as np
import matplotlib.pyplot as plt


def display_matrix(data):
    size = [len(data),len(data[0])]

    # Display the data
    fig, ax = plt.subplots()
    cax = ax.matshow(data, cmap='gray_r', vmin=0, vmax=1)  # '_r' reverse the color map

    # Major ticks
    ax.set_xticks(np.arange(0, size[1], 1))
    ax.set_yticks(np.arange(0, size[0], 1))

    # Minor ticks
    ax.set_xticks(np.arange(-.5, size[1], 1), minor=True)
    ax.set_yticks(np.arange(-.5, size[0], 1), minor=True)

    # Gridlines based on minor ticks
    ax.grid(which='minor', color='grey', linestyle='-', linewidth=2)

    plt.show()


def color_diagonal(size):
    chessboard = np.zeros((size, size))

    # Color the diagonal
    for i in range(size):
        for j in range(size):
            if i == j:
                chessboard[i, j] = 1

    # Display the chessboard
    display_matrix(chessboard)


# Usage example
size = 8
color_diagonal(size)