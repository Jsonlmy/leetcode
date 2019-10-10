'''
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        '''
        解法1：递归，结束条件，当nums的数量小于等于1时，直接返回节点或None，
        每次去nums中间的节点作为当前根节点，将nums[:half]递归构造左子树，nums[half+1:]构造右子树
        '''
        count = len(nums)
        if count == 0: return None
        if count == 1: return TreeNode(nums[0])
        
        half = count // 2
        root = TreeNode(nums[half])
        root.left = self.sortedArrayToBST(nums[:half])
        root.right = self.sortedArrayToBST(nums[half+1:])
        return root