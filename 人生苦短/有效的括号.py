'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

链接：https://leetcode-cn.com/problems/valid-parentheses
'''
class Solution(object):
    def isValid(self, s):
        """
        解法1：栈+字典
        """
        if not s: return True
        if len(s) % 2 == 1: return False        # 长度为奇数时肯定是无效字符串，可以避免无效计算
        dic = {'(': ')', '[': ']', '{': '}'}
        lis = []
        for c in s:
            if c in dic:
                lis.append(dic[c])
            else:
                if not lis or c != lis[-1]:
                    return False
                lis.pop()
        if lis: return False
        return True