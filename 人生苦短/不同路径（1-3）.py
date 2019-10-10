class Solution:
    '''
    不同路径

    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

    问总共有多少条不同的路径？
    
    网格中的障碍物和空位置分别用 1 和 0 来表示。

    说明：m 和 n 的值均不超过 100。

    示例 1:

    输入:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    输出: 2
    解释:
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右

    图片见链接
    链接：https://leetcode-cn.com/problems/unique-paths-ii
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        解法1：排列组合，从左上角走到右下角，要么下移，要么右移，
        所以步数是固定的，就变成于从a步（总步数）中选择b步下移或右移的问题
        '''
        # return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
        '''
        解法2：杨辉三角，设左上角为（0，0），例如要走到（3，3），
        只有两种走法，（3，2）或（2，3），所以必须要先算出移动到这两个位置的路径然后相加
        '''
        # def inner(i, j):
        #     if i == 1 or j == 1: return i + j
        #     return 2 * inner(i-1, j) if i == j else inner(i-1, j) + inner(i, j-1)
        # return 1 if m == 1 or n == 1 else inner(m-1, n-1)
        '''
        以下改进方法通过字典避免重复计算
        '''
        pos = {}
        def inner(i, j):
            if i == 1 or j == 1: return i + j
            if (i-1, j) in pos or (j, i-1) in pos:
                a = pos[i-1, j]
            else:
                a = inner(i-1, j)
                pos[i-1, j] = pos[j, i-1] = a
            if (i, j-1) in pos or (j-1, i) in pos:
                b = pos[i, j-1]
            else:
                b = inner(i, j-1)
                pos[i, j-1] = pos[j-1, i]= b
            return a + b
        return 1 if m == 1 or n == 1 else inner(m-1, n-1)

    '''
    不同路径 II

    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

    机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

    现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

    网格中的障碍物和空位置分别用 1 和 0 来表示。

    说明：m 和 n 的值均不超过 100。

    示例 1:

    输入:
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    输出: 2
    解释:
    3x3 网格的正中间有一个障碍物。
    从左上角到右下角一共有 2 条不同的路径：
    1. 向右 -> 向右 -> 向下 -> 向下
    2. 向下 -> 向下 -> 向右 -> 向右

    链接：https://leetcode-cn.com/problems/unique-paths-ii
    '''
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        '''
        解法1：动态规划，可以到达一个方格的路径数等于到达它左边方格和上边方格路径数之和，
        但是当该方格上有障碍物时，到达的路径数等于0
        '''
        row_count, col_count = len(obstacleGrid), len(obstacleGrid[0])
        res = [1] + [0] * col_count     # 给左边加一个边界
        for i in range(row_count):
            for j in range(col_count):
                res[j] = 0 if obstacleGrid[i][j] else res[j] + res[j-1]
        return res[-2]

    '''
    不同路径 III

    在二维网格 grid 上，有 4 种类型的方格：

    1 表示起始方格。且只有一个起始方格。
    2 表示结束方格，且只有一个结束方格。
    0 表示我们可以走过的空方格。
    -1 表示我们无法跨越的障碍。
    返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目，每一个无障碍方格都要通过一次。

     

    示例 1：

    输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    输出：2
    解释：我们有以下两条路径：
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
    示例 2：

    输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    输出：4
    解释：我们有以下四条路径： 
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
    示例 3：

    输入：[[0,1],[2,0]]
    输出：0
    解释：
    没有一条路能完全穿过每一个空的方格一次。
    请注意，起始和结束方格可以位于网格中的任意位置。
     

    提示：

    1 <= grid.length * grid[0].length <= 20

    链接：https://leetcode-cn.com/problems/unique-paths-iii
    '''
    def uniquePathsIII(self, grid: list) -> int:
        '''
        解法1：回溯，O(4^(r*c))，递归尝试每一个格子的四个方向，
        每经过一个值为0的格子就将该格子设置为-1，防止重复递归，返回时恢复
        '''
        self.grid = grid
        self.row_count = len(grid)
        self.col_count = len(grid[0])
        self.zero_count = 0
        start_row, start_col = 0, 0
        for i in range(self.row_count):
            for j in range(self.col_count):
                if grid[i][j] == 0: self.zero_count += 1
                elif grid[i][j] == 1: start_row, start_col = i, j

        return self.search(start_row-1, start_col) + self.search(start_row+1, start_col) +\
               self.search(start_row, start_col-1) + self.search(start_row, start_col+1)
        '''
        解法2：动态规划，O(r*c*2^(r*c))
        '''
        # from functools import lru_cache

        # R, C = len(grid), len(grid[0])

        # def code(r, c): return 1 << (r * C + c)     # 将方格坐标编码

        # def neighbors(r, c):        # 生成所有可经过相邻方格的坐标
        #     for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
        #         if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] % 2 == 0:
        #             yield nr, nc

        # grid_code = 0
        # for r, row in enumerate(grid):
        #     for c, val in enumerate(row):
        #         if val % 2 == 0: grid_code |= code(r, c)   # 将所有可经过方格（包含终点）坐标编码到一个二进制数中
        #         if val == 1: sr, sc = r, c  # 记录起点
        #         if val == 2: tr, tc = r, c  # 记录终点

        # @lru_cache(None)
        # def dp(r, c, codes):    # dp[r, c, d]为从(r, c)出发，地图编码为d时，好路径的数量
        #     if r == tr and c == tc: return codes == 0

        #     path_count = 0
        #     for nr, nc in neighbors(r, c):
        #         if codes & code(nr, nc):
        #             path_count += dp(nr, nc, codes ^ code(nr, nc))
        #     return path_count

        # return dp(sr, sc, grid_code)

    def search(self, r: int, c: int) -> int:
        if r < 0 or r == self.row_count or c < 0 or c == self.col_count: return 0       # 越界
        value = self.grid[r][c]
        if value == 1 or value == -1: return 0          # 或遇到障碍（包括起点）
        if value == 2: return self.zero_count == 0      # 遇到终点时检查是否还有可以经过的格子未经过（0的数量）

        self.grid[r][c], self.zero_count = -1, self.zero_count - 1
        res = self.search(r-1, c) + self.search(r+1, c) + self.search(r, c-1) + self.search(r, c+1)
        self.grid[r][c], self.zero_count = 0, self.zero_count + 1
        return res


if __name__ == "__main__":
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    res = Solution().uniquePathsIII(grid)
    print(res)