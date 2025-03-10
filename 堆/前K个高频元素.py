# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 维护一个大小为k的最小堆
        # 堆中保存的是元素的值，堆的顺序是按元素的频录排的
        dic = {}
        for num in nums:
            dic[num] = dic.get(num,0)+1
        
        min_heap = []
        for i in dic:
            self.Build_D(min_heap,k,dic,i)
        return min_heap

    def Build_D(self,heap,k,dic,num):
        if len(heap)==k and dic[num]<=dic[heap[0]]:
            return
        if len(heap)==k:
            heap[0]=num
            self.adjust(heap,0,dic)
        else:
            heap.append(num)
            index = len(heap)-1
            while index>0:
                parent = (index-1)//2
                if dic[heap[parent]]<dic[heap[index]]:
                    break
                heap[parent],heap[index] = heap[index],heap[parent]
                index = parent


    def adjust(self,heap,index,dic):
        left = 2*index+1
        right = left+1
        smallest = index
        if left<len(heap) and dic[heap[smallest]]>dic[heap[left]]:
            smallest = left
        if right<len(heap) and dic[heap[smallest]]>dic[heap[right]]:
            smallest = right
        if smallest!=index:
            heap[index],heap[smallest]=heap[smallest],heap[index]
            self.adjust(heap,smallest,dic)    
