# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
# 原地算法：在算法执行过程中，除了输入数据本身所占用的存储空间外，只使用常数级别的额外空间来完成计算任务的算法。

class Solution():
    def MatrixtoZero(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # 遍历一遍矩阵，纪录下0元素的位置在一个数组中，将坐标在数组中的元素全部置为0

        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)
        
        for i in range(len(matrix)):
            for j in cols:
                matrix[i][j]=0
        for i in rows:
            for j in range(len(matrix[0])):
                matrix[i][j]=0
        
        return 
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # 原地算法要求使用常数级的存储空间
        # 使用矩阵的第一行和第一列来标记哪些元素需要被置零，不再使用额外的存储空间
        # 首先记录第一行第一列是否需要置零
        # 接下来将需要置零的行和列的第一个值设为0，遍历一遍后置零

        row_zero = any(x==0 for x in matrix[0])
        col_zero = any(matrix[i][0]==0 for i in range(len(matrix)))
        for i in range(1,len(matrix)):# 从1开始，避免混淆第一个值是原本就是0还是被置0
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1,len(matrix)):# 从1开始，避免影响以后行列的判断
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        

        if row_zero:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        if col_zero:
            for i in range(len(matrix)):
                matrix[i][0]=0
        return
matrix = []
while True:
    a = input()
    if a == '':
        break
    a = list(map(int,a.split(',')))
    matrix.append(a)

solution = Solution()
solution.setZeroes(matrix)
print(matrix)
