# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

# 请必须使用时间复杂度为 O(log n) 的算法。
class Solution():
    def SearchInsert(self,nums,target):
        if not nums:
            nums.append(target)
            return 0
        star = 0
        end = len(nums)-1
        while star<=end:
            mid = (star+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                star = mid+1
            else:
                end = mid-1
        return star
    

nums = [1,3,5,6]
target = 7
sol = Solution()
ans = sol.SearchInsert(nums,target)
print(ans)