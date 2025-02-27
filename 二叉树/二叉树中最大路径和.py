# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

# 路径和 是路径中各节点值的总和。

# 给你一个二叉树的根节点 root ，返回其 最大路径和 。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 比较当前节点，当前节点加左子树，当加右，当加左右的最大值
        # 注意返回的时候只能返回单边最大值，不能返回跨双边的最大值
        if not root:
            return 0

        self.max = root.val

        def Max(root):
            if not root:
                return 0
            left = Max(root.left)
            right = Max(root.right)
            self.max = max(root.val,root.val+left,root.val+right,root.val+left+right,self.max)
            return max(root.val,root.val+left,root.val+right,0)

        max_num = Max(root)
        return self.max


   
