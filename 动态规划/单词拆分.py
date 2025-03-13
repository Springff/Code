# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[float('inf')]*(len(s)+1)
        for i in range(1,len(s)+1):
            for word in wordDict:
                if i==len(word) and word==s[:i]:
                    dp[i]=1
                if i>len(word) and word==s[i-len(word):i]:
                    dp[i]=min(dp[i-len(word)],dp[i])
        if dp[-1]==1:
            return True
        return False
