# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

# 求在该柱状图中，能够勾勒出来的矩形的最大面积。

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 继承自上一题最大温度，找到左右第一个小于自己的柱子

        left = [len(heights)-i-1 for i in range(len(heights))]
        right = [i for i in range(len(heights))]
        stack = []
        
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                pre_i = stack.pop()
                left[pre_i] = i-pre_i-1
            stack.append(i)
        
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i]<heights[stack[-1]]:
                pre_i = stack.pop()
                right[pre_i] = pre_i-i-1
            stack.append(i)
        
        max = 0
        for i in range(len(heights)):
            width = left[i]+right[i]+1
            if max<width*heights[i]:
                max = width*heights[i]

        return max

