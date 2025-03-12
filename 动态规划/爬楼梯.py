# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        
        d=[0]*n
        d[0]= 1
        d[1]=2
        for i in range(2,n):
            d[i] = d[i-1]+d[i-2]

        return d[-1]
