# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。

# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。

# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 快慢指针，一阶段，快慢指针从0出发，在环中相遇s=u+x=ko,u=ko-x
        # 二阶段，慢指针从0出发，快指针从相遇点出发，相同速度前进，想遇点就是环入口。
        fast,slow=nums[nums[0]],nums[0]
        while nums[fast]!=nums[slow]:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = nums[0]
        while nums[fast]!=nums[slow]:
            fast = nums[fast]
            slow = nums[slow]
        return slow
