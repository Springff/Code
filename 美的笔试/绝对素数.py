# 判断一个素数，逆序排列后是否仍是素数
import math
class Solution():
    def isAPrime(self,x):
        char = str(x)
        if x<=1:
            return False
        x_n = 0
        for i in range(len(char)-1,-1,-1):
            x_n=int(char[i])+x_n*10
        if x_n==2:
            return True
        if x_n%2==0:
            return False
        for i in range(3,int(math.sqrt(x_n))+1,2):
            if x_n%i==0:
                return False
        return True
    

s = Solution()
a = 61
ans = s.isAPrime(a)
print(ans)

