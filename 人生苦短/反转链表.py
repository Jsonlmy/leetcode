'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

链接：https://leetcode-cn.com/problems/reverse-linked-list
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        解法1：借助两个临时变量，一边遍历原列表，一边构建新的逆序列表
        '''
        # prev = None
        # node = head
        # while node:
        #     node_next = node.next
        #     node.next = prev
        #     prev = node
        #     node = node_next
        # return prev
        '''
        解法2：快慢指针递归翻转
        '''
        if not head or not head.next: return head   # 如果是空或只有1个节点，直接返回
        slow, fast = head, head.next                # slow初始化为节点1，fast为节点2
        while fast.next:                            # 当fast有下一个节点
            slow = slow.next                        # slow前进一步
            fast = fast.next
            if fast.next: fast = fast.next          # fast保证自身不为空的情况下前进2步
        right_head = slow.next                      # 原链表右半边的头节点
        self.reverseList(right_head)                # 翻转右半边链表
        slow.next = None                            # 从中间截断原链表
        self.reverseList(head)                      # 翻转左半边链表
        right_head.next = slow                      # rihgt_head现在为新链表的左边的尾结点
        return fast                                 # 返回新的头节点