'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        '''
        解法1：迭代，将广度优先的队列改成多队列
        '''
        res = []
        cur_level = [root] if root else []
        while cur_level:
            next_level = []
            values = []
            for node in cur_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
                values.append(node.val)
            res.append(values)
            cur_level = next_level
        return res
        