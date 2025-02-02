# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。

# 经验： 需要一个标记和字典来检查当前窗口是否符合要求

class Solution():
    def MinWindow(self,s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 需要一个标记来标识现在的窗口中是否包含所有需要的字符
        # 一个哈希字典和一个值来作为标记，哈希字典存储t中字符串是否出现，一个值判定是否所有字符都已出现

        if len(s)<len(t) or len(s)==0:
            return ""
        label = len(t)
        dit = {}
        star = 0
        min_len = float('inf')
        for i in t:
            dit[i] = dit.get(i,0)+1
        
        left = 0
        for right,char in enumerate(s):
            if char in dit:
                if dit[char]>0:#神来之笔
                    label-=1
                dit[char]-=1
            while label==0:
                if min_len>right-left+1:
                    min_len = right-left+1
                    star = left
                if s[left] in dit:
                    dit[s[left]]+=1
                    if dit[s[left]]>0:
                        label+=1
                left +=1
        
        return s[star:star+min_len] if min_len!=float('inf') else ""



import sys
s = input()
t = sys.stdin.readline().strip()

solution = Solution()
ans = solution.MinWindow(s,t)
print(ans)