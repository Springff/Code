# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup1(self, head, k) :
        # 首先判断是否有k个节点可以交换
        # 采用头插法进行翻转
        # 预先建一个空节点就不用注意第一次是否需要翻转的问题了
        def hasKnode(head,k):
            p = head
            for i in range(k):
                if p==None:
                    return False
                p = p.next
            return True

        def reverse(head,k):
            p = head
            ans = ListNode()
            ans.next = head
            for i in range(k):
                q = p
                p = p.next
                q.next = ans.next
                ans.next = q
            return ans.next,p
            
        out = ListNode()
        out.next = head
        p = head
        pre = out
        while p:
            if hasKnode(p,k):
                star,end = reverse(p,k)
                pre.next = star
                p = end
                for i in range(k):
                    pre = pre.next
            else:
                return out.next
        return out.next
    
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # 双指针，第一个指针先走k步，来判断是否翻转

        out = ListNode()
        out.next = head
        fast,slow = out,out
        while fast.next:
            for _ in range(k):
                if not fast.next: 
                    return out.next
                fast = fast.next
            next = fast.next
            pre,last = self.remove(slow.next,fast)
            slow.next = pre
            last.next = next
            fast,slow = last,last
        return out.next


    

    def remove(self,head1,head2):
        # 输入第一个和最后一个节点，翻转后返回第一个和最后一个节点
        out = ListNode()
        last = head1
        q = head1
        prev = head2.next ###注意注意注意
        while q!=prev:
            p = q
            q = q.next 
            p.next = out.next
            out.next = p
        
        return out.next,head1



solution = Solution()
list = [1,2,3,4,5]
head = ListNode()
q = head
for i in range(len(list)):
    p = ListNode(list[i])
    q.next = p
    q = p
head = head.next
k = 2
ans  = solution.reverseKGroup(head,k)
while ans:
    print(ans.val)
    ans = ans.next