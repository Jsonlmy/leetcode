'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

链接：https://leetcode-cn.com/problems/single-number
'''
class Solution(object):    
    def singleNumber(self, nums) -> int:
        '''
        解法1：使用字典，遍历nums，没有这个key就添加，有就删除，根据数组的性质，最后只有一个key
        '''
        # dic = {}
        # for num in nums:
        #     if num in dic:
        #         dic.pop(num)
        #     else:
        #         dic[num] = 0
        # return dic.popitem()[0]
        '''
        解法2：由于 0^a = a，a^a = 0 ，
        而数组中除了一个数字是只出现一次的，其他数字均出现两次，则可以采用此思路来解答这个问题。 
        异或运算实际上就是不进位的加法，满足交换律
        '''
        res = 0
        for num in nums: res ^= num
        return res