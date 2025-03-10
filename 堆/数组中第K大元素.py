# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ### 堆排序算法
        ##建堆
        for i in range(len(nums)//2,-1,-1):
            self.Build_D(nums,i,len(nums))
        
        for i in range(len(nums)-1,len(nums)-k-1,-1):
            nums[0],nums[i] = nums[i],nums[0]
            self.Build_D(nums,0,i)
        return nums[len(nums)-k]


    def Build_D(self,nums,i,n):
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left<n and nums[largest]<nums[left]:
            largest = left
        if right < n and nums[largest]<nums[right]:
            largest = right
        if largest!=i:
            nums[largest],nums[i] = nums[i],nums[largest]
            self.Build_D(nums,largest,n)
