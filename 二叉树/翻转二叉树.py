# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        return self.reverse(root)
    
    def reverse(self, root):
        if root == None:
            return
        cache = root.left
        root.left = self.reverse(root.right)
        root.right = self.reverse(cache)
        return root
    

def buildTree(tree):
    root  = TreeNode(tree[0])
    stack = []
    stack.append(root)
    for i in range(len(tree)):
        stack.
        if tree[i] != None:
            node = TreeNode(tree[i])