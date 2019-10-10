class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        '''
        解法1：生成入度表，广度优先遍历
        '''
        indegrees = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]

        for pre, nxt in prerequisites:
            indegrees[nxt] += 1
            adjacency[pre].append(nxt)

        q = [i for i, v in enumerate(indegrees) if v == 0]
        while q:
            for nxt in adjacency[q.pop()]:
                indegrees[nxt] -= 1
                if indegrees[nxt] == 0:
                    q.append(nxt)

        for v in indegrees:
            if v: return False
        return True


if __name__ == "__main__":
    print(Solution().canFinish(2, [[0,1],[1,0]]))