# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

# 你可以认为每种硬币的数量是无限的。


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 遍历所有硬币
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin==i:
                    dp[i]=1
                elif coin<i:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        for i in range(len(dp)):
            if dp[i]==float('inf'):
                dp[i]=-1
        return dp[-1]
