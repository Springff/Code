# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

class Solution():
    def generateParenthesis(self,n):
        # 约束条件：
        # 左括号不能超过n
        # 右括号不能超过左括号
        # 字符串长度为2n时结束
        def backtrack(s,left,right):
            if len(s) == 2*n:
                out.append(s)

            if left < n:
                backtrack(s+'(',left+1,right)
            if right < left:
                backtrack(s+')',left,right+1)
        
        out = []
        s = ''
        backtrack(s,0,0)
        return out
                