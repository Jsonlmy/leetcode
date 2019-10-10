'''
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, n] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:

输入:
[4,3,2,7,8,2,3,1]

输出:
[5,6]

链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
'''
class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:
        '''
        解法1：集合，使用了额外空间
        '''
        # s = set(nums)
        # return [i for i in range(1, len(nums) + 1) if i not in s]
        '''
        解法2：使用abs函数，因为1 ≤ a[i] ≤ n，所以将所有出现过的元素对应的索引的值设为负，
        最后剩下的正值索引+1的就是未出现过的元素
        '''
        # for n in nums:
        #     nums[abs(n) - 1] = -abs(nums[abs(n) - 1])
        # return [i + 1 for i, n in enumerate(nums) if n > 0]
        '''
        解法3：异或交换，将nums各元素放到其对应的位置，最后返回值与索引不对应的索引值
        '''
        def swap(a, b):
            nums[a] ^= nums[b]
            nums[b] ^= nums[a]
            nums[a] ^= nums[b]

        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]: break
                swap(i, nums[i]-1)
        
        return [i+1 for i in range(len(nums)) if i != nums[i]-1]