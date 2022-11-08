m,n=input().split()
m=int(m)#行数
n=int(n)#列数
dp=[[0 for i in range(n)]for i in range(m)]
line=[]
for i in range(m):
    line=input().split()
    line=list(map(int,line))
    for j in range(n):
        dp[i][j]=line[j]
max=-99999999999999
sum=0


# right为右边界 left为左边界 up为上边界 down为下边界
for left in range(n):
    for right in range(left,n):
        for up in range(m):
            for down in range(up,m):
                sum=0
                for i in range(left,right+1):
                    for j in range(up,down+1):
                        sum=sum+dp[j][i]
                if sum>max:
                    max=sum
print(max)