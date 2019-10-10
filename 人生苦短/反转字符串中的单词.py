'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1:

输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        '''
        解法1：两次反转，分割以后第一次翻转单词顺序，组合后整个翻转
        '''
        return ' '.join(s.split(' ')[::-1])[::-1]