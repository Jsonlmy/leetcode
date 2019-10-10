'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。

链接：https://leetcode-cn.com/problems/palindromic-substrings
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        马拉车算法
        '''
        if not s: return 0

        count = mx = id = 0
        string = '#' + '#'.join(s) + '#'
        
        p = [0] * len(string)
        for i in range(len(string)):
            p[i] = min(p[2*id-i], mx-i+1) if mx > i else 1

            while p[i]+i < len(string) and i >= p[i]:
                if string[p[i]+i] != string[i-p[i]]: break
                p[i] += 1
            
            if p[i]+i > mx+1:
                id = i
                mx = p[i]+i-1

            count += p[i]//2
        
        return count


if __name__ == "__main__":
    res = Solution().countSubstrings('afsdfsdfsdfsfsfsfsfsbc')
    print(res)