'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

链接：https://leetcode-cn.com/problems/move-zeroes
'''
class Solution:
    def moveZeroes(self, nums: list) -> None:
        '''
        解法1：遇到0就在列表尾部加0，然后在遍历一遍移除原来位置的0
        '''
        # origin_len = len(nums)
        # for i in range(origin_len):
        #     if nums[i] == 0: nums.append(0)
        # for i in range(origin_len-1, -1, -1):
        #     if nums[i] == 0: nums.pop(i)
        '''
        解法2：双指针，如果nums必须是固定长度的数组，首先找到第一个0的位置，
        然后从此位置开始，依次将0元素覆盖移动，同时统计0的个数，最后将尾部若干个元素置0
        '''
        length = len(nums)
        for k in range(length):
            if nums[k] == 0: 
                zero_count = 1
                break
        else:
            return
        
        j = k
        while j < length - zero_count:
            if nums[j+zero_count] != 0:
                nums[k] = nums[j+zero_count]
                k += 1
                j += 1
            else:
                zero_count += 1
            
        for i in range(j, length):
            nums[i] = 0


if __name__ == "__main__":
    a = [0,1,0,3,12]
    Solution().moveZeroes(a)
    print(a)