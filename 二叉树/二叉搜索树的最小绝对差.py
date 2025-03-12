# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

# 差值是一个正数，其数值等于两值之差的绝对值。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 最小值存在与根节点与左树最右节点和右数最左节点之间
        # 思路是对的，但实现过程还可以更优化，中序遍历
        self.mini = float('inf')
        self.out(root)
        return self.mini

    def out(self,root):
        if not root:
            return
        self.Mini(root)
        self.out(root.left)
        self.out(root.right)

    def Mini(self,root):
        t = root
        if t.left:
            t = t.left
            if t.right:
                while t.right.right:
                    t = t.right
                t=t.right
            temp = t.val-root.val
            if temp<0:
                temp=-temp
            if temp<self.mini:
                self.mini = temp
        if root.right:
            t = root.right
            if t.left:
                while t.left.left:
                    t = t.left
                t = t.left
            temp = t.val-root.val
            if temp<0:
                temp=-temp
            if temp<self.mini:
                self.mini = temp

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 最小值存在与根节点与左树最右节点和右数最左节点之间
        # 思路是对的，但实现过程还可以更优化，中序遍历
        
        self.mini = float('inf')
        self.pre = float('inf')
        self.Inorder(root)
        return self.mini
    def Inorder(self,root):
        if not root:
            return
        self.Inorder(root.left)
        temp = root.val-self.pre
        if temp<0:
            temp = -temp
        if temp<self.mini:
            self.mini = temp
        self.pre = root.val
        self.Inorder(root.right)

            
        
