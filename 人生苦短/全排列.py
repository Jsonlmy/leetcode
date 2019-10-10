'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例1:

输入: [1,2]
输出:
[
  [1,2],
  [2,1]
]

示例2:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

链接：https://leetcode-cn.com/problems/permutations
'''
class Solution:
    def permute(self, nums: list) -> list:
        '''
        解法1：回溯法，递归生成列表
        '''
        # ret = [[]]
        # def inner(l: list):
        #     l = l.copy()
        #     l.insert(i, n)
        #     return l

        # for n in nums:
        #     tmp = []
        #     for i in range(len(ret[0])+1):
        #         tmp += [inner(l) for l in ret]
        #     ret = tmp
        # return ret
        '''
        解法2：动态规划
        '''
        res = [[]]  # 设置初始状态
        # for n in nums:
        #     tmp = []
        #     for arr in res:
        #         for i in range(len(arr)+1):
        #             cp = arr.copy()
        #             cp.insert(i, n)
        #             tmp.append(cp)
        #     res = tmp
        for j, n in enumerate(nums): res = [arr[:i]+[n]+arr[i:] for arr in res for i in range(j+1)] # 简洁写法
        return res

       

if __name__ == "__main__":
    ret = Solution().permute([1,2,3])
    for r in ret:
        print(r)