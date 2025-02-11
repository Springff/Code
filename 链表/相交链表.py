# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 三种思路
        # 第一，A链表后接B链表，B后接A，遍历检查是否有交点
        # 第二，将长链表的初始节点先向后移动链表差值个单位，再逐个检查
        # 第三，将一个链表的每个节点加入哈希字典中，遍历另一个链表，检查是否有交点
        pa = headA
        pb = headB

        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        
        return pa


  
heada = LinkNode()
p = heada

while True:
    a = input('请输入链表A:')
    if a=='':
        break
    q = LinkNode(a)
    p.next = q
    p = p.next

if heada.next:
    heada = heada.next
else:
    heada = None


headb = LinkNode()
p = headb

while True:
    a = input('请输入链表B:')
    if a=='':
        break
    q = LinkNode(a)
    p.next = q
    p = p.next

if headb.next:
    headb = headb.next
else:
    headb = None


solution = Solution()
ans = solution.getIntersectionNode(heada,headb)
print(ans)
