'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

链接：https://leetcode-cn.com/problems/unique-binary-search-trees
'''
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        解法1：动态规划。
        F(n) = sum(F(n-1...0)*F(0...n-1))
        '''
        # if n < 2: return 1
        # res = [1, 1] + [0]*(n-1)
        # for i in range(2, n+1): res[i] = sum([res[j]*res[i-1-j] for j in range(i)])
        # return res[n]
        '''
        解法2：卡塔兰数。
        C(i+1) = 2Ci*(2*i+1) / (i+2)
        '''
        C = 1
        for i in range(n): C = C * 2 * (2 * i + 1) // (i + 2)
        return C


if __name__ == "__main__":
    res = Solution().numTrees(4)
    print(res)