# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits)==0:
            return []
        self.dic = {
            '2':['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
            }
        self.ans = []
        self.back(0,[],digits)
        return self.ans
    
    def back(self,index,current_s,digits):
        if index==len(digits):
            self.ans.append("".join(current_s))
            return
        letters = self.dic[digits[index]]
        for letter in letters:
            current_s.append(letter)
            self.back(index+1,current_s,digits)
            current_s.pop()
        
