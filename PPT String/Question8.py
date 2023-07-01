def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result = [[0] * n for _ in range(m)]
    mat1_nonzero = {}

    for i in range(m):
        mat1_nonzero[i] = {}
        for j in range(k):
            if mat1[i][j] != 0:
                mat1_nonzero[i][j] = mat1[i][j]

    for i in range(m):
        for j in range(n):
            for col in mat1_nonzero[i]:
                result[i][j] += mat1_nonzero[i][col] * mat2[col][j]

    return result


mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(multiply(mat1, mat2))
