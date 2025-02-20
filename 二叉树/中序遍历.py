  # 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 递归输出
        out = []
        self.inorder(root,out)
        return out


    def inorder(self,root,out):
        if root == None:
            return 
        self.inorder(root.left,out)
        out.append(root.val)
        self.inorder(root.right,out)
        
  def diedai(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 迭代遍历，用栈来保存待遍历的节点

        stack = []
        out = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            out.append(curr.val)
            curr = curr.right
        return out
