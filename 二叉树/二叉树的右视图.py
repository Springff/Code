# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 层序遍历，输出每一层最右侧节点
        result = []
        self.Level(result,root,0)
        out = []
        for i in range(len(result)):
            out.append(result[i][-1])
        return out



    def Level(self,result,root,level):
        if not root:
            return 
        if len(result)==level:
            result.append([])
        result[level].append(root.val)
        self.Level(result,root.left,level+1)
        self.Level(result,root.right,level+1)
        
