import re


# python 递归 解题
class Solution:
    def computeString(self, inputStr):
        inputStr = str(inputStr)
        K = ''
        for index, letter, in enumerate(inputStr):
            if letter != '*':
                K = K + letter
            else:
                newstr = inputStr[index + 2:-1]
                break
        num = int(re.sub("\D", "", K))
        var = ''.join(re.findall(r'[A-Za-z]', K))
        if '[' in newstr:
            the_iter = Solution().computeString(newstr)
            return var + the_iter * num
        else:
            return var + newstr * num


if __name__ == '__main__':
    inputStr = input()
    a = Solution()
    print(a.computeString(inputStr))


# def computeString(s):
#     stack = []
#     num = 0
#     res = ""
#     for i in s:
#         if i.isdigit():
#             num = num * 10 + int(i)
#         elif i == '*':
#             continue
#         elif i == "[":
#             stack.append((res, num))
#             res, num = "", 0
#         elif i == "]":
#             top = stack.pop()
#             res = top[0] + res * top[1]
#         else:
#             res += i
#     return res.strip('*')
#
# s=input()
# a=computeString(s)
# print(a)