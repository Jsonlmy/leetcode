'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

链接：https://leetcode-cn.com/problems/3sum
'''
class Solution:
    def threeSum(self, nums: list) -> list:
        '''
        解法1：排序+双指针
        '''
        res = []
        cnt = len(nums)
        if cnt < 3: return res      # 数组个数小于3直接返回空
        nums.sort()                 # 先排序
        for left in range(0, cnt-2):                        # 从数组中最小的数遍历至导数第三个
            if left > 0 and nums[left] == nums[left-1]:     # 如果left和前一个相等跳过，因为完全一样
                continue
            if nums[left] > 0: break                        # left>0返回，因为三个大于零的数和必然大于0
            mid = left + 1
            right = cnt - 1
            while mid < right:
                s = nums[left] + nums[mid] + nums[right]
                if s == 0:
                    res.append((nums[left], nums[mid], nums[right]))
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1                            # 跳过相同的数字，避免重复
                    while right > mid and nums[right] == nums[right-1]: 
                        right -= 1                              
                    mid += 1
                    right -= 1
                elif s < 0:
                    mid += 1
                else:
                    right -= 1
                    if nums[right] < 0: break               # right<0跳出，三个小于零的数和必然小于零
        return res