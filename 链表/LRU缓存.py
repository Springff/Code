# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

class DLinkNode(): # 双向链表
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.cache = {}


        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 如果有值返回值，将节点移动到头节点，没值返回-1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove_to_head(node)
        return node.value



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_to_head(node)
        else:
            if self.size < self.capacity:
                node = DLinkNode(key,value)
                self.add_head(node)
                self.cache[key] = node
                self.size += 1
            else:
                del self.cache[self.tail.pre.key]# 注意这两步的顺序，调整后会有什么问题
                self.remove(self.tail.pre)

                # 也可以这样
                # remove_node = self.tail.pre
                # self.remove(remove_node)
                # del self.cache[remove_node.key]

                node = DLinkNode(key,value)
                self.add_head(node)
                self.cache[key] = node
        

    def remove_to_head(self,node):
        self.remove(node)
        self.add_head(node)

    def add_head(self,node):
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node
    
    def remove(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre
        


capacity = input('请输入缓存容量：')
obj = LRUCache(int(capacity))
key = input('请输入key：')

param_1 = obj.get(key)
print(param_1)
value = input('请输入value：')
obj.put(key,value)
param_1 = obj.get(key)
print(param_1)