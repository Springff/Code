# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
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
        

solution = Solution()
s = input()
answer = solution.lengthOfLongestSubstring(s)
print(answer)