# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# Definition for singly-linked list.
class LinkNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # 维护一个栈来检查，当前值与栈顶元素一样则弹出栈顶元素，否则入栈。
        # 错误原因：只能检查偶数类回文，不能检查奇数类回文
        # 解决办法：使用快慢指针
        
        if head==None or head.next==None:
            return True

        fast = head
        slow = head

        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        while slow:
            if slow.val != stack[-1]:
                return False
            slow = slow.next
            stack.pop()
        
        return True

import sys   
head = LinkNode()
p = head

while True:
    a = sys.stdin.readline().strip()
    if a=='':
        break
    q = LinkNode(a)
    p.next = q
    p = p.next

if head.next:
    head = head.next
else:
    head = None

solution = Solution()
ans = solution.isPalindrome(head)
print(ans)