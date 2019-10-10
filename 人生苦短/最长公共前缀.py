'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

链接：https://leetcode-cn.com/problems/longest-common-prefix
'''
class Solution(object):
    def longestCommonPrefix(self, strs: list):
        """
        解法1：逐个扫描
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        common = strs[0] if len(strs[0]) < len(strs[-1]) else strs[-1]
        for s in strs:
            while common:
                if s.startswith(common): break
                common = common[:-1]
            else:
                return ""
        return common