# -*- coding: utf-8 -*-
# @Time : 2022/11/7 20:56
# @Author : zhengweili
# @Email : genius.lizhengwei@outlook.com
# @File : 816. 模糊坐标.py
# @Project : Algorithm
s="(123)"

def ambiguousCoordinates(s):
    def get_pos(s) :
        pos = []
        if s[0] != '0' or s == '0':
            pos.append(s)
        for p in range(1, len(s)):
            if p != 1 and s[0] == '0' or s[-1] == '0':
                continue
            pos.append(s[:p] + '.' + s[p:])
        return pos

    n = len(s) - 2
    res = []
    s = s[1: len(s) - 1] #去括号
    print(s) #123
    for l in range(1, n):
        lt = get_pos(s[:l])
        if len(lt) == 0:
            continue
        rt = get_pos(s[l:])
        if len(rt) == 0:
            continue
        for i, j in product(lt, rt):
            res.append('(' + i + ', ' + j + ')')
    return res

ambiguousCoordinates(s)