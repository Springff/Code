# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 旋转矩阵相当于将matrix[i][j]变为matrix[j][n-1-i]
        # 等于先转置再调整每行的顺序

        n = len(matrix)

        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] 
        
        for i in range(n):
            for j in range(int(n/2)):
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
        
        return
    
import sys
matrix = []

while True:
    a = sys.stdin.readline().strip()
    if a=='':
        break
    a = list(map(int,a.split(',')))
    matrix.append(a)
solution = Solution()
solution.rotate(matrix)
print(matrix)