'''
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

链接：https://leetcode-cn.com/problems/invert-binary-tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
        解法1：递归，当节点为None时返回。交换左右节点，然后依次对左右节点翻转
        '''
        # if not root: return
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        '''
        解法2：迭代，通过建立一个队列进行辅助，首先将root放入队列，
        当队列不为空时，取队首节点，交换其子节点，再将其非空的子节点入队
        '''
        q = [root] if root else []
        while q:
            node = q.pop(0)
            node.left, node.right = node.right, node.left
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return root