# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    '''
    环形链表 I
    给定一个链表，判断链表中是否有环。

    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

    进阶：

    你能用 O(1)（即，常量）内存解决此问题吗？

    示例图片无法复制，查看原链接
    链接：https://leetcode-cn.com/problems/linked-list-cycle
    '''
    def hasCycle(self, head: ListNode):
        """
        解法一：用字典。每遍历一个元素就检查字典，不包含则添加，只要有环存在迟早会遇到
        """
        # if head is None: return False
        # dic, idx = {}, 0
        # while head:
        #     if head in dic:
        #         return True
        #     else:
        #         dic[head] = idx
        #         idx += 1
        #         head = head.next
        # return False
        """
        解法二：双指针，如果存在环，则快指针一定会遇上慢指针
        """
        if head is None or head.next is None: return False
        slow = head.next
        fast = slow.next
        while fast and fast.next:
            if fast is slow: return True
            slow = slow.next
            fast = fast.next.next
        return False

    '''
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

    为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

    说明：不允许修改给定的链表。

    进阶：
    你是否可以不用额外空间解决此题？

    链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
    
    '''
    def detectCycle(self, head: ListNode) -> ListNode:
        '''
        解法1：使用字典辅助，遍历链表，逐个往字典里存入，如果已存在，则返回该节点
        '''
        # dic = {}
        # while head:
        #     if head in dic: return head
        #     dic[head] = 1
        #     head = head.next
        '''
        解法2：Floyd 算法，设链表有环，则链表分三段，
        a: 起点到环点
        b: 环点到两指针相遇点
        c: 其余部分
        S = a + b + c
        2(a + b) = a + b + c + a
        a = c
        上式表面，快慢指针相遇之后，慢指针继续走，从头另起一慢指针，两指针会在环点相遇
        '''
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if fast == slow: break
        else:
            return
        while head != slow:
            head, slow = head.next, slow.next
        return head