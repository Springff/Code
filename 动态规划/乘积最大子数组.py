# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

# 测试用例的答案是一个 32-位 整数。

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 维护一个最大值和一个最小值，无论正负，最大值一定在其中产生
        max_dp=[float('-inf')]*len(nums)
        min_dp=[float('inf')]*len(nums)
        max_prodect = float('-inf')
        for i in range(len(nums)):
            if nums[i]>=0:
                max_dp[i] = max(nums[i],max_dp[i-1]*nums[i])
                min_dp[i] = min(nums[i],min_dp[i-1]*nums[i])
            else:
                max_dp[i] = max(nums[i],min_dp[i-1]*nums[i])
                min_dp[i] = min(nums[i],max_dp[i-1]*nums[i])
            max_prodect = max(max_prodect,max_dp[i])

        return max_prodect
        
