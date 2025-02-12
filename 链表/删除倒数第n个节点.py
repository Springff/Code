# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

# Definition for singly-linked list.
class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # 指针1先走n步，指针2再开始走，指针1为空删除指针2
        p1 = head
        p2 = head
        pre = head
        for i in range(n):
            p1 = p1.next
        if not p1:
            return head.next
        p1 = p1.next
        p2 = p2.next
        while p1:
            p1 = p1.next
            p2 = p2.next
            pre = pre.next
        pre.next = p2.next
        del(p2)
        return head

head = LinkNode()
n = input('输入n:')
n = int(n)

p = head
while True:
    a = input('输入链表节点：')
    if a=='':
        break
    a = LinkNode(int(a))
    p.next = a
    p = p.next

head = head.next

solution = Solution()
ans = solution.removeNthFromEnd(head, n)
while ans:
    print(ans.val)
    ans = ans.next