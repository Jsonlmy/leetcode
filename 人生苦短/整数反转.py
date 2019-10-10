'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

链接：https://leetcode-cn.com/problems/reverse-integer
'''
class Solution(object):
    def reverse(self, x: int):
        """
        解法一：逆序遍历字符串。
        """
        if not x: return x
        neg = False
        if x < 0:
            x = -x
            neg = True
        
        s = str(x)
        limit = 2**31
        res = 0
        for i in range(len(s)-1, -1, -1):
            res += int(s[i])*10**i
            if res > limit: return 0
        
        if neg:
            return -res
        elif res < limit:
            return res
        else:
            return 0