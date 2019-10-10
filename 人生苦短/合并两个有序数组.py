'''
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

链接：https://leetcode-cn.com/problems/merge-sorted-array
'''
class Solution(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        解法1：对两个列表倒序遍历，谁大就放到nums1队尾中
        """
        a = m - 1
        b = n - 1
        for i in range(m+n-1, -1, -1):
            if a >= 0 and b >= 0:
                if nums1[a] > nums2[b]:
                    nums1[i] = nums1[a]
                    a -= 1
                else:
                    nums1[i] = nums2[b]
                    b -= 1
            elif a < 0:
                nums1[:i+1] = nums2[:b+1]
                break