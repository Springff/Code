# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。


# 经验：查找字符串位置可以用哈希表，时间复杂度更低
#       保存窗口索引而不是所有内容，可以节省空间

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 维护一个最大窗口和一个当前窗口
        # 检查当前字符，是否已经存在于窗口中，如果存在更新当前窗口；如果不存在添加字符到当前窗口，并判断是否需要更新最大窗口
        #输出最大窗口的长度

        longest_substring = []
        current_substring = []

        for i in s:
            if i in current_substring:
                index = current_substring.index(i)
                current_substring = current_substring[index + 1:]
                current_substring.append(i)
            else:
                current_substring.append(i)
                if len(current_substring)>len(longest_substring):
                    longest_substring = current_substring
        return len(longest_substring)
    
    def Huadongchuangkou(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 维护一个哈希表和窗口的索引
        # 检查当前字符是否出现在窗口中，若出现，则更新窗口；若不出现，则检查最大窗口长度
        #输出最大窗口的长度

        char_map = {}
        star = 0
        max_string = 0
        for end,char in enumerate(s):
            if char in char_map and star <= char_map[char]:
                star = char_map[char]+1
            else:
                max_string = max(max_string,end - star + 1)
            char_map[char] = end
        
        return max_string
        

solution = Solution()
s = input()
answer = solution.lengthOfLongestSubstring(s)
print(answer)