'''
编写一个程序，找到两个单链表相交的起始节点。

图片无法复制，查看原链接
链接：https://leetcode-cn.com/problems/intersection-of-two-linked-lists
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        编写一个程序，找到两个单链表相交的起始节点。
        解法一：将第一个链表的所有元素的地址放到一个字典中，遍历第二个链表，如果当前结点在字典中存在，则返回
        """
        # if not headA or not headB: return
        # dic = {}
        # node = headA
        # while node:
        #     dic[node] = None
        #     node = node.next
        
        # node = headB
        # while node:
        #     if node in dic: return node
        #     node = node.next
        """
        解法二：算出两个链表的长度，然后在长链表的某个结点开始和短链表同时遍历，遇到相同结点则说明相交
        其中某个结点满足：从该结点到末尾的长度等于短链表的长度
        """
        # if not headA or not headB: return
        # length, node = 0, headA
        # while node:
        #     length += 1
        #     node = node.next

        # node = headB
        # while node:
        #     length -= 1
        #     node = node.next

        # if length < 0: headA, headB, length = headB, headA, -length

        # for i in range(length): headA = headA.next
        
        # while headA:
        #     if headA is headB: return headA
        #     headA, headB = headA.next, headB.next
        """
        解法三：将A接到B尾部，B接到A尾部，使两个链表等长，然后再同时遍历，遇到相同结点则说明相交
        但是基于python提交会超时
        """
        if not headA or not headB: return
        node = headA
        while node.next: node = node.next
        node.next = headB

        node = headB
        while node.next: node = node.next
        node.next = headA

        while headA:
            if headA is headB: return headA
            headA, headB = headA.next, headB.next

if __name__ == "__main__":
    pass