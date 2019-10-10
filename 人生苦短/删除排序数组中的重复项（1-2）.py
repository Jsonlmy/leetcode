class Solution(object):
    '''
    删除排序数组中的重复项 II

    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

    示例 1:

    给定数组 nums = [1,1,2], 

    函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

    你不需要考虑数组中超出新长度后面的元素。
    示例 2:

    给定 nums = [0,0,1,1,1,2,2,3,3,4],

    函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

    你不需要考虑数组中超出新长度后面的元素。
    说明:

    为什么返回数值是整数，但输出的答案是数组呢?

    请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

    你可以想象内部操作如下:

    // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
    int len = removeDuplicates(nums);

    // 在函数里修改输入数组对于调用者是可见的。
    // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }

    链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
    '''
    def removeDuplicates(self, nums: list) -> int:
        '''
        解法：快慢指针，快指针正常遍历数组，慢指针在遇到不重复的数字时才加1
        '''
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]
        return j + 1 if len(nums) else 0

    '''
    删除排序数组中的重复项 II

    给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

    示例 1:

    给定 nums = [1,1,1,2,2,3],

    函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

    你不需要考虑数组中超出新长度后面的元素。
    示例 2:

    给定 nums = [0,0,1,1,1,1,2,3,3],

    函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

    你不需要考虑数组中超出新长度后面的元素。
    说明:

    为什么返回数值是整数，但输出的答案是数组呢?

    请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

    你可以想象内部操作如下:

    // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
    int len = removeDuplicates(nums);

    // 在函数里修改输入数组对于调用者是可见的。
    // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
    for (int i = 0; i < len; i++) {
        print(nums[i]);
    }

    链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
    '''
    def removeDuplicates2(self, nums: list) -> int:
        '''
        解法1：双指针，一次扫描，直接修改数组中的值
        '''
        # last = float('inf')
        # new_len = 0
        # repeat = False
        # for num in nums:
        #     if num == last and repeat: continue
        #     repeat = num == last
        #     if not repeat: last = num
        #     nums[new_len] = num
        #     new_len += 1
        # return new_len
        '''
        解法2：
        '''
        for i in range(len(nums)-1, 1, -1):         # 倒序遍历
            if nums[i] == nums[i-2]: nums.pop(i)    # 若果第i项与i-2项相同就删除
        return len(nums)



if __name__ == "__main__":
    print(Solution().removeDuplicates2([1,1,1,1]))