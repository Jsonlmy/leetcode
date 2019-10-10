'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
'''
class Solution:
    def search(self, nums: list, target: int) -> int:
        '''
        解法：一次二分法，首先判读数组是否被旋转，未旋转直接使用一般二分法进行查找
        如果旋转，则先判断目标是否在单调递增的那半边，否则查找令一半
        '''
        if not nums: return -1
        if len(nums) == 1: return -1 if nums[0] != target else 0

        half = len(nums) // 2
        if nums[half] == target: return half

        if nums[0] > nums[-1]:  # 数组被旋转过
            if nums[0] <= nums[half-1]:
                if target >= nums[0] and target <= nums[half-1]:
                    res = self.search(nums[:half], target)
                    base = 0
                else:
                    res = self.search(nums[half:], target)
                    base = half
            else:
                if target >= nums[half] and target <= nums[-1]:
                    res = self.search(nums[half:], target)
                    base = half
                else:
                    res = self.search(nums[:half], target)
                    base = 0
        else:                   # 未被旋转，使用一般二分法查找
            if target < nums[half]:
                res = self.search(nums[:half], target)
                base = 0
            else:
                res = self.search(nums[half:], target)
                base = half
        return -1 if res == -1 else res + base

if __name__ == "__main__":
    res = Solution().search([4,5,6,7,0,1,2], 3)
    print(res)