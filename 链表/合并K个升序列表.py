# 给你一个链表数组，每个链表都已经按升序排列。

# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # 建一个空链表，逐个合并每个链表
        out = ListNode()
        p = out
        for ln in lists:
            q = out
            while ln and q.next:
                if ln.val<q.next.val:
                    p = ln
                    ln = ln.next
                    p.next = q.next
                    q.next = p
                q = q.next
            if ln:
                q.next = ln
        return out.next
                
    def diedai(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # 分而治之，迭代合并，优化时间复杂度
        k = len(lists)
        if k==0:
            return None
        if k==1:
            return lists[0]
        n = int(k/2)
        left = self.mergeKLists(lists[:n]) 
        right = self.mergeKLists(lists[n:]) 

        return self.Merge(left,right)



    def Merge(self,head1,head2):
        out = ListNode()
        q = out
        while head1 and head2:
            if head1.val<head2.val:
                q.next = head1
                head1 = head1.next
            else:
                q.next = head2
                head2 = head2.next
            q = q.next
        if head1:
            q.next = head1
        if head2:
            q.next = head2
        return out.next
        
