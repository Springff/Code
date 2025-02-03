# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和子数组
# 是数组中的一个连续部分

class Solution():
    def MaxSubArray(self, nums):
        # 维护一个current_sum,如果其大于0，则继续加和；若小于0，则从下一个值重新计算
        # 遍历过程中，不断比较，纪录最大值。

        current_sum = 0
        max_num = nums[0]

        for num in nums:
            if current_sum < 0:
                current_sum = num
            else:
                current_sum += num
            if max_num < current_sum:
                max_num = current_sum
        return max_num

import sys
nums = sys.stdin.readline().strip()
nums = list(map(int,nums.split(',')))

solution = Solution()
ans = solution.MaxSubArray(nums)
print(ans)
