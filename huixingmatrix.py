n = int(input())

def nnmatrix(n):
    a = [[0 for i in range(n)] for j in range(n)]
    p = 0
    q = n - 1
    t = 1
    while p < q:
        for i in range(p, q):
            a[p][i] = t
            t = t + 1
        for i in range(p, q):
            a[i][q] = t
            t = t + 1
        for i in range(q, p, -1):
            a[q][i] = t
            t = t + 1
        for i in range(q, p, -1):
            a[i][p] = t
            t = t + 1
        p = p + 1
        q = q - 1
    if p == q: a[p][p] = t
    for i in range(n):
        print(a[i])

test=nnmatrix(n)
print(test)
