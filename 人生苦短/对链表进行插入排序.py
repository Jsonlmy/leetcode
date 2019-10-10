'''
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5

动画见链接
链接：https://leetcode-cn.com/problems/insertion-sort-list
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        '''
        
        '''
        n = head
        a = []
        while n:
            a.append(n.val)
            n = n.next
        a.sort()
        i = 0
        n = head
        while n:
            n.val = a[i]
            i += 1
            n = n.next
        return head