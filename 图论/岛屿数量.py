# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 遇到一块陆地以后，将所有陆地置为0，当下次遇到1时，陆地数加一

        nums = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    nums += 1
                    self.dfs(grid,i,j)
        return nums
    
    def dfs(self,grid,r,c):
        if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]=='0':
            return
        grid[r][c]='0'
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)
