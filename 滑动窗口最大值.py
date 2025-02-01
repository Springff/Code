# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# 返回 滑动窗口中的最大值 。

class Solution():
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 暴力破解
        ans = []

        for i in range(len(nums)-k+1):
            max = nums[i]
            for j in range(i,i+k):
                if max < nums[j]:
                    max = nums[j]
            ans.append(max)
        
        return ans


    def shuangduanduilie(nums,k):
        # 双端队列
        # 维护一个单调减小的双端队列，队列中存储的是索引。
        # 每次窗口滑动，检查队首索引是否仍在窗口内，若不在，则弹出该索引。
        # 将小于当前值的索引全部从队尾弹出
        # 将队首元素加入输出队伍中
        
        ans = []
        window = deque()

        for i,num in enumerate(nums):
            if window and window[0]<i-k+1:# 滑动窗口的范围要搞清楚
                window.popleft()
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            if i > k-2:
                ans.append(nums[window[0]])
        
        return ans

from collections import deque
import sys

nums = sys.stdin.readline().strip()
nums = list(map(int,nums.split(',')))
k = sys.stdin.readline().strip()
k = int(k)

solution = Solution()
ans = solution.maxSlidingWindow(nums,k)
print(ans)

