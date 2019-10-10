'''
数组中的第K个最大元素

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
'''
import heapq

def partition(nums: list) -> int:
    left, right = 0, len(nums)-2   # 使用第一个和倒数第二个作为左右指针
    pivot = nums[-1]            # 选定最后一位数为基准，如果nums是一个有序数列，该算法会退化到O(n^2)
    while left <= right:
        if nums[left] < pivot:
            left += 1
            continue
        if nums[right] >= pivot:
            right -= 1
            continue
        nums[left], nums[right] = nums[right], nums[left]
    nums[left], nums[-1] = nums[-1], nums[left]  
    return left

def qsort(nums: list) -> list:
    '''
    快速排序
    '''
    if len(nums) < 2: return nums               # 长度小于2不用排序
    if len(nums) == 2 and nums[0] > nums[1]:    # 等于2时检查是否有序
        nums[0], nums[1] = nums[1], nums[0]
        return nums

    mid = partition(nums)   # nums[mid] 是基准，此时nums[:mid]都是小于基准的数，nums[mid+1:]都是大于等于基准的数
    return qsort(nums[:mid]) + [nums[mid]] + qsort(nums[mid+1:])     # 将基准左右两边部分递归排序

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        '''
        解法1：使用小根堆，nums前k个元素全部push到堆中，
        其余元素，凡是发现有大于堆顶的就弹出顶元素，然后将该元素push到堆中
        时间复杂度 : O(N log k)。
        空间复杂度 : O(k)，用于存储堆元素。
        '''
        # heap = []
        # for num in nums[:k]: heapq.heappush(heap, num)
        # for num in nums[k:]: 
        #     if num > heap[0]: heapq.heappushpop(heap, num) 
        # return heap[0]
        '''
        解法2：快速选择，在快速排序算法基础上进行改进，平均O(n)，但是最坏情况为O(n^2)。
        '''
        if len(nums) == 1: return nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]: nums[0], nums[1] = nums[1], nums[0]
            return nums[-k]

        mid = partition(nums)               # 获取基准
        right_length = len(nums) - mid - 1  # 获取大于基准部分的长度
        if right_length == k: return min(nums[mid+1:])      # 长度正好为k，则返回其中最小数
        if right_length == k-1: return nums[mid]            # 长度为k-1，正好基准就是第k大的数
        if right_length == k-2: return max(nums[:mid])      # 长度为k-2，则返回小于基准的部分中最大的数
        if right_length > k: return self.findKthLargest(nums[mid+1:], k)    # 长度大于k，继续递归
        return self.findKthLargest(nums[:mid], k-right_length-1)
        '''
        解法3：introselect算法，O(n)
        '''
        

    
if __name__ == "__main__":
    print(Solution().findKthLargest([5,7,3,5,7,1,5,9,2,3,9,7], 9))
    print(qsort([5,7,3,5,7,1,5,9,2,3,9,7])[-9])