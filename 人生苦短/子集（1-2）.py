class Solution:
    '''
    子集

    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

    说明：解集不能包含重复的子集。

    示例:

    输入: nums = [1,2,3]
    输出:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

    链接：https://leetcode-cn.com/problems/subsets
    '''
    def subsets(self, nums: list) -> list:
        '''
        动态规划，例：nums = [1,2,3]
        每迭代一次ret元素：
        [[]]
        [[], [1]]
        [[], [1], [2], [2, 1]]
        [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
        '''
        ret = [[]]
        for i in nums: ret = ret + [[i] + j for j in ret]
        return ret
      
    '''
    子集 II

    给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

    说明：解集不能包含重复的子集。

    示例:

    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

    链接：https://leetcode-cn.com/problems/subsets-ii
    '''
    def subsetsWithDup(self, nums: list) -> list:
        '''
        解法1：动态规划，通过字典统计nums各数字出现的次数，然后动态构造子集，该解法也适用于第1题，
        例：[1,2,2]，答案生成顺序为：
        [[]]
        [[]] + [[1]]
        [[], [1]] + [[2], [2,2]] + [[1,2], [1,2,2]]
        '''
        dic = {}
        for num in nums: dic[num] = dic.get(num, 0) + 1
        res = [[]]
        for num, count in dic.items(): res = [arr+[num]*i for arr in res for i in range(count+1)]
        return res


if __name__ == "__main__":
    res = Solution().subsetsWithDup([1,2,2])
    for r in res: print(r)