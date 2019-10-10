'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

链接：https://leetcode-cn.com/problems/3sum-closest
'''
class Solution(object):
    def threeSumClosest(self, nums: list, target: int) -> int:
        '''
        双指针对撞
        '''
        nums.sort()
        res = float("inf")
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]: continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                tmp = nums[k] + nums[i] + nums[j]
                if abs(tmp - target) < abs(res - target): res = tmp
                if tmp > target: j -= 1
                elif tmp < target: i += 1
                else: return target
        return res


if __name__ == "__main__":
    res = Solution().threeSumClosest([0, 2, 1, -3], 1)
    print(res)