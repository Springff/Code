# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

# 不允许修改 链表

class Listnode():
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next 

def DetectCycle(head):
    # 快慢指针
    if not head or not head.next:
        return -1
    fast,slow = head,head

    while fast and fast.next!=None:
        fast = fast.next.next
        slow = slow.next
        if fast==slow:
            break
    if fast!=slow:
        return -1
    fast = head
    
    while fast!=slow:
        fast = fast.next
        slow = slow.next
        
    return slow
    
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

s = input().split(',')
s = list(map(int,s))
head = Listnode()
t = head
for num in s:
    p = Listnode(num)
    t.next = p
    t = t.next
head = head.next
k = int(input())
p = head
for i in range(k):
    p = p.next
t.next = p

ans = DetectCycle(head)
print(ans.val)