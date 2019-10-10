'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。

链接：https://leetcode-cn.com/problems/find-the-duplicate-number
'''
class Solution:
    def findDuplicate(self, nums: list) -> int:
        '''
        解法1：排序再找重复，不满足约束条件
        '''
        # nums.sort()
        # for i, j in zip(nums, nums[1:]): if i == j: return i
        # return nums[-1]
        '''
        解法2：字典
        '''
        # dic = {}
        # for n in nums:
        #     if n in dic: return n
        #     dic[n] = 0
        '''
        解法3：Floyd算法，循环检测。参考下面检测链表是否有环
        '''
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1

    # def detectCycle(self, head: ListNode) -> ListNode:
    #     '''
    #     Floyd 算法，设链表有环，则链表分三段，
    #     a: 起点到环点
    #     b: 环点到两指针相遇点
    #     c: 其余部分
    #     S = a + b + c
    #     2(a + b) = a + b + c + a
    #     a = c
    #     上式表面，快慢指针相遇之后，慢指针继续走，从头另起一慢指针，两指针会在环点相遇
    #     '''
    #     fast = slow = head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #         if fast == slow: break
    #     else:
    #         return
    #     while head != slow:
    #         head, slow = head.next, slow.next
    #     return head