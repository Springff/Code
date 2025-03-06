# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。

# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。


### 经验：回溯算法一般都有两个边界，递归传递一个边界，遍历一个边界。

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def backtrack(row):
            if row==n:
                output.append(["".join(row) for row in ans])
                return 
            for col in range(n):
                if col not in col_list and col+row not in dia_l and col-row not in dia_r:
                    ans[row][col]='Q'
                    col_list.append(col)
                    dia_l.append(col+row)
                    dia_r.append(col-row)
                    backtrack(row+1)
                    ans[row][col]='.'
                    col_list.pop()
                    dia_l.pop()
                    dia_r.pop()
                continue
        
        col_list=[]
        dia_l = []
        dia_r = []
        
        ans = [['.' for _ in range(n)] for _ in range(n)]
        output = []
        backtrack(0)
        return output