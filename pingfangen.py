def sqrt(N):
    left, right = 1, N / 2 + 1
    while (left <= right):
        mid = (left + right) // 2
        if mid > N / mid:
            right = mid - 1
        elif mid< N/mid:
            left = mid+1
        else:
            return int(mid)
    return int(right)

N=int(input())
re=sqrt(N)
print(re)