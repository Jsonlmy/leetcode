'''
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:
输入: [1,2,3]

       1
      / \
     2   3

输出: 6

示例 2:
输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def maxPathSum(self, root: TreeNode) -> int:
    #     '''
    #     解法1：递归，使用一个成员变量保持当前最大的路径和，递归函数返回一个节点到它任意一个子节点（含自身）的最大路径
    #     '''
    #     self.sum = float('-inf')
    #     def recursion(node: TreeNode):
    #         if not node: return 0
    #         left = max(0, recursion(node.left))
    #         right = max(0, recursion(node.right))
    #         self.sum = max(self.sum, node.val + left + right)
    #         return node.val + max(left, right)
    #     recursion(root)
    #     return self.sum
    def maxPathSum(self, root: TreeNode, ok=True) -> int:
        '''
        递归，4行版
        '''
        if not root: return 0
        l, r = self.maxPathSum(root.left, False), self.maxPathSum(root.right, False)
        self.max = max(getattr(self, 'max', float('-inf')), l + root.val + r)
        return self.max if ok else max(root.val + max(l, r), 0)

