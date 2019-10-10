'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

图片见原链接
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        '''
        解法1：根据其性质，左子树的全部点都比根节点小，右子树的全部点都比根节点大。
        所以当遇到两个点比根节点一大一小时必然分布在不同的子树上，所以根节点必然是其最近公共祖先。
        否则根据情况将根节点设为其左节点或右节点
        '''
        while (root.val - p.val) * (root.val - q.val) > 0: root = (root.right, root.left)[q.val > root.val]
        return root