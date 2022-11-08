def max_matrix_area(matrix):
    if not matrix: return 0
    m, n = len(matrix), len(matrix[0])
    # print(matrix)
    # print(m)
    # print(n)
    pre = [0] * (n + 1)
    res = 0
    for i in range(m):
        for j in range(n):
            pre[j] = pre[j] + 1 if matrix[i][j] == "1" else 0

        stack = [-1]
        for k, num in enumerate(pre):
            while stack and pre[stack[-1]] > num:
                index = stack.pop()
                res = max(res, pre[index] * (k - stack[-1] - 1))
            stack.append(k)
    return res


N = int(input())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().rstrip())))
# for i in range(0,N):
#     for j in range(0,N):
#         matrix[i][j]=input()
result = max_matrix_area(matrix)
print(result)
