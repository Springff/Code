# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        ### 为什么要从target倒序遍历，为了防止重复利用的情况，例如target=4，但是nums里只有一个2
        target = 0
        for num in nums:
            target = target + num
        if target%2==1:
            return False
        target = target/2
        dp = [0]*(target+1)
        dp[0] = 1
        for num in nums:
            for i in range(target,num-1,-1):
                if dp[i-num]:
                    dp[i] = 1
        if dp[target]==1:
            return True
        return False
