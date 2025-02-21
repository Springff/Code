# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
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
