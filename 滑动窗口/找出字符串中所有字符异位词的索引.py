# 给定两个字符串 s 和 p，找到 s 中所有 p 的异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

# 经验：维护一个窗口，每次只关注窗口变动的部分，可以减少时间复杂度。


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 遍历s，检查s中每len(p)个子串是否可以构成p，若可以则输出索引
        ans = []
        if len(s) < len(p):
            return ans
        p_count = {}
        for i in p:
            p_count[i] = p_count.get(i,0)+1
        
        for i in range(len(s)-len(p)+1):
            char_map = {}
            j = i
            max = i+len(p)
            # 注意这里的判断条件，j < max的条件要放在前面，否则会出现数组越界
            while  j < max and s[j] in p:
                char_map[s[j]] = char_map.get(s[j],0)+1
                j+=1
            if char_map==p_count:
                ans.append(i)
        return ans
    def Huadongchuangkou(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 维护一个窗口，检查窗口内的字符串是否与p匹配
        # 每次滑动一个步长，只更新新增和删除的那个字符，再次检查是否匹配，避免重新遍历窗口。

        if len(s) < len(p):
            return []
        ans = []
        p_count = {}
        windows = {}
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i],0)+1
            windows[s[i]] = windows.get(s[i],0)+1

        for i in range(len(s)-len(p)+1):
            if i==0:
                if windows == p_count:
                    ans.append(i)
            else:
                windows[s[i-1]] = windows[s[i-1]]-1
                if windows[s[i - 1]] == 0:
                   del windows[s[i - 1]]
                windows[s[i+len(p)-1]] = windows.get(s[i+len(p)-1],0)+1
                if windows == p_count:
                    ans.append(i)
        return ans


s = input()
p = input()
solution = Solution()
answer = solution.findAnagrams(s,p)
print(answer)