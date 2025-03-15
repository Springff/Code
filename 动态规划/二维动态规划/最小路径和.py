# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 一步一步走，计算每步的最小花费
        m = len(grid)
        n = len(grid[0])

        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j] = grid[i][j]
                elif i==0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif j==0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j])+grid[i][j]
        return dp[m-1][n-1]
