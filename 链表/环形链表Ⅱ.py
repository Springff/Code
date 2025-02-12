# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

# 不允许修改 链表


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # a:非环段路程，b:从环的起点到相遇点，c:从相遇点到环的起点
        # 2（a+b）= a+k(b+c)+b
        # 化简得：a=(k-1)(b+c)+c
        # 所以一个从相遇点开始走，一个从起点开始走，会在环得起点处相遇

        if not head or not head.next or not head.next.next:
            return 

        fast = head.next.next
        slow = head.next

        while fast and fast.next and fast!=slow:
            fast = fast.next.next
            slow = slow.next
        if not fast or not fast.next:
            return
        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return fast
    

    def Haxizidian(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 保存每个链表元素，看看是否在哈希字典中
        dit = {}
        p = head
        while p:
            if p in dit:
                return p
            dit[p] = True
            p = p.next
        
        return