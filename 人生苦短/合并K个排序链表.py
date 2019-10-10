'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6

链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
'''
from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        '''
        解法1：将所有链表放到一个数组中再将数组排序，最后构造一个新的链表，
        时间复杂度为O(N log N)，空间复杂度为O(N)，N为所有链表的节点数
        '''
        # if len(lists) == 0: return None
        # if len(lists) == 1: return lists[0]
        # total = []
        # for node in lists:
        #     while node:
        #         total.append(node)
        #         node = node.next
            
        # total.sort(key=lambda x: x.val)
        # for i in range(len(total)-1):
        #     total[i].next = total[i+1]
        # if len(total) < 1:
        #     return None
        # total[-1].next = None
        # return total[0]
        '''
        解法2：逐一比较，每次查找数组中最小节点，并将该链表的节点往后移，若为空，则弹出
        时间复杂度为O(kN)，最差为O(N^2)，空间复杂度为O(1)，k为链表数
        '''
        # def searchMinNode() -> ListNode:
        #     min_idx = -1
        #     min_val = float('inf')
        #     for i in range(len(lists)):
        #         if lists[i].val < min_val:
        #             min_idx, min_val = i, lists[i].val
        #     res = lists[min_idx]
        #     if res.next:
        #         lists[min_idx] = res.next
        #     else:
        #         lists.pop(min_idx)
        #     return res

        # for i in range(len(lists)-1, -1, -1):   # 移除坑爹输入
        #     if not lists[i]: lists.pop(i)
        # head = node = ListNode(0)
        # while lists:
        #     node.next = searchMinNode()
        #     node = node.next
        # return head.next
        '''
        解法3：优先队列优化的方法2
        时间复杂度为O(N log k)，空间复杂度为O(k)
        '''
        # q = PriorityQueue()
        # for i in range(len(lists)):
        #     if lists[i]:
        #         q.put((lists[i].val, i))
        
        
        # head = p = ListNode(0)
        # while not q.empty():
        #     val, i = q.get()
        #     p.next = lists[i]
        #     p = p.next
        #     if p.next:
        #         lists[i] = p.next
        #         q.put((lists[i].val, i))
        
        # return head.next
        '''
        解法4：分治，将所有链表按2个一组，每组合并为单个链表，重复此过程知道最后只剩一个链表
        时间复杂度为O(N log k)，空间复杂度为O(k)
        '''
        if len(lists) == 0: return None
        while len(lists) > 1:
            left = 0
            right = len(lists) - 1
            while right > left:     # 双指针首尾合并
                lists[left] = self.mergeTwoLists(lists[left], lists[right])
                left += 1
                right -= 1
            lists = lists[:right+1]
        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val > l2.val: l1, l2 = l2, l1         # 比较并交换l1, l2 简化代码
        l1.next = self.mergeTwoLists(l1.next, l2)   # 每次将l1链表的当前节点截断，剩下的部分和l2留给后续递归
        return l1      

    
def test_build(nums: list) -> ListNode:
    head = node = ListNode(nums[0])
    for n in nums[1:]:
        node.next = ListNode(n)
        node = node.next
    return head

if __name__ == "__main__":
    lists = []
    lists.append(test_build([1,4,5]))
    lists.append(test_build([1,3,4]))
    lists.append(test_build([2,6]))

    res = Solution().mergeKLists(lists)