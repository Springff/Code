# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 用一些额外的空间来保存数组
        
        k = k%len(nums)
        if k==0:
            return 
        nums[0:k],nums[k:] = nums[-k:],nums[0:-k]
        return 

nums = input()
k = int(input())
nums = list(map(int,nums.split(',')))

solution = Solution()
solution.rotate(nums,k)
print(nums)