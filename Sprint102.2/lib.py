matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

diagonal =[matrix[i][i] for i in range(len(matrix))]

print(diagonal)