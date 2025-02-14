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