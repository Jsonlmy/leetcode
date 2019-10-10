class Solution:
    '''
    组合总和 I
    给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的数字可以无限制重复被选取。

    说明：

    所有数字（包括 target）都是正整数。
    解集不能包含重复的组合。 
    示例 1:

    输入: candidates = [2,3,6,7], target = 7,
    所求解集为:
    [
    [7],
    [2,2,3]
    ]
    示例 2:

    输入: candidates = [2,3,5], target = 8,
    所求解集为:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]

    链接：https://leetcode-cn.com/problems/combination-sum
    '''
    def combinationSum(self, candidates: list, target: int) -> list:
        '''
        解法1：回溯+剪枝
        '''
        # if target < 0: return []
        # if target == 0: return [[]]
        # return [[num]+comb for i, num in enumerate(candidates) for comb in self.combinationSum(candidates[i:], target - num)]
        '''
        解法2：动态规划。
        a[j] += [a[j-i] + [i]]
        '''
        A = [[[]]] + [[] for i in range(target)]
        for c in candidates:
            for n in range(c, target+1):
                A[n] += [comb+[c] for comb in A[n-c]]
        return A[target]
        
        '''
    组合总和 II
    给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

    candidates 中的每个数字在每个组合中只能使用一次。

    说明：

    所有数字（包括目标数）都是正整数。
    解集不能包含重复的组合。 
    示例 1:

    输入: candidates = [10,1,2,7,6,1,5], target = 8,
    所求解集为:
    [
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
    ]
    示例 2:

    输入: candidates = [2,5,2,1,2], target = 5,
    所求解集为:
    [
      [1,2,2],
      [5]
    ]

    链接：https://leetcode-cn.com/problems/combination-sum-ii
    '''
    def combinationSum2(self, candidates: list, target: int) -> list:
        '''
        解法1：回溯，同1的解法1
        '''
    #     return self.search2(sorted(candidates), target)      # 先排序，再递归

    # def search2(self, sorted_list: list, target: int) -> list:
    #     res = []
    #     for i, v in enumerate(sorted_list):
    #         if i > 0 and sorted_list[i] == sorted_list[i-1]: continue   # 当出现重复数字时直接跳过过
    #         if target > v:
    #             # 因为一个数字不能多次使用，这里由sorted_list[i:]改为sorted_list[i+1:]
    #             res.extend([[v]+lis for lis in self.search2(sorted_list[i+1:], target-v)])
    #         else:
    #             if target == v: res.append([v])
    #             break   # 当出现数字大于等于当前目标值时停止
    #     return res
        '''
        解法2：动态规划
        '''
        a = [{()}] + [set() for i in range(target)]
        for i in sorted(candidates):
            for j in range(target, i-1, -1):            # 在题1的基础上变成倒序
                a[j].update([t+(i,) for t in a[j-i]])   # 使用集合+元组去重
        return list(a[-1])

    '''
    组合总和 III
    找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

    说明：

    所有数字都是正整数。
    解集不能包含重复的组合。 
    示例 1:

    输入: k = 3, n = 7
    输出: [[1,2,4]]
    示例 2:

    输入: k = 3, n = 9
    输出: [[1,2,6], [1,3,5], [2,3,4]]

    链接：https://leetcode-cn.com/problems/combination-sum-iii
    '''
    def combinationSum3(self, k: int, n: int, start=0) -> list:
        '''
        解法1：回溯，同上2道，不过太慢
        '''
    #     self.k = k
    #     return [lis for lis in self.search3([i for i in range(1, 10)], n) if len(lis) == k] if n <= 45 else []

    # def search3(self, sorted_list: list, target: int) -> list:
    #     res = []
    #     for i, v in enumerate(sorted_list):
    #         if target > v:
    #             # 在 II 的基础上，添加 len(lis) < self.k 的限制
    #             res.extend([[v]+lis for lis in self.search3(sorted_list[i+1:], target-v) if len(lis) < self.k])
    #         else:
    #             if target == v: res.append([v])
    #             break   # 当出现数字大于等于当前目标值时停止
    #     return
        '''
        解法2：回溯，重新设计函数。
        给原函数加一个默认参数start=0，当k还剩1的时候判断n是否小于10，
        当k大于1的时候，判断n的一半，并且不能超过10
        '''
        # return ([[n]] if n < 10 else []) if k == 1 else [[i]+j for i in range(start+1, min((n+1)//2, 10)) for j in self.combinationSum3(k-1, n-i, i)]
        '''
        解法3：动态规划。就是第2题换了个马甲，将target换成n，并且限制组合的长度
        '''
        # res = {i: [] for i in range(n+1)}  
        # res[0] = [[]]

        # for i in range(1, 10): 
        #     end = i - 1
        #     for v in range(n, end, -1):
        #         res[v].extend([lis+[i] for lis in res[v-i] if len(lis) < k])
        # return res[n]
        a = [[[]]] + [[] for i in range(target)]
        for i in range(1, 10):
            for j in range(n, i-1, -1):
                a[j].extend([lis+[i] for lis in a[j-i] if len(lis) < k])    # 如果 len(lis) >= k 就放弃
        return [res for res in a[-1] if len(res) == k]

    '''
    组合总和 Ⅳ
    给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。

    示例:
    
    nums = [1, 2, 3]
    target = 4
    
    所有可能的组合为：
    (1, 1, 1, 1)
    (1, 1, 2)
    (1, 2, 1)
    (1, 3)
    (2, 1, 1)
    (2, 2)
    (3, 1)
    
    请注意，顺序不同的序列被视作不同的组合。
    
    因此输出为 7。
    进阶：
    如果给定的数组中含有负数会怎么样？
    问题会产生什么变化？
    我们需要在题目中添加什么限制来允许负数的出现？
    
    链接：https://leetcode-cn.com/problems/combination-sum-iv
    '''
    def combinationSum4(self, nums: list, target: int) -> int:
        '''
        解法1：动态规划，拷贝题1代码，但是超时
        '''
        # a = [[[]]] + [[] for i in range(target)]
        # for i in range(1, target+1):
        #     for j in sorted(nums):
        #         if i >= j: a[i].extend([[j]+lis for lis in a[i-j]])
        # return len(a[-1])
        '''
        解法2：动态规划，找规律，直接加数字
        '''
        A = [1] + [0] * target
        for n in range(1, target+1): 
            A[n] = sum([A[n-c] for c in nums if n >= c])
        return A[target]

if __name__ == "__main__":
    # print(Solution().combinationSum([2,3,5], 8))
    # print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))
    # print(Solution().combinationSum3(3, 9))
    print(Solution().combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10))