
# 给定一个二叉树 root ，返回其最大深度。

# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 遍历二叉树，纪录最大深度
        
        return self.Depth(root,0)

    def Depth(self,root,depth):
        if root == None:
            return depth
        depth += 1
        left_depth = self.Depth(root.left,depth)
        right_depth = self.Depth(root.right,depth)
        return max(left_depth,right_depth)
    def diedai(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 中序遍历二叉树，纪录最大深度
        depth = 0
        max_d = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                depth += 1
                if depth > max_d:
                    max_d = depth
                stack.append((curr,depth))
                curr = curr.left
            curr,depth = stack.pop()
            
            
            curr = curr.right
               
            

        return max_d
