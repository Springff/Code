# 给你二叉树的根结点 root ，请你将它展开为一个单链表：

# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 先序遍历获得遍历属性，再新建tree
        if not root:
            return 
        order = []
        self.Preorder(root,order)
        out = order[0]
        q = out
        for i in range(1,len(order)):
            q.left = None
            q.right = order[i]
            q = q.right
        return out


    def Preorder(self,root,order):
        if root==None:
            return
        order.append(root)
        self.Preorder(root.left,order)
        self.Preorder(root.right,order)
