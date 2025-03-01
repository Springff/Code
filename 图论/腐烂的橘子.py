# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。


from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 维护一个队列，保存边缘腐烂的橘子，再维护一个新鲜橘子的数量，当没有橘子可以再腐烂时，查看新鲜橘子的数量
        queue = deque()
        row = len(grid)
        col = len(grid[0])
        fresh = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh += 1
        if fresh==0:
            return 0
        time = 0
        while queue and fresh>0:#只有还能继续蔓延时time才增加
            num = len(queue)
            for _ in range(num):
                i,j = queue.popleft()
                if j+1>=0 and j+1<col and grid[i][j+1]==1:
                    fresh-=1
                    grid[i][j+1]=2
                    queue.append((i,j+1))
                if j-1>=0 and j-1<col and grid[i][j-1]==1:
                    fresh-=1
                    grid[i][j-1]=2
                    queue.append((i,j-1))
                if i+1>=0 and i+1<row and grid[i+1][j]==1:
                    fresh-=1
                    grid[i+1][j]=2
                    queue.append((i+1,j))
                if i-1>=0 and i-1<row and j>=0 and j<col and grid[i-1][j]==1:#i,j符合条件不用再检查
                    fresh-=1
                    grid[i-1][j]=2
                    queue.append((i-1,j))
            time+=1
        if fresh!=0:
            return -1
        return time
                
