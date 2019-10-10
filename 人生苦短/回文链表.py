'''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

链接：https://leetcode-cn.com/problems/palindrome-linked-list
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
        解法1：两遍遍历，第一遍获取长度，第二遍将前一半链表的值入栈，后一半一遍出栈一遍比较
        '''
        # length = 0
        # stack = []
        # node = head
        # while node:
        #     length += 1
        #     node = node.next

        # half = length // 2
        # node = head
        # while half:
        #     stack.append(node.val)
        #     node = node.next
        #     half -= 1
        
        # if length % 2: node = node.next
        # while stack:
        #     if stack.pop() != node.val: return False
        #     node = node.next
        # return True
        '''
        解法2：一遍遍历，将所有值装入列表，比较列表左边部分和右边翻转的部分
        '''
        # lis = []
        # while head:
        #     lis.append(head.val)
        #     head = head.next
        # return lis[:(len(lis)+1)//2] == lis[len(lis)//2:][::-1]
        '''
        解法3：双指针+反转链表，常数空间复杂度，
        快指针走完时慢指针正好到链表的中间，将后半部分链表反转再与原链表前半部分比较
        '''
        def reverse(node: ListNode) -> ListNode:
            prev = None
            while node:
                node_next = node.next
                node.next = prev
                prev = node
                node = node_next
            return prev
        
        if not (head and head.next): return True
        slow, fast = head, head.next
        while fast and fast.next: 
            slow, fast = slow.next, fast.next.next
        
        tail = reverse(slow.next if fast else slow)
        if fast: slow.next = None
        while tail and head:
            if tail.val != head.val: return False
            tail, head = tail.next, head.next
        return True

        
if __name__ == "__main__":
    head = ListNode(0)
    head.next = ListNode(0)
    # head.next.next = ListNode(3)
    res = Solution().isPalindrome(head)
    # while res:
    #     print(res.val)
    #     res = res.next