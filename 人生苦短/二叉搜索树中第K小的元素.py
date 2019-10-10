'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        '''
        解法1：中序遍历，提前终止
        '''
        # tmp = []
        # def search(node: TreeNode):
        #     if node.left: search(node.left)
        #     if len(tmp) == k: return
        #     tmp.append(node.val)
        #     if node.right: search(node.right)
        # search(root)
        # return tmp[-1]
        '''
        解法2：迭代器，chain 函数可以组合多个迭代器，islice 函数对迭代器做切片操作
        '''
        from itertools import chain, islice
        def gen(x): yield from chain(gen(x.left), [x.val], gen(x.right)) if x else ()
        return next(islice(gen(root), k - 1, k))
