# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # 新建一个队列，保存要遍历的节点，维护一个k，表示该层要遍历的节点
        if not root:
            return []
        out = [root.val]
        ans = []
        queue = []
        k = 0
        ans.append(out)
        if root.left:
            queue.append(root.left)
            k += 1
        if root.right:
            queue.append(root.right)
            k += 1
        while queue:
            a = k
            k = 0
            out = []
            while a > 0:
                q = queue.pop(0)
                out.append(q.val)
                if q.left:
                    queue.append(q.left)
                    k += 1
                if q.right:
                    queue.append(q.right)
                    k += 1
                a-=1
            ans.append(out)
        return ans
    
    # 更高效的队列
    from collections import deque

    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        # 新建一个队列，保存要遍历的节点，维护一个k，表示该层要遍历的节点
        # 不用维护k，直径用len（queue）
        if not root:
            return []
        
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            out = []
            a = len(queue)
            while a > 0:
                q = queue.popleft()
                out.append(q.val)
                if q.left:
                    queue.append(q.left)  
                if q.right:
                    queue.append(q.right)  
                a-=1
            ans.append(out)
        return ans


