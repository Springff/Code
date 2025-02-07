# 单行输入
import sys
# 将字符串转换为列表
a = sys.stdin.readline().strip().split(',')
# 将列表中的字符串转换为整数
a = list(map(int,a))

print(a)
print(type(a))



# 多行输入
data = []
while True:
    # 多行输入不要直接split，否则会报错，最后一行没有逗号
    line = sys.stdin.readline().strip()
    if line == '':
        break
    line = list(map(int,line.split(',')))
    data.append(line)
    
# print(data)
# print(type(data))
# print(type(data[0]))




# 简易输入

a = input()
a = list(map(int,a.split(',')))

data = []
while True:
    line = input()
    if not line:
        break
    line = list(map(int,line.split(',')))
    data.append(line)

print(data)
    
