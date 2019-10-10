'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

链接：https://leetcode-cn.com/problems/palindrome-number
'''
class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        '''
        解法1：字符串
        '''
        # return str(x) == str(x)[::-1]
        '''
        解法2：翻转后半部分与前半部分比较
        '''
        if x < 0 or (x >= 10 and x % 10 == 0): return False     # 小于0，尾数为0都不是回文数
        if x < 10: return True
        second_half = 0
        while x > second_half:
            second_half = second_half*10+(x%10)
            if second_half == x or second_half == (x//10): return True
            x = x // 10
        return False