# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。

class Solution():
    def Vaild(self,s):
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack:
                    return False
                a = stack.pop()
                if a!='(':
                    return False
            elif i == '}':
                if not stack:
                    return False
                a = stack.pop()
                if a!='{':
                    return False
            elif i == ']':
                if not stack:
                    return False
                a = stack.pop()
                if a!='[':
                    return False
        if not stack:
            return True
        return False
            
