'''
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.pre = None

    def flatten(self, root: TreeNode) -> None:
        '''
        解法1：前序遍历，生成一个顺序的列表，然后遍历列表修改
        '''
        # if root:
        #     lis = self.dfs(root)
        #     for pre, node in zip(lis, lis[1:]): pre.left, pre.right = None, node
        '''
        解法2：前序遍历，借助全局变量直接修改
        '''
        if root is None: return
        if self.pre: self.pre.left, self.pre.right = None, root
        pre, right = root, root.right
        self.flatten(self.left)
        self.flatten(right)
    
    def dfs(self, node: TreeNode) -> list:
        return [node] + (self.dfs(node.left) if node.left else []) + (self.dfs(node.right) if node.right else [])