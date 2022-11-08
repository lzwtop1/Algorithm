s=input()
def getstr(s:str):
    res=tmp=0
    dic={}
    for j in range(len(s)): #索引
        i=dic.get(s[j],-1)#返回指定键值
        print(i)
        dic[s[j]] = j
        tmp=tmp+1 if tmp<j-i else j-i
        res=max(tmp,res)
    return res

a=getstr(s)
print(a)