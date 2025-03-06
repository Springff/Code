# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #使用深度优先遍历，将本位置置空，防止回退
        def dfs(i,j,k):
            if k == len(word):
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[k]!=board[i][j]:
                return False
            temp, board[i][j] = board[i][j],''
            ans = dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1) or dfs(i-1,j,k+1) 
            board[i][j] = temp
            return ans
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0]==board[i][j]:
                    if dfs(i,j,0):
                        return True

        return False


 