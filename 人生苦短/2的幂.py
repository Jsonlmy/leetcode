'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

链接：https://leetcode-cn.com/problems/power-of-two
'''
class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        解法1：按位循环
        '''
        # if n <= 0: return False  # 小于等于0直接False
        # while n > 1:
        #     if n & 1: return False
        #     n = n >> 1
        # return True
        '''
        解法2：在保证n大于0的情况下，n若是2的幂次方，则只有1位为1，与其相差1的数进行按位与运算必为0
        '''
        return n > 0 and n & n - 1 == 0