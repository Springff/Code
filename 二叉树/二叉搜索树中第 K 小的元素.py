# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        # 中序遍历二叉树，输出第k个值
        queue = deque()
        q = root
        t = 0
        while queue or q:
            while q:
                queue.append(q)
                q = q.left
            ans = queue.pop()
            t = t+1
            if k==t:
                return ans.val
            q = ans.right


def LevelOrder(nums):
    if not nums:
        return None        
    queue = deque()
    root = TreeNode(nums[0])
    queue.append(root)
    k = 1
    while k < len(nums):
        q = queue.popleft()
        if nums[k]:
            t = TreeNode(nums[k])
            q.left = t
            queue.append(t)
        k += 1
        if k<len(nums) and nums[k]:
            t = TreeNode(nums[k])
            q.right = t
            queue.append(t)
        k += 1
    return root

nums =[]
while True:
    a = input()
    if a=='':
        nums.append(None)
    if a=='end':
        break
    nums.append(int(a))

root = LevelOrder(nums)
solution = Solution()
ans = solution.kthSmallest(root,3)
print(ans)