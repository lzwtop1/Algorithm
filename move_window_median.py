'''
letcode
480. 滑动窗口中位数
'''

nums = [1,4,2,3]
k = 4
def medianSlidingWindow(nums, k):
    res = []
    arr = []
    for i in range(len(nums)-k+1):
        arr.append(nums[i:i + k])
    for t in arr:
        l, r = 0, len(t)
        t.sort()
        mid=r//2
        if r % 2 != 0:
            res.append(t[mid])
        else: res.append((t[mid - 1] + t[mid]) / 2)
    print(res)
test_func = medianSlidingWindow(nums, k)