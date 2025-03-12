# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:

# MedianFinder() 初始化 MedianFinder 对象。

# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。



####### 经验：堆的两个主要函数：建堆（删除堆顶元素）和插堆



class MedianFinder(object):

    def __init__(self):
        self.list = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        
        if not self.list or num>=self.list[-1]:
            self.list.append(num)
            return
        a=0  
        for i in range(len(self.list)):
            if num<=self.list[i]:
                a=i
                break
        self.list.append(num)
        
        for j in range(len(self.list)-1,a,-1):
            self.list[j]=self.list[j-1]
        self.list[a]=num

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.list)
        if length%2==0:
            return (self.list[length/2]+self.list[length/2-1])/2.0
        return self.list[length//2]




# 经验：堆的两个主要函数：建堆（删除堆顶元素）和插堆

class MedianFinder(object):
# 建两个堆，一个最大堆一个最小堆，来一个数字，先加入到最大堆，再将最大堆的第一个元素加入最小堆，如果两堆不平衡，再移动最小堆的元素；
    def __init__(self):
        self.mini_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.Insert_max(self.max_heap,num)
        
        self.Insert_mini(self.mini_heap,self.delete_max(self.max_heap))
        if len(self.mini_heap)>len(self.max_heap):
            self.Insert_max(self.max_heap,self.delete_mini(self.mini_heap))


    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.mini_heap)+len(self.max_heap)
        if length%2==0:
            return (self.mini_heap[0]+self.max_heap[0])/2.0
        return self.max_heap[0]

    def Insert_max(self,heap,num):
        heap.append(num)
        index = len(heap)-1
        while index>0:
            parent = (index-1)//2
            if heap[parent]>=heap[index]:
                break
            heap[parent],heap[index]=heap[index],heap[parent]
            index = parent
    def Insert_mini(self,heap,num):
        heap.append(num)
        index = len(heap)-1
        while index>0:
            parent = (index-1)//2
            if heap[parent]<=heap[index]:
                break
            heap[parent],heap[index]=heap[index],heap[parent]
            index = parent

    def delete_max(self,heap):
        a = heap[0]
        if len(heap)==1:
            del heap[0]
            return a
        heap[0],heap[-1] = heap[-1],heap[0]
        n = len(heap)-2
        self.Build_max(heap,0,n)
        del heap[-1]
        return a

    def Build_max(self,heap,i,n):
        left = 2*i+1
        right = left+1
        largest = i
        if left<=n and heap[left]>heap[largest]:
            largest = left
        if right<=n and heap[right]>heap[largest]:
            largest = right
        if largest!=i:
            heap[largest],heap[i] = heap[i],heap[largest]
            self.Build_max(heap,largest,n)

    def delete_mini(self,heap):
        a = heap[0]
        if len(heap)==1:
            del heap[0]
            return a
        heap[0],heap[-1] = heap[-1],heap[0]
        n = len(heap)-2
        self.Build_mini(heap,0,n)
        del heap[-1]
        return a

    def Build_mini(self,heap,i,n):
        left = 2*i+1
        right = left+1
        largest = i
        if left<=n and heap[left]<heap[largest]:
            largest = left
        if right<=n and heap[right]<heap[largest]:
            largest = right
        if largest!=i:
            heap[largest],heap[i] = heap[i],heap[largest]
            self.Build_mini(heap,largest,n)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
