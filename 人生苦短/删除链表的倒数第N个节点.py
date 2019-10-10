'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        解法1：遍历链表，将所有节点存入列表中
        '''
        # lis = []
        # node = head
        # while node:
        #     lis.append(node)
        #     node = node.next
        
        # if n == len(lis): return head.next
        # lis[-n-1].next = lis[-n].next
        # return head
        '''
        解法2：双指针，一个指针先走n+1步，然后两个指针再同时走，当快指针到头时，慢指针的next正好是要移除的节点
        '''
        tmp = ListNode(0)   # 在head之前添加一个哑节点，防止超出链表
        tmp.next = head
        fast = head
        for i in range(n): fast = fast.next

        slow = tmp
        while fast: slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return tmp.next