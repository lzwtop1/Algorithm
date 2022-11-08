# -*- coding: utf-8 -*-
# @Time : 2022/11/7 22:49
# @Author : zhengweili
# @Email : genius.lizhengwei@outlook.com
# @File : 15. 三数之和.py
# @Project : Algorithm
nums = [-1, 0, 1, 2, -1, -4]


def threeSum(nums):
    res = []
    n = len(nums)
    nums.sort()
    if n < 3:
        return res
    for i in range(n):
        if nums[i] > 0:
            return res
        if (i > 0 and nums[i] == nums[i + 1]):
            continue
        L = i + 1
        R = n - 1
        while (L < R):
            if (nums[i] + nums[L] + nums[R] == 0):
                res.append([nums[i], nums[L], nums[R]])
                while (L < R and nums[L] == nums[L + 1]):
                    L += 1
                while (L < R and nums[R] == nums[R - 1]):
                    R -= 1
                L += 1
                R -= 1
            elif (nums[i] + nums[L] + nums[R] < 0):
                L += 1
            else:
                R -= 1
    return res


result = threeSum(nums)
print(result)
