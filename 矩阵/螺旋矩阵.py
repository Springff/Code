# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 定义上，下，左，右四个边界，初始时上边界为0，下边界为m-1，左边界为0，右边界为n-1
        # 从左到右遍历元素，遍历完上边界加一，以此类推
        # 终止条件为上边界大于下边界或左边界大于右边界

        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1
        output = []

        while left<=right and top<=bottom:
            for j in range(left,right+1):
                output.append(matrix[top][j])
            top+=1
            for i in range(top,bottom+1):
                output.append(matrix[i][right])
            right-=1
            if top<=bottom:# while条件限制，前两次遍历肯定符合要求，仅需要检查最后两次是否合规
                for j in range(right,left-1,-1):
                    output.append(matrix[bottom][j])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    output.append(matrix[i][left])
                left+=1
        return output
            

            
matrix = []
while True:
    a = input()
    if a=='':
        break
    a = list(map(int,a.split(',')))
    matrix.append(a)

solution = Solution()
ans = solution.spiralOrder(matrix)
print(ans)