# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。

# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 递归尝试所有组合，选择是否是否使用当前数字
        def backtrack(star,remain):
            if remain==0:
                output.append(path[:])
            for i in range(star,len(candidates)):
                if candidates[i]>remain:
                    continue
                path.append(candidates[i])
                backtrack(i,remain-candidates[i])
                path.pop()


        path = []
        output = []
        backtrack(0,target)
        return output
    
candidates = input('无重复整数数组')
candidates = list(map(int,candidates.split(',')))
solution = Solution()
ans = solution.combinationSum(candidates,8)
print(ans)
