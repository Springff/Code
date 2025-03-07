# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

# 如果数组中不存在目标值 target，返回 [-1, -1]。

# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 还是二分查找，在查找到目标值之和向左右扩展
        if not nums:
            return [-1,-1]
        star = 0
        end = len(nums)-1

        while star<=end:
            mid = (star+end)//2
            if nums[mid]==target:
                break
            if nums[mid]<target:
                star = mid+1
            else:
                end = mid-1    
        if nums[mid]!=target:
            return [-1,-1]
        i = mid
        while i<len(nums) and nums[i]==target:
            i += 1
        j = mid
        while j>-1 and nums[j]==target:
            j -= 1
        return [j+1,i-1]
        
