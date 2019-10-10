'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

链接：https://leetcode-cn.com/problems/lru-cache
'''

from collections import OrderedDict
'''
解法1：有序字典，python自带的有序字典类OrderDict，综合了哈希表和链表
'''
# class LRUCache(OrderedDict):
#     def __init__(self, capacity: int):
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self: return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)
        

class DoubleLinkNode(object): 
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

'''
解法2：哈希表（字典）+双向链表，字典的查找为O(1)，双向链表能够方便的移动元素，同时支持最近使用机制
'''
class LRUCache(object):
    def __init__(self, capacity: int):
        self.dic = {}
        self.head = DoubleLinkNode(-1, -1)
        self.tail = DoubleLinkNode(-1, -1)
        self.head.prev = self.head.next = self.tail
        self.tail.prev = self.tail.next = self.head
        self.capacity = capacity

    def _move_head(self, node: DoubleLinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _insert_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_tail(self):
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        self.dic[node.key]

    def get(self, key: int) -> int:
        if key not in self.dic: return -1
        self._move_head(self.dic[key])
        return self.dic[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._move_head(self.dic[key])
            self.dic[key].value = value
        else:
            node = DoubleLinkNode(key, value)
            self.dic[key] = node
            self._insert_head(node)
            if len(self.dic) > self.capacity:
                self._remove_tail()

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1,1)
    lru.put(2,2)
    lru.get(1)
    lru.put(3,3)