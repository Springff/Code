# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 暴力求解，将链表内容逐个存储在哈希字典中，遍历完再逐个输出。
        dit = {}
        length = 0
        p = head
        if p == None:
            return None
        while p:
            dit[length] = p.val
            p = p.next
            length += 1
        length = length-1
        q = ListNode()
        q.val = dit[length]
        ans = q
        for i in range(length,0,-1):
            q.next = ListNode(dit[i-1])
            q = q.next
        
        return ans
    def diedai(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 迭代法，将节点从链表上逐个解下来，后序建立新的链表
        
        pre = None
        cur = head

        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
    
Input = ListNode()
q = Input
while True:
    a = input()
    if a=='':
        break
    
    p = ListNode(a)
    p.next = None
    q.next = p
    q = q.next

if Input.next:
    Input = Input.next
else:
    Input = None

solution = Solution()
ans = solution.diedai(Input)

while ans:
    print(ans.val)
    ans = ans.next
