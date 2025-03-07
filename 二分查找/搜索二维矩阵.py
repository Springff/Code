# 给你一个满足下述两条属性的 m x n 整数矩阵：

# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
class Solution():
    def SearchMatrix(self,matrix,target):
        # 两层二分查找，先确定行再确定列
        row = self.SearchRow(matrix,target)
        if row==-1:
            return False
        nums = matrix[row]
        star = 0
        end = len(nums)-1
        while star<=end:
            mid = (star+end)//2
            if nums[mid]==target:
                return True
            if nums[mid]<target:
                star = mid+1
            else:
                end = mid-1
        return False
    
    def SearchRow(self,matrix,target):
        row = len(matrix)
        col = len(matrix[0])
        if target<matrix[0][0] or target>matrix[row-1][col-1]:
            return -1
        star = 0
        end = row-1
        while star<=end:
            mid = (star+end)//2
            if matrix[mid][0]==target:
                return mid
            if matrix[mid][0]<target:
                star = mid+1
            else:
                end = mid-1
        return end
    
matrix = [[1]]
target = 1
solution = Solution()
ans = solution.SearchMatrix(matrix, target)
print(ans)