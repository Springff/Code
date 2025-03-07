# 整数数组 nums 按升序排列，数组中的值 互不相同 。

# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 先判断哪边有序再来判断移动边界
        ##注意判断条件很容易踩坑
        star = 0
        end = len(nums)-1
        while star<=end:
            mid = (star+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[end]:
                if nums[mid]<target<=nums[end]:
                    star = mid+1
                else:
                    end = mid-1
            else:
                if nums[star]<=target<nums[mid]:
                    end = mid-1
                else:
                    star = mid+1
        return -1
