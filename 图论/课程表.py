# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

from collections import deque, defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 计算每个节点的入度，入度为0即可修，修完对应节点入度减一，最终检查修完课程与选修课数是否一致
        if prerequisites==[]:
            return True
        queue = deque()
        graph = defaultdict(list) 
        count = [0]*numCourses

        for course,precourse in prerequisites:
            graph[precourse].append(course)
            count[course]+=1
        for i in range(numCourses):
            if count[i]==0:
                queue.append(i)
        num = 0
        while queue:
            course = queue.popleft()
            num += 1
            node = graph[course]
            for i in node:
                count[i]-=1
                if count[i]==0:
                    queue.append(i)
        
        return num==numCourses
