# 请设计一个机械累加器，计算从 1、2... 一直累加到目标数值 target 的总和。注意这是一个只能进行加法操作的程序，不具备乘除、if-else、switch-case、for 循环、while 循环，及条件判断语句等高级功能。
class Solution(object):
    def mechanicalAccumulator(self, target):
        """
        :type target: int
        :rtype: int
        """
        return target and target+self.mechanicalAccumulator(target-1)  or 0
        # and 的作用是 如果左右均为真，则返回最后一个真值，否则返回第一个假值
        # or 的作用是 如果左边为真，返回左边，否则返回右边
