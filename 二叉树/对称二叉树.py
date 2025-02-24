# 经验：用队列可以代替递归

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric1(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 错误思路：一个中序遍历，一个中序遍历的逆序，最后检查是否一样
        # 错误原因：不对称但是遍历结果一样的情况存在
        left = []
        right = []
        self.Preorder(root.left,left)
        self.Lastorder(root.right,right)
        if len(left)!=len(right):
            return False
        for i in range(len(right)):
            if left[i]!=right[i]:
                return False
        return True

    def Preorder(self,root,out):
        if root==None:
            return 
        self.Preorder(root.left,out)
        out.append(root.val)
        self.Preorder(root.right,out)
    
    def Lastorder(self,root,out):
        if root==None:
            return 
        self.Lastorder(root.right,out)
        out.append(root.val)
        self.Lastorder(root.left,out)
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        return self.duichen(root.left,root.right)

    def duichen(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val==right.val) and self.duichen(left.left,right.right) and self.duichen(left.right,right.left)




    def diedai(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 用一个队列来保存待检查的点
        if not root:
            return True

        queue = []
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
            


