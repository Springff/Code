# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯
        self.result = []
        path = []
        self.back(0,nums,path)
        return self.result

    def back(self,star,nums,path):
        self.result.append(path[:])

        for i in range(star,len(nums)):
            path.append(nums[i])
            self.back(i+1,nums,path)
            path.pop()


solution = Solution()
ans = solution.subsets([1,2,3])