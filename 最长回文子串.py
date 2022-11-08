# -*- coding: utf-8 -*-
# @Time : 2022/11/7 21:17
# @Author : zhengweili
# @Email : genius.lizhengwei@outlook.com
# @File : 最长回文子串.py
# @Project : Algorithm

s = "babad"


def longestPalindrome(s: str) -> str:
    size = len(s)
    # 特殊处理
    if size == 1:
        return s
    # 创建动态规划dynamic programing表
    dp = [[False for _ in range(size)] for _ in range(size)]
    # 初始长度为1，这样万一不存在回文，就返回第一个值（初始条件设置的时候一定要考虑输出）
    max_len = 1
    start = 0
    for j in range(1, size):
        for i in range(j):
            # 边界条件：
            # 只要头尾相等（s[i]==s[j]）就能返回True
            if j - i <= 2:
                if s[i] == s[j]:
                    dp[i][j] = True
                    cur_len = j - i + 1
            # 状态转移方程
            # 当前dp[i][j]状态：头尾相等（s[i]==s[j]）
            # 过去dp[i][j]状态：去掉头尾之后还是一个回文（dp[i+1][j-1] is True）
            else:
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    cur_len = j - i + 1
            # 出现回文更新输出
            if dp[i][j]:
                if cur_len > max_len:
                    max_len = cur_len
                    start = i

    return s[start:start + max_len]


s = longestPalindrome(s)
print(s)
