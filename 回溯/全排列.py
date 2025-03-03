# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

class Solution(object):
  def permute(self, nums):
      """
      :type nums: List[int]
      :rtype: List[List[int]]
      """
      # 使用递归的思想，每次排一个位置上的数
      self.result = []
      self.backtrack(0,nums)
      return self.result


  def backtrack(self,star,nums):
      if star == len(nums):
          self.result.append(nums[:])
          ## nums是复制引用，nums[:]是重新复制一遍
          return
      for i in range(star,len(nums)):
          nums[i], nums[star] = nums[star], nums[i]
          self.backtrack(star+1,nums)
          nums[star], nums[i] = nums[i], nums[star]




