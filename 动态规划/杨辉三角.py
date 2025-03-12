# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        out = []
        for i in range(numRows):
            ans = [1]*(i+1)
            if i<2:
                out.append(ans)
                continue
            for j in range(1,i):
                ans[j]=out[-1][j-1]+out[-1][j]
            out.append(ans)
        return out
