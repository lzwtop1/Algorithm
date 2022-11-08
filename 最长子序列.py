# -*- coding: utf-8 -*-
# @Time : 2022/7/19 21:05
# @Author : zhengweili
# @Email : genius.lizhengwei@outlook.com
# @File : 最长子序列.py
# @Project : Algorithm
nums = [9, 11, 1, 19, -9, 10, 11, 1, 5, 3, 4, 5, 6, 7]


def zuichangzixulie(nums):
    if not nums:
        return 0
    nums = set(nums)
    nums = sorted(nums)
    left, right=0,0
    leftidx,rightidx=0,1
    for rightidx in range(len(nums)):
        index=leftidx
        if (nums[rightidx] - nums[leftidx] == 1):
            leftidx+=1
            rightidx+=1
        if (leftidx != index) and (rightidx-index > right-left):
            left=index
            right=rightidx
        else:
            leftidx += 1
            rightidx += 1
    print(right - left)


zuichangzixulie(nums)
