def multiply_matrices(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Example usage
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
print(multiply_matrices(mat1, mat2))

