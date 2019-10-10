'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

链接：https://leetcode-cn.com/problems/generate-parentheses
'''
class Solution:
    def generateParenthesis(self, n: int) -> list:
        '''
        解法1：构造法，因为只有一种括号，不存在嵌套问题，所以从左到右构造时保证')'的个数不超过'('的个数即可，
        同时还要控制'('的个数不超过n
        '''
        def inner(t):
            string, left, right = t
            if left < n:
                if right < left:
                    return [(string+'(', left+1, right), (string+')', left, right+1)]
                else:
                    return [(string+'(', left+1, right)]
            else:
                if right < left:
                    return [(string+')', left, right+1)]
                else:
                    return [t]
        pre = [('', 0, 0)]
        now = []
        for i in range(2*n):
            for j in pre:
                now += inner(j)
            pre = now
            now = []
        return [i[0] for i in pre]


if __name__ == "__main__":
    print(Solution().generateParenthesis(0))