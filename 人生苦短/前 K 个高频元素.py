'''
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
说明：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。

链接：https://leetcode-cn.com/problems/top-k-frequent-elements
'''
import heapq
import collections

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        '''
        解法1：使用Counter统计频率，然后构建列表按频率倒序返回前k个，O(n*logn)
        '''
        # return [i[0] for i in sorted(collections.Counter(nums).most_common(), key=lambda x: -x[0], reverse=True)][:k]
        '''
        解法2：统计次数，堆排序，O(n*logk)
        '''
        # counter = collections.Counter(nums)
        # return heapq.nlargest(k, counter.keys(), key=counter.get)     # counter.get(x) 返回
        '''
        解法3：统计次数，桶排序，O(n)
        '''
        counter = collections.Counter(nums)     # 生成统计字典
        frequency_lis, res = [[] for i in range(len(nums)+1)], []
        for value, count in counter.items():    # 将数字按出现的次数放入频率列表对应下标中
            frequency_lis[count].append(value)
        for p in frequency_lis[::-1]:           # 倒序遍历频率列表，将非空的子列表添加到结果列表中
            if p:
                res += p
                k -= len(p)
                if k == 0: break                # 结果列表满k个就返回
        return res


if __name__ == "__main__":
    res = Solution().topKFrequent([4,1,1,2,2,3], 2)
    print(res)