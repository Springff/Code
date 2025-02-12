# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

# 请你将两个数相加，并以相同形式返回一个表示和的链表。

# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 逐位加和，超十进一
        ans = ListNode()
        p = ans
        label = False
        while l1 and l2:
            if label:
                if l1.val+l2.val>8:
                    q = ListNode(l1.val+l2.val-9)
                    p.next = q
                    p = p.next
                    label = True
                else:
                    q = ListNode(l1.val+l2.val+1)
                    p.next = q
                    p = p.next
                    label = False
            else:
                if l1.val+l2.val>9:
                    q = ListNode(l1.val+l2.val-10)
                    p.next = q
                    p = p.next
                    label = True
                else:
                    q = ListNode(l1.val+l2.val)
                    p.next = q
                    p = p.next
                    label = False
            l1 = l1.next
            l2 = l2.next
        if not label:    
            while l1:
                p.next = l1
                l1 = l1.next
                p = p.next 
            while l2:
                p.next = l2
                l2 = l2.next
                p = p.next
        else:
            while l1:
                if label:
                    if l1.val>8:
                        p.next = l1
                        p = p.next
                        p.val = 0
                        l1 = l1.next
                        label = True
                    else:
                        p.next = l1
                        p = p.next
                        p.val = l1.val+1
                        l1 = l1.next
                        label = False
                else: 
                    p.next = l1
                    l1 = l1.next
                    p = p.next 
                    label = False
            while l2:
                if label:
                    if l2.val>8:
                        p.next = l2
                        p = p.next
                        p.val = 0
                        l2 = l2.next
                        label = True
                    else:
                        p.next = l2
                        p = p.next
                        p.val = l2.val+1
                        l2 = l2.next
                        label = False
                else:
                    p.next = l2
                    l2 = l2.next
                    p = p.next
                    label = False
        if label:
            p.next = ListNode(1)
        ans = ans.next
        return ans
            
    def AddTwoNum(self, l1, l2):
        # 大量冗余代码，优化之
        label = 0
        ans = ListNode()
        p = ans
        while l1 or l2 or label:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + label
            label = total//10
            p.next = ListNode(total%10)
            p = p.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        ans = ans.next
        return ans
            
