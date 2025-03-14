给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 检查两种情况
        # （）：dp[i-1]+2
        # （。。。）：dp[i-dp[i-1]-2]+2+dp[i-1]
        if len(s)<2:
            return 0
        dp = [0]*(len(s))
        for i in range(1,len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i]=(dp[i-2] if i>=2 else 0)+2
                elif i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=dp[i-dp[i-1]-2 if i-dp[i-1]-2>=0 else 0]+2+dp[i-1]
        max_n=0
        for num in dp:
            if max_n<num:
                max_n=num
        return max_n
