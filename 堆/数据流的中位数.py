# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。

# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:

# MedianFinder() 初始化 MedianFinder 对象。

# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。

# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。

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


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
