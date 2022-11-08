s = "babad"

def huiwen(s):
    n=len(s)
    if n < 2: return s
    max_len=1
    for j in range(1,n):
        for i in range(j):
            if s[i:j] == s[i:j][::-1]:  # 倒序检测回文
                cur_len=j-i+1
                if max_len>cur_len:
                    max_len=cur_len
    return s[i:i+max_len]
n=huiwen(s)
print(n)