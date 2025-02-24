# 给你一棵二叉树的根节点，返回该树的 直径 。

# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

# 两节点之间路径的 长度 由它们之间边数表示。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 递归计算（深度优先）左右子树的高度，更新最大直径与左右子树高度之和的大小

      
        self.dia = 0
        self.dfs(root)
        return self.dia

    def dfs(self, root):
        if not root:
            return 0
        left_high = self.dfs(root.left)
        right_high = self.dfs(root.right)
        self.dia = max(self.dia,left_high+right_high)
        return max(left_high, right_high)+1
