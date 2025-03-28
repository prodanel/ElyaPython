def increase_non_diagonal_elements(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    for i in range(rows):
        for j in range(cols):
            if i != j:
                matrix[i][j] *= 2
    return matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = increase_non_diagonal_elements(matrix)
print(result)
