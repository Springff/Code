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
    def flatten1(self, root):
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


    def flatten_digui(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        # 后序遍历二叉树，逐个处理每个节点，左节点加入到右边，左子树置空
        # 递归空间复杂度肯定不是O(1)了
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        temp = root.right
        root.right = root.left
        root.left = None
        p = root
        while p.right:
            p = p.right
        p.right = temp
        return root

    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """

        # 后序遍历二叉树，逐个处理每个节点，左节点加入到右边，左子树置空
        # 递归空间复杂度肯定不是O(1)了
        # 找当前节点左子树的最右节点，将右子树连接到左子树的最右节点
        # 将左子树变为右子树，左子树置空
        if not root:
            return 
        curr = root
        while curr:
            p = curr.left
            if not p:
                curr = curr.right
                continue
            while p.right:
                p = p.right
            p.right = curr.right
            curr.right = curr.left
            curr.left = None
            curr = curr.right
        
        return root
