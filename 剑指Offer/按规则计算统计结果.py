# 为了深入了解这些生物群体的生态特征，你们进行了大量的实地观察和数据采集。数组 arrayA 记录了各个生物群体数量数据，其中 arrayA[i] 表示第 i 个生物群体的数量。请返回一个数组 arrayB，该数组为基于数组 arrayA 中的数据计算得出的结果，其中 arrayB[i] 表示将第 i 个生物群体的数量从总体中排除后的其他数量的乘积。
class Solution(object):
    def statisticalResult(self, arrayA):
        """
        :type arrayA: List[int]
        :rtype: List[int]
        """
        # 考虑特殊情况！！！
        total = 1
        count = 0
        for i in arrayA:
            if i==0:
                pass
            else:
                total*=i
                count+=1
        ans = []
        if count==len(arrayA):
            ans = []
            for i in arrayA:
                ans.append(total/i)
            return ans
        elif count==len(arrayA)-1:
            ans = [0]*len(arrayA)
            for i in range(len(arrayA)):
                if arrayA[i]==0:
                    ans[i] = total
            return ans
        else:
            return [0]*len(arrayA)
