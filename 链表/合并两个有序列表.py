# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


# Definition for singly-linked list.
class LinkNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 边比较大小边合并
        pa = list1
        pb = list2
        if not pa:
            return pb
        if not pb:
            return pa
        if pa.val<pb.val:
            ans = pa
            pa = pa.next
        else:
            ans = pb
            pb = pb.next
        q = ans
        while pa and pb:
            if pa.val<pb.val:
                q.next = pa
                pa = pa.next
                q = q.next
            else:
                q.next = pb
                pb = pb.next
                q = q.next
        if pa:
            while pa:
                q.next = pa
                pa = pa.next
                q = q.next
        if pb:
            while pb:
                q.next = pb
                pb = pb.next
                q = q.next

        return ans
    
list1 = LinkNode()
list2 = LinkNode()

p = list1
while True:
    a = input("输入第一个有序列表：")
    if a=='':
        break
    a = LinkNode(int(a))
    p.next = a
    p = p.next

if not list1.next:
    list1 = None
else:
    list1 = list1.next


p = list2
while True:
    a = input("输入第二个有序列表：")
    if a=='':
        break
    a = LinkNode(int(a))
    p.next = a
    p = p.next

if not list2.next:
    list2 = None
else:
    list2 = list2.next

solution = Solution()
ans = solution.mergeTwoLists(list1,list2)

while ans:
    print(ans.val)
    ans = ans.next