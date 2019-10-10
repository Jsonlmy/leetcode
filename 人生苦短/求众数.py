'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2

链接：https://leetcode-cn.com/problems/majority-element
'''
class Solution(object):
    def majorityElement(self, nums: list) -> int:
        '''
        解法1：遍历，统计
        '''
        # dic = {}
        # for num in nums:
        #     if num in dic:
        #         dic[num] += 1
        #     else:
        #         dic[num] = 1
        # half = len(nums) // 2
        # for k, v in dic.items():
        #     if v > half: return k
        '''
        解法2：设置一个current变量和cnt计数变量，current==num时cnt++否则cnt--，当cnt=0时，current改为num，cnt重置1。
        因为众数的数量比其他数的总和还多，所以即使相互抵消，最后剩下的也还是众数。
        '''
        current, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                current = num
                cnt = 1
            elif current == num:
                cnt += 1
            else:
                cnt -= 1
        return current