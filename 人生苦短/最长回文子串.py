'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

链接：https://leetcode-cn.com/problems/longest-palindromic-substring
'''

def getExpandLength(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        解法2：中心展开方法遍历所有字符串，O(n^2)
        '''
        # if len(s) < 2: return s
        # start = end = 0
        # for i in range(len(s)):
        #     len1 = getExpandLength(i, i, s)
        #     len2 = getExpandLength(i, i+1, s)
        #     maxlen = max(len1, len2)
        #     if maxlen > end - start:
        #         start = i - (maxlen-1) // 2
        #         end = i + maxlen // 2 + 1
        # return s[start:end]
        '''
        解法1：manacher算法，O(n)。https://zhuanlan.zhihu.com/p/67559846
        '''
        # if len(s) < 2: return s
        # s = '#' + '#'.join(list(s)) + '#'
        # p = [0] * len(s)
        # max_id = -1
        # max_radius = -1
        # c = -1
        # mx = -1
        # for i in range(len(s)):
        #     if i > mx:
        #         radius = getExpandLength(i, i, s) // 2
        #         p[i] = radius
        #         c = i
        #         mx = i + radius
        #         if radius > max_radius:
        #             max_id, max_radius = i, radius
        #     else:
        #         j = 2*c - i
        #         if j - p[j] > 2 * c - mx:
        #             p[i] = p[j]
        #         elif j - p[j] < 2 * c - mx:
        #             p[i] = mx - i
        #         else:
        #             radius = getExpandLength(i-p[j]-1, i+p[j]+1, s) // 2
        #             p[i] = radius
        #             if i + radius > mx:
        #                 c = i
        #                 mx = i + radius
        #             if radius > max_radius:
        #                 max_id, max_radius = i, radius
        # return s[max_id-max_radius:max_id+max_radius+1].replace('#', '')
        '''
        优化马拉车
        '''
        if len(s) <= 1: return s
        s = '\0\1' +'\1'.join([x for x in s]) + '\1\2' # 每个字符之间插入\1
        p = [0] * len(s)
        center = mx = 0
        max_str = ''
        for i in range(1,len(p)-1):
            if i < mx:                                  # i是在以某一z值为中心的最长回文子串的半径之内
                j = 2*center - i                        # i关于center的对称点
                p[i] = min(mx-i,p[j])
            while s[i-p[i]-1] == s[i+p[i]+1]:           # 尝试继续向两边扩展，更新p[i]
                p[i] += 1
                if i + p[i] > mx:
                    mx = i +p[i]                        # 更新中心
                    center = i
                if 1 + 2*p[i] > len(max_str):
                    max_str = s[i - p[i]:i+p[i]+1]      # 更新最长串
        return max_str.replace('\1','')