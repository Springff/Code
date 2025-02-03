# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

class Solution():
    def Merge(self, intervals):
        # 先对intervals中区间按左区间进行排序，逐个检查是否可以合并

        output = []
        ################################
        intervals.sort(key=lambda x:x[0])
        ##################################
        inter = intervals[0]

        for i in range(1,len(intervals)):
            if inter[0]<=intervals[i][0]<=inter[1]:
                inter[1] = max(inter[1],intervals[i][1])
            else:
                output.append(inter)
                inter = intervals[i]
        if inter not in output:
            output.append(inter)
        return output

intervals = []
while True:
    a = input()
    if a=="":
        break
    a = list(map(int,a.split(',')))
    intervals.append(a)

solution = Solution()
ans = solution.Merge(intervals)
print(ans)
