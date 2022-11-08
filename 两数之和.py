# -*- coding: utf-8 -*-
# @Time : 2022/5/13 14:23
# @Author : zhengweili
# @Email : genius.lizhengwei@outlook.com
# @File : 两数之和.py
# @Project : Algorithm
# @Description :给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

def twoSum(nums, target):
    for i in range(len(nums)):
        if (target-nums[i]) in nums:
            if (nums.count(target-nums[i])==1&(target-nums[i]==nums[i])):#判断找到的是不是同一个本身
                continue
            else:j=nums.index(target-nums[i])
            return [i,j]

nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
