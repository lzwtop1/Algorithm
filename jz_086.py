#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re
class Solution:
    def partition(self, s: str):
        n = len(s)
        self.ans = []

        def dfs(s, path):
            if not s:
                self.ans.append(path)
                return
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    dfs(s[i+1:], path + [s[:i+1]])

        dfs(s, [])
        m=len(self.ans)
        return m

# class Solution:
#     def partition(self, s: str):
#         n = len(s)
#         dp = [[False for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True
#         for l in range(n - 1, -1, -1):
#             for r in range(l + 1, n):
#                 if s[l] == s[r]:
#                     if l + 1 == r:
#                         dp[l][r] = True
#                     else:
#                         if dp[l+1][r-1] == True:
#                             dp[l][r] = True
#
#         n = len(s)
#         res = []
#         path = []
#         m=0
#
#         def backtrace(idx: int) -> None:
#             if idx == n:
#                 res.append(path[:])
#                 return
#             for i in range(idx, n):
#                 if dp[idx][i] == True:
#                     path.append(s[idx : i + 1])
#                     backtrace(i + 1)
#                     path.pop()
#
#         backtrace(0)
#         m=len(res)
#         return m

try:
    _text = input()
except:
    _text = None

s = Solution()
res = s.partition(_text)

print(str(res) + "\n")