# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。

# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。

# 返回一个表示每个字符串片段的长度的列表。



class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # 维护一个哈希表，保存每个字符出现的最远距离，遍历s进行分组
        h = {}
        for i in range(len(s)):
            h[s[i]] = i
           
        length = 0
        out = []
        temp = 0
        for i in range(len(s)):
            length+=1
            if temp < h[s[i]]:
                temp = h[s[i]]
            if i==temp:
                out.append(length)
                length=0


        return out
