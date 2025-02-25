# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 平衡 二叉搜索树。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        # 递归的构建树的根节点
        length = len(nums)
        num = length//2
        root = TreeNode(nums[num])
        root.left = self.sortedArrayToBST(nums[:num])
        root.right = self.sortedArrayToBST(nums[num+1:])
        return root
