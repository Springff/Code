# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

# 有效 二叉搜索树定义如下：

# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # 递归验证父节点是否大于左小于右,仅看父节点是不行的，还是会有错误情况
        # 递归的检验当前节点是否符合大小要求
        return self.Vaild(root)


    def Vaild(self, root, low=float('-inf'), high=float('inf')):
        if root == None:
            return True
        if root.val>=high or root.val<=low:
            return False
        return self.Vaild(root.left,low,root.val) and self.Vaild(root.right,root.val,high) 
    
from collections import deque
def Build(s):
    if s=='':
        return TreeNode()
    i = 1
    root = TreeNode(s[0])
    queue = deque([root])
    while queue and i < len(s):
        q = queue.popleft()
        if s[i]!='null':
            newtree = TreeNode(int(s[i]))
            q.left = newtree
            queue.append(newtree)
        i+=1
        if i<len(s) and s[i]!='null':
            newtree = TreeNode(int(s[i]))
            q.right = newtree
            queue.append(newtree)
        i+=1
    return root

def LevelOrder(root):
    result = []

    def Level(root,level):
        if not root:
            return 
        if len(result)==level:
            result.append([])
        result[level].append(root.val)
        Level(root.left,level+1)
        Level(root.right,level+1)
    Level(root,0)
    return result

s = input().split(',')
root = Build(s)
ans = LevelOrder(root)
print(ans)