'''
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:

输入: [1,2,3,4]
输出: [24,12,8,6]
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）

链接：https://leetcode-cn.com/problems/product-of-array-except-self
'''
class Solution:
    def productExceptSelf(self, nums: list) -> list:
        '''
        不能使用reduce函数，reduce函数连乘会遍历列表，造成超时
        解法1：双指针法，i从0开始递增至len(nums)，j则是逆序递减，例如当i遍历到后半部分时，
        l指针的值为nums[:i]的连乘，res[i]的值为nums[i+1:]的连乘，将两者相乘，正好是nums除了第i个元素之外的连乘
        '''
        res, l, r = [1] * len(nums), 1, 1
        for i, j in zip(range(len(nums)), reversed(range(len(nums)))):
            res[i] *= l
            res[j] *= r
            l *= nums[i]
            r *= nums[j]
        return res

    
if __name__ == "__main__":
    res = Solution().productExceptSelf([2,3,4,5])
    print(res)