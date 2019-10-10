'''
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    解法1：递归，因为是二叉搜索树结构，先深度优先遍历右子树，然后是当前节点，最后遍历左子树，
    相当于从最大的节点开始从高到低遍历，在此过程中将节点的值进行累加即可
    '''
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root: self.recursion(root, 0)
        return root

    def recursion(self, root: TreeNode, total) -> int:
        if not root: return total
    
        if root.right:
            root.val += self.recursion(root.right, total)
        else:
            root.val += total
        if root.left:
            return self.recursion(root.left, root.val)
        return root.val


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(4)
    root.left.left = TreeNode(-2)
    root.right.left = TreeNode(3)
    res = Solution().convertBST(root)