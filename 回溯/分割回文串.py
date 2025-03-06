# 给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

class Solution():
    def fenge(self,s):
        def is_hw(char):
            return char==char[::-1]
        def backtrack(star):
            if star==len(s):
                out.append(path[:])
                return 
            for end in range(star+1,len(s)+1):
                if is_hw(s[star:end]):
                    path.append(s[star:end])
                    backtrack(end)
                    path.pop()
        
        out = []
        path = []
        backtrack(0)
        return out
