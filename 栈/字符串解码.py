# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

 class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        current_char = ''
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = 10*current_num + int(char)
            elif char=='[':
                stack.append((current_char,current_num))
                current_num = 0
                current_char = ''
            elif char == ']':
                chars, num =stack.pop()
                current_char = chars+current_char*num
            else:
                current_char = current_char+char
        
        return current_char


