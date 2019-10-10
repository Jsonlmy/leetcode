'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

链接：https://leetcode-cn.com/problems/perfect-squares
'''
import math

class Solution:
    def numSquares(self, n: int) -> int:
        '''
        解法1：动态规划。
        这道题是一个典型的背包问题，当前正整数n的结果对应于n去掉一个完全平方数之后的子问题结果加一，
        但是去掉哪一个完全平方数才能达到最佳结果，这需要去进行一个遍历，然后取最小的值即可。
        状态转移方程：dp[i] = min(dp[i], dp[i-j*j]+1)
        '''
        '''
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            j = 1
            k = i - j
            while k >= 0:
                dp[i] = min(dp[i], dp[k]+1)
                j += 2
                k -= j
        return dp[n]
        '''
        dp = [0]
        for i in range(1, n+1):
            dp.append(min(dp[-j*j] for j in range(1, 1 + int(i**0.5))) + 1)
        return dp[-1]
        '''
        解法2：拉格朗日四平方数公式。
        任何一个正整数都可以表示成不超过四个整数的平方之和。
        推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n=4^a * (8b+7)
        '''
        # 1. 先判断这个数是否满足 4^a * (8b+7)，如果满足，那么这个数就需要 4 个数的平方和表示。
        while n % 4 == 0: n /= 4
        if n % 8 == 7: return 4
        # 2. 如果不满足，再在上面除以 4 之后的结果上，穷举只需要 1 个数就能表示和只需要 2 个数就能表示的情况。
        a = 0
        while a**2 <= n:
            b = int((n - a**2)**0.5)
            if a**2 + b**2 == n: return bool(a) + bool(b)
            a += 1
        # 3. 如果还不满足，那么就需要 3 个数表示
        return 3

if __name__ == "__main__":
    res = Solution().numSquares(12)
    print(res)

