# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 暴力破解，双层循环，第一层循环代表子数组的起始位置，第二层循环代表数组的终止位置
        counts = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i == j:
                    if nums[i]==k:
                        counts+=1
                else:
                    sum = 0
                    for num in range(i,j+1):
                        sum+=nums[num]
                    if sum==k:
                        counts+=1
        return counts
    
    def qianzhuihe(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 计算一个哈希表，内容是前缀和的出现次数，子数组和为k就等查找于前缀和-k的前缀和是否出现在哈希表中
        # 注意要边计算哈希表边检查，以防出现负数的情况

        map = {}
        counts = 0
        sum = 0

        for i in nums:
            sum += i
            if sum==k:## 这个判断是否有更好的选择，有，初始哈希表中，加入{0：1}即可，减少判断时间
                counts+=1
            if sum-k in map:
                counts+=map[sum-k]
            map[sum] = map.get(sum,0)+1
        
        return counts

nums = input().split(',')
k = int(input())
nums = list(map(int,nums))
solution = Solution()
answer = solution.subarraySum(nums,k)

print(answer)