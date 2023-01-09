# -*- coding: utf-8 -*-
# @Time : 2022/11/8 21:25
# @Author : zhengweili
# @Email : genius.lizhengwei@outlook.com
# @File : 20. 有效的括号.py
# @Project : Algorithm

s = "([{}])"


def isValid(s: str) -> bool:
    # dic={'(':')','[':']','{':'}'}
    dic = {')': '(', ']': '[', '}': '{'}
    stack = []
    for i in s:
        if stack and i in dic:
            print("dic: ", dic[i])
            if stack[-1] == dic[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)  # （
            print("i: ", i)
    return not stack


result = isValid(s)
print(result)
