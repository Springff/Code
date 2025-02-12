# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head==None or head.next==None :
            return head 
        mid = head
        last = head.next
        mid.next = last.next
        last.next = mid
        head = last

        pre = head.next
        mid = pre.next
        if mid==None or mid.next==None:
            return head
        last = pre.next.next
        
        while last:
            pre.next = last
            mid.next = last.next
            last.next = mid

            pre = pre.next.next
            mid = pre.next
            if mid==None or mid.next==None:
                return head
            last = pre.next.next
        return head

