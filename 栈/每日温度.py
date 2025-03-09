# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # 用栈保存已经检查过的值
        stack = []
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                pre_i = stack.pop()
                ans[pre_i] = i-pre_i
            stack.append(i)

        return ans
