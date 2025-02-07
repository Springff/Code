# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

# 题目数据保证数组nums之中任意元素的全部前缀元素和后缀的乘积都在32位整数范围内。

# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 计算一个前缀积数组和一个后缀积数组，每次需要的值就是前后积之积

        prefix_products = []
        prefix_products.append(1)
        for i in range(1,len(nums)):
            prefix_products.append(prefix_products[i-1]*nums[i-1])
        
        suffix_products = []
        suffix_products.append(1)
        for i in range(len(nums)-2,-1,-1):
            suffix_products.append(suffix_products[-1]*nums[i+1])
        
        output = []
        for i in range(len(nums)):
            output.append(prefix_products[i]*suffix_products[-i-1])
        return output
        

nums = input()
nums = list(map(int,nums.split(',')))
solution = Solution()
ans = solution.productExceptSelf(nums)
print(ans)