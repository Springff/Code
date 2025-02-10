# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 从右上角或者左下角开始遍历，当找到目标值或者索引超出合理范围，遍历结束
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while 0<=i<=m-1 and 0<=j<=n-1:
            if matrix[i][j] == target:
                return True 
            if matrix[i][j] < target:
                i+=1
            else:
                j-=1
        return False

matrix = []
while True:
    a = input()
    if a=='':
        break
    a = list(map(int,a.split(',')))
    matrix.append()

solution = Solution()
ans = solution.searchMatrix(matrix)
print(ans)