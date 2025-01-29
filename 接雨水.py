# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        stack = []
        t = 0

        for i,h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] - 1
                high = min(h,height[stack[-1]]) - height[top]
                t = t + high*distance
            stack.append(i)
        
        return t
    



import sys
a = sys.stdin.readline().strip()
a = list(map(int,a.split(',')))

solution = Solution()
answer  =  solution.trap(a)
print(answer)