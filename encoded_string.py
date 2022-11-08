#
#
# @param str string字符串
# @return string字符串
#
str=input()
def computeString(str):
    # write code here
    n = len(str)
    num_stack = []
    ch_stack = []
    i = 0
    while i < n:
        if str[i].isdigit():
            res = 0
            while i < n and str[i].isdigit():
                res = res * 10 + int(str[i])
                i += 1
            num_stack.append(res)
        if str[i] == '*':
            i += 1
            continue
        if str[i] == '[':
            ch_stack.append('[')
            i += 1
            continue
        if str[i].isalpha():
            ch_stack.append(str[i])
            i += 1
            continue
        if str[i] == ']':
            tmp = ""
            while ch_stack and ch_stack[-1] != '[':
                tmp = ch_stack[-1] + tmp
                ch_stack.pop()
            if ch_stack and ch_stack[-1] == '[':
                ch_stack.pop()
            if num_stack:
                tmp = tmp * num_stack[-1]
                num_stack.pop()
            for c in tmp:
                ch_stack.append(c)
            i += 1
    return "".join(ch_stack)

a=computeString(str)
print(a)
