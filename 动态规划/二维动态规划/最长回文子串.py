# 给你一个字符串 s，找到 s 中最长的 回文 子串。

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 可能是偶数回文串或者奇数回文
        
        if len(s)<1:
            return ''
        star,end = 0,0
        ans = 0
        for i in range(len(s)):
            len1 = self.expand(s,i,i)
            len2 = self.expand(s,i,i+1)
            max_len = max(len1,len2)
            if ans<max_len:
                ans = max_len
                star = i-(max_len-1)//2 ###关键一步
                end = i+max_len//2
        return s[star:end+1]
            
    def expand(self,s,left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
           
        return right-left-1
        