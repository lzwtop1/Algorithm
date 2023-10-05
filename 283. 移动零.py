from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:  # 如果不为0，就把当前元素和j位置的元素交换
                print('xuhao', i, j)
                print(nums)
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


# 示例输入
nums = [0, 1, 0, 3, 12]
# 创建 Solution 类的实例
solution = Solution()
# 调用 moveZeroes 方法
solution.moveZeroes(nums)
# 输出结果
print(nums)
