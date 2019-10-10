'''
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。

示例 1:

输入: [2, 6, 4, 8, 10, 9, 15]
输出: 5
解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
说明 :

输入的数组长度范围在 [1, 10,000]。
输入的数组可能包含重复元素 ，所以升序的意思是<=。

链接：https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray
'''
class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        '''
        解法1：比较原数组与排序后数组数值不同的索引，再将最大索引减去最小索引+1
        '''
        # diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
        # return len(diff) and max(diff) - min(diff) + 1
        '''
        解法2：先找出从左往右第一次出现递减的位置，再从右往左找到第一次出现递增的位置，
        然后找出这个区间的极大值和极小值，最后再遍历找到这两个极值应该的位置，时间复杂度O(n)，空间复杂度O(1)
        '''
        length = len(nums)
        left = 0
        while left < length-1:
            if nums[left] > nums[left+1]: break
            left += 1
        right = length - 1
        while right > 0:
            if nums[right] < nums[right-1]: break
            right -= 1
        if right < left: return 0

        local_max = max(nums[left:right+1])
        local_min = min(nums[left:right+1])
        for i, v in enumerate(nums):
            if v > local_min:
                left = i
                break
        for i in range(length-1, -1, -1):
            if nums[i] < local_max:
                right = i
                break
        return right - left + 1


if __name__ == "__main__":
    print(Solution().findUnsortedSubarray([1,3,2,4,5]))