'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

链接：https://leetcode-cn.com/problems/insert-interval。
'''
class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        '''
        解法1：构造法
        '''
        if not intervals:
            return [newInterval]
        result = []
        # 逐个扫描，比对判断
        for i in range(len(intervals)):
            inter_i = intervals[i]
            if newInterval[1] < inter_i[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            if newInterval[1] <= inter_i[1]:
                if newInterval[0] < inter_i[0]:
                    inter_i[0] = newInterval[0]
                result.extend(intervals[i:])
                return result
            else:
                if newInterval[0] > inter_i[1]:
                    result.append(inter_i)
                elif inter_i[0] < newInterval[0]:
                    newInterval[0] =inter_i[0]
        result.append(newInterval)
        return result