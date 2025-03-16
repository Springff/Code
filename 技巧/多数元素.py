# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 投票算法，既然你是多数元素，你的票数一定比别人高

        candidate = None
        count = 0
        for num in nums:
            if count==0:
                candidate = num
                count = 1
            elif candidate==num:
                count+=1
            else:
                count-=1

        return candidate
