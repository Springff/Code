# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

# 0 <= j <= nums[i] 
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 每次选择上限最高的选择
        
        if len(nums)==1:
            return 0
        i = 0
        largest = 0
        jump = 0

        while i<len(nums):
            for j in range(i,largest+1):
                if nums[j]+j>largest:
                    largest = nums[j]+j
                    i = j
                if largest>=len(nums)-1:
                    return jump+1
            jump+=1
      

