# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        for i in range(n):
            if nums[i]!=0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
# nums = input()
# nums = nums.split(',')
# nums = list(map(int,nums))
# print(nums)

import sys
nums = sys.stdin.readline().strip()
nums = list(map(int,nums.split(',')))
print(nums)