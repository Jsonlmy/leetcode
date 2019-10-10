'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

链接：https://leetcode-cn.com/problems/minimum-path-sum
'''
class Solution:
    def minPathSum(self, grid: list) -> int:
        '''
        解法1：动态规划。
        F(i,j) = v(i,j) + min(F(i-1, j), F(i, j-1))
        '''
        res = [sum(grid[0][:i+1]) for i in range(len(grid[0]))] + [float('inf')]
        for row in grid[1:]:
            for i, v in enumerate(row):
                res[i] = v + min(res[i], res[i-1])
        return res[-2]

if __name__ == "__main__":
    grid = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    res = Solution().minPathSum(grid)
    print(res)