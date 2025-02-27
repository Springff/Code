# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 递归寻找匹配节点（空，p,q)，观察左右子树返回值
        if not root or root==p or root==q:
            return root
        p1 = self.lowestCommonAncestor(root.left,p,q)
        p2 = self.lowestCommonAncestor(root.right,p,q)
        if p1 and p2:
            return root
        if p1:
            return p1
        return p2
