remainTickets=[4,7,9]

remainTickets.sort()
b_len=remainTickets[-1]
print(b_len)
b=[]
for num in range(1,b_len+1):
    b.append(num)
res = []
for i in b:
    if i not in remainTickets:
        res.append(i)
print(res)