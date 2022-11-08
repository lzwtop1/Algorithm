#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re
# class Solution:
#     def longestDecomposition(self, text: str) -> int:
#         n = len(text)
#         i, pre_i = 0, -1
#         ans = 0
#         j = n - 1
#         while i <= j:  # 写成while True也行
#             while text[i] != text[j]:  # 一定会结束
#                 i += 1
#             # print("i, j:",i, j)
#             if i == j:
#                 ans += 1
#                 break
#             elif i < j:
#                 l = i - pre_i
#                 flag = True
#                 for k in range(0, l):
#                     if text[j - k] == text[i - k]:
#                         continue
#                     else:
#                         flag = False
#                         break
#                 if flag:
#                     # 程序成功遍历结束
#                     pre_i = i
#                     i += 1
#                     j = j - l
#                     ans += 2
#                 else:
#                     i += 1
#             else:
#                 break
#         return ans
# class Solution:
#     def longestDecomposition(self, text: str) -> int:
    # n = len(text)
    # res = 0
    # L0, L = 0, 0  # 当前这段[L0,  L]
    # R = n - 1
    # while L <= R:
    #     while text[L] != text[R]:
    #         L += 1
    #     if L == R:  # 相遇了
    #         res += 1
    #         return res
    #     elif L < R:
    #         word_len = L - L0 + 1  # 当前这段的长度
    #         if text[L0: L + 1] == text[R - word_len + 1: R + 1]:
    #             res += 2
    #             L += 1
    #             L0 = L
    #             R -= word_len
    #         else:
    #             L += 1
    #     elif L > R:
    #         break
    # return res
class Solution:
    def longestDecomposition(self, text: str) -> int:
        sum_huiwen=[]
        res = 0
        while text:
            for i in range(1, len(text)//2+1):
                if text[:i] == text[-i:]:
                    text = text[i:-i]
                    res += 2
                    break
            else:
                return res + 1
        return res


try:
    n_text = input()
except:
    n_text = None

s = Solution()
res = s.longestDecomposition(n_text)

print(str(res) + "\n")

