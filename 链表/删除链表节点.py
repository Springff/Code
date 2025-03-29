# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

# 返回删除后的链表的头节点。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # 注意边界条件的判断
        p = head
        if head.val == val:
            return head.next
        while p:
            if p.next.val==val:
                q = p.next
                p.next = p.next.next
                del q
                return head
            p = p.next
