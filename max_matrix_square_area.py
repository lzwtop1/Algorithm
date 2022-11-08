import numpy as np
def max_matrix_square_area(matrix):
    m, n = len(matrix), len(matrix[0])
    # print(m)
    # print(n)
    dp = [[0] * n for _ in range(m)]
    res = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                if j - 1 >= 0 and i - 1 >= 0:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 1
                res = max(dp[i][j], res)
    return res *res

N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().rstrip())))
print(matrix[1])
result = max_matrix_square_area(matrix)
print(result)
