# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 新建一个节点作为前置头节点，向后遍历，对于每一个新节点将其插入到合适的位置

        out = ListNode()
        out.next = None
        p = head
        
        while p:
            next_node = p.next
            q = out
            while q.next and p.val>q.next.val:
                q = q.next
            
            p.next = q.next
            q.next = p
            p = next_node
            
        return out.next
    
    def digui_sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 找到链表的中点，递归寻找排序两段链表
        # 融合链表
        
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.digui_sortList(head)
        right = self.digui_sortList(mid)
        return self.merge(left,right)

    def merge(self,head1, head2):
        # 合并两个有序链表
        p1 = head1
        p2 = head2
        ans = ListNode()
        q = ans
        while p1 and p2:
            if p1.val<p2.val:
                q.next = p1
                q = q.next
                p1 = p1.next
            else:
                q.next = p2
                q = q.next
                p2 = p2.next
            
        if p1:
            q.next = p1
            
        if p2:
            q.next = p2

        
        return ans.next



head = ListNode()
p = head
while True:
    a = input()
    if a=='':
        break
    a = ListNode(int(a))
    p.next = a
    p = p.next
head = head.next
solution = Solution()
ans = solution.sortList(head)
while ans:
    print(ans.val)
    ans = ans.next