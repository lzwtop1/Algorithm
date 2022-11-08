
class Solution:
    def find_greatest_sub_array(self, array):
        """
        sum_of_array记录当前子组和，当子组合<0,则重置为0，重新开始计和
        greatest_sum记录目前出现过最大的子组和
        """
        if not array:
            return

        sum_of_array = 0
        greatest_sum = array[0]

        for number in array:
            sum_of_array += number

            if sum_of_array > greatest_sum:
                greatest_sum = sum_of_array

            if sum_of_array < 0:
                sum_of_array = 0

        return greatest_sum


# 测试用例
if __name__ == '__main__':
    n=input()
    arr=input()
    arrays = [int(n) for n in arr.split()]
    s = Solution()
    for array in arrays:
        print (s.find_greatest_sub_array(array))



# def function(lists):
#     max_sum = lists[0]
#     pre_sum = 0
#     for i in lists:
#         if pre_sum < 0:
#             pre_sum = i
#         else:
#             pre_sum += i
#         if pre_sum > max_sum:
#             max_sum = pre_sum
#     return max_sum
#
#
# def main():
#     n = input()
#     arr = input()
#     lists = [int(n) for n in arr.split()]
#     print(function(lists))
#
#
# if __name__ == "__main__":
#     main()
#
