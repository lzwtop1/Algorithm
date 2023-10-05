class Solution:
    # baoli
    def trap_baoli(self, height) -> int:
        sum_rain = 0
        for i in range(len(height)):
            max_left = 0
            max_right = 0
            for j in range(0, i):
                max_left = max(height[j], max_left)
            for j in range(i, len(height)):
                max_right = max(height[j], max_right)
            if min(max_left, max_right) > height[i]:
                sum_rain += min(max_left, max_right) - height[i]
        return sum_rain

    def trap_shuangzhizhen(self, height):
        if not height:
            return 0
        n = len(height)
        left = 0
        right = n - 1
        max_left = height[left]
        max_right = height[right]
        sum_rain = 0

        while left <= right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            if max_left < max_right:
                sum_rain += max_left - height[left]
                left += 1
            else:
                sum_rain += max_right - height[right]
                right -= 1
        return sum_rain
