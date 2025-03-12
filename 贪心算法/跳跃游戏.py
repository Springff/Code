# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 维护一个最远边界，遍历数组，如果遍历到最远边界输出false；如果最远边界达到数组长度，输出true

        largest = nums[0]
        for i in range(len(nums)):
            if largest>=len(nums)-1:
                return True
            if i>largest:
                return False
            if nums[i]+i>largest:
                largest = nums[i]+i
