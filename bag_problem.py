T=input()
N, V = map(int, input().split())
print(T)
print(N,V)
bones = []
for i in range(N):
    bones.append([int(i) for i in input().split()])
print(bones)
# dp = [[0 for i in range(V + 1)] for j in range(N + 1)]
#
# for i in range(1, N + 1):
#     for j in range(1, V + 1):
#         dp[i][j] = dp[i - 1][j]
#         if j >= bones[i - 1][0]:
#             dp[i][j] = max(dp[i][j], dp[i - 1][j - bones[i - 1][0]] + bones[i - 1][1])
#
# print(dp[-1][-1])
