'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        解法1：创建一个新的头结点，对比两个链表，挨个插入新链表
        '''
        # head = ListNode(0)
        # cur = head
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # if l1:
        #     cur.next = l1       # l2为空，直接将l1剩下部分全部接上
        # elif l2:
        #     cur.next = l2       # l1为空，直接将l2剩下部分全部接上
        # return head.next
        '''
        解法2：与解法1类似，比较两个链表的头结点，以小的为主链表，遍历主链表，将副链表依次比较插入
        '''
        # if not l1: return l2
        # if not l2: return l1
        # if l2.val < l1.val: l2, l1 = l1, l2
        # head = l1
        # while l1.next:
        #     if not l2: return head      # 副链表以空，直接返回
        #     if l2.val <= l1.next.val:
        #         temp = l1.next
        #         l1.next, l2 = l2, l2.next
        #         l1.next.next = temp
        #     else:
        #         l1 = l1.next
        # l1.next = l2                    # 把副链表剩余部分接在主链表尾部
        # return head
        '''
        解法3：递归法
        '''
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val: l1, l2 = l2, l1         # 比较并交换l1, l2 简化代码
        l1.next = self.mergeTwoLists(l1.next, l2)   # 每次将l1链表的当前节点截断，剩下的部分和l2留给后续递归
        return l1                                   # l1的头结点接上排好序的链表返回