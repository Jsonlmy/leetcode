'''
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释: 
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释: 
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

链接：https://leetcode-cn.com/problems/edit-distance
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 详解：https://zhuanlan.zhihu.com/p/80682302
        '''
        解法1：带备忘录递归
        '''
        # memo = {}
        # def dp(i, j):
        #     if (i,j) in memo: return memo[(i,j)]
        #     if i == -1: return j + 1
        #     if j == -1: return i + 1
        #     if word1[i] == word2[j]:
        #         memo[(i,j)] = dp(i-1, j-1)
        #     else:
        #         memo[(i,j)] = min(dp(i,j-1)+1,     # 插入
        #                           dp(i-1,j)+1,     # 删除
        #                           dp(i-1,j-1)+1)   # 替换
        #     return memo[(i,j)]
        # return dp(len(word1)-1, len(word2)-1)
        '''
        解法2：动态规划
        '''
        dp = [[i+j for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
        return dp[len(word1)][len(word2)]

if __name__ == "__main__":
    print(Solution().minDistance('rad', 'apple'))