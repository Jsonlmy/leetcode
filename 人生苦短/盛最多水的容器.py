'''
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49

图片见链接
链接：https://leetcode-cn.com/problems/container-with-most-water
'''
class Solution:
    def maxArea(self, height: list) -> int:
        '''
        解法1：暴力搜索，超时
        '''
        # maxarea = 0
        # for i in range(0, len(height)-1):
        #     for j in range(i+1, len(height)):
        #         maxarea = max(maxarea, (j-i)*min(height[i], height[j]))
        # return maxarea
        '''
        解法2：双指针，从首尾向中间移动，哪个指针值低就移动哪个，每移动一次重新计算容积
        '''
        maxarea, left, right = 0, 0, len(height)-1
        while left < right:
            maxarea = max(maxarea, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
    