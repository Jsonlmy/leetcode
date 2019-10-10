'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
'''
from functools import reduce

class Solution:
    def letterCombinations(self, digits: str) -> list:
        '''
        解法1：建立字典，迭代遍历所有组合
        '''
        # phone = {'2': 'abc',
        #          '3': 'def',
        #          '4': 'ghi',
        #          '5': 'jki',
        #          '6': 'mno',
        #          '7': 'pqrs',
        #          '8': 'tuv',
        #          '9': 'wxyz'}

        # res = ['']
        # for d in digits:
        #     res = [r+a for r in res for a in phone[d]]
        # return res if digits else []
        # return reduce(lambda acc, digit: [x+y for x in acc for y in phone[digit]], digits, ['']) if digits else []

        '''
        解法2：辗转相除法
        '''
        if not digits: return []
        
        _map = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    
        _s = [_map[int(i)-2] for i in digits]
        
        _c = 1
        for i in _s:
            _c = _c*len(i)
        
        out = []
        for i in range(_c):
            idx = ''
            m = i
            for j in _s:
                idx += j[m%len(j)]
                m //= len(j)
            out.append(idx)
            
        return out


    
if __name__ == "__main__":
    res = Solution().letterCombinations('23')
    print(res)