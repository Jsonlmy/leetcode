'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

链接：https://leetcode-cn.com/problems/hamming-distance
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        解法1：列表生成式+逐位比较
        '''
        # return sum([1 for i in range(31) if (1 << i & x) != (1 << i & y)])
        '''
        解法2：异或，因为同位相同等于0，不同才等于1，所以统计x^y中1的个数就可以了
        '''
        return bin(x^y).count('1')


if __name__ == "__main__":
    res = Solution().hammingDistance(1, 4)
    print(res)