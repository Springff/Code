# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        # 双重递归，第一层递归遍历所有节点，第二层递归计算从当前节点开始的符合条件的路径
        if root==None:
            return 0
        count = self.Count(root,targetSum)
        count += self.pathSum(root.right,targetSum)
        count += self.pathSum(root.left,targetSum)
        return count
    def Count(self,root,targetSum):
        if not root:
            return 0
        count = 0
        if root.val == targetSum:
            count+=1
        count += self.Count(root.left,targetSum-root.val)
        count += self.Count(root.right,targetSum-root.val)
        return count
