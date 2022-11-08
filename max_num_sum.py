def MaxSubArr(nums):
    n=len(nums)
    if n==1: return nums[0]
    pre=nums[0]
    mark=pre
    for i in range(1,n):
        pre=nums[i]+max(pre,0)
        mark=max(mark,pre)
    return mark

#
arr=input()
nums=int(input())
a=MaxSubArr(nums)
print(a)