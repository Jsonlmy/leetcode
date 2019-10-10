class Solution:
    '''
    螺旋矩阵
    
    给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

    示例 1:

    输入:
    [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
    ]
    输出: [1,2,3,6,9,8,7,4,5]
    示例 2:

    输入:
    [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
    ]
    输出: [1,2,3,4,8,12,11,10,9,5,6,7]
    
    链接：https://leetcode-cn.com/problems/spiral-matrix
    '''
    def spiralOrder(self, matrix: list) -> list:
        '''
        解法1：每次取矩阵第一行，并将剩余部分旋转
        '''
        res = []
        while matrix:
            res.extend(matrix[0])
            matrix = [r for r in zip(*matrix[1:])][::-1]
        return res

    '''
    螺旋矩阵 II

    给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

    示例:

    输入: 3
    输出:
    [
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
    ]

    链接：https://leetcode-cn.com/problems/spiral-matrix-ii
    '''
    def generateMatrix(self, n: int) -> list:
        '''
        解法1：从中心倒序构造
        '''
        r, n = [[n**2]], n**2
        while n > 1: n, r = n - len(r), [[*range(n - len(r), n)]] + [*zip(*r[::-1])]
        return r
        '''
        解法2：设置4个边界，从外圈逐个遍历到最里层
        '''
        # ret, i, k = [[0 for i in range(n)] for i in range(n)], 1, n**2
        # l, r, t, b = 0, n, 1, n
        # x = y = 0
        # while i <= k:
        #     for x in range(l, r):
        #         ret[y][x] = i
        #         i += 1
        #     r -= 1

        #     for y in range(t, b):
        #         ret[y][x] = i
        #         i += 1
        #     b -= 1

        #     for x in range(r-1, l-1, -1):
        #         ret[y][x] = i
        #         i += 1
        #     l += 1

        #     for y in range(b-1, t-1, -1):
        #         ret[y][x] = i
        #         i += 1
        #     t += 1
        # return ret

    '''
    螺旋矩阵 III

    在 R 行 C 列的矩阵上，我们从 (r0, c0) 面朝东面开始

    这里，网格的西北角位于第一行第一列，网格的东南角位于最后一行最后一列。

    现在，我们以顺时针按螺旋状行走，访问此网格中的每个位置。

    每当我们移动到网格的边界之外时，我们会继续在网格之外行走（但稍后可能会返回到网格边界）。

    最终，我们到过网格的所有 R * C 个空间。

    按照访问顺序返回表示网格位置的坐标列表。

    图片无法复制，查看原链接
    链接：https://leetcode-cn.com/problems/spiral-matrix-iii
    '''
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> list:
        '''
        解法1：模拟
        '''
        ans = [(r0, c0)]
        if R * C == 1: return ans
        for k in xrange(1, 2*(R+C), 2):
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k+1), (-1, 0, k+1)):
                for _ in xrange(dk):
                    r0 += dr
                    c0 += dc
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans

