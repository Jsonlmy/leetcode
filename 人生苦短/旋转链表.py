'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

链接：https://leetcode-cn.com/problems/rotate-list
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        解法1：先遍历一遍链表，得到长度l，m = k % l, if m == 0 则直接返回，
        否则将链表首尾相连，在 l - m 处节点断开环
        '''
        if k == 0: return head
        dic = {}
        node = head
        length = 1
        while node.next:
            length += 1
            node = node.next
        
        step = k % length
        if step == 0: return head
        step = k - step - 1

        node.next = head
        node = head
        while step > 0:
            node = node.next
            step -= 1

        res = node.next
        node.next = None
        return res
