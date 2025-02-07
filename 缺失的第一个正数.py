# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用   常数级别额外空间    的解决方案。

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 用一个哈希表来存储出现过的正整数，遍历完数组，输出没有出现过的正整数

        map = {}
        for num in nums:
            if num > 0:
                map[num] = map.get(num,0)+1
        
        label = True
        ans = 1
        while label:
            if ans in map:
                ans += 1
            else:
                label = False
        return ans

    def FirstMissingPositive(self,nums):

        # 常数级的内存占用，考虑使用索引来检查符合要求的数
        # 用索引来检查对应的数是否存在于数组中,就不需要额外的存储空间了
        # 先标记不需要考虑的数，

        for i in range(len(nums)):
            if nums[i]<1 or nums[i]>len(nums):
                nums[i] = len(nums)+1
        
        for i in range(len(nums)):
            num = abs(nums[i])# 仔细思考一下这一步的作用，避免掉坑
            #如果不先取绝对值，在接下来的赋值操作中容易出问题
            if num<len(nums)+1:
                nums[num-1] = -abs(nums[num-1])
        
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        
        return len(nums)+1


import sys

nums = sys.stdin.readline().strip()
nums = list(map(int,nums.split(',')))

solution = Solution()
ans = solution.FirstMissingPositive(nums)
print(ans)