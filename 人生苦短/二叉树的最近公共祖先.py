'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

图片见原链接
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        解法1：遍历二叉树，查找目标节点并记录路径，然后比对两者路径
        '''
        if p == root or q == root: return root
        node_path = {'p': None, 'q': None}

        def getNodePath(node, path):
            '''
            遍历整个树，实时更新当前路径，遇到是要找的节点就复制路径
            '''
            if node == p:
                node_path['p'] = path.copy()
            elif node == q:
                node_path['q'] = path.copy()
            if node.left:
                path.append(0)
                getNodePath(node.left, path)
            if node.right:
                path.append(1)
                getNodePath(node.right, path)
            path.pop()

        getNodePath(root, [-1])     # 遍历整棵树取得p和q的路径
        ancestor = root             # 祖先节点先初始化为根节点
        p_path, q_path = node_path['p'], node_path['q']
        depth = min(len(p_path), len(q_path))
        for i in range(1, depth):
            if p_path[i] == q_path[i]:        # 路径为0则往左走，1则往右走
                ancestor = ancestor.right if p_path[i] else ancestor.left
            else:  
                break       # 两者路径不相等说明从上一个节点已经分叉了，最近公共祖先已经找到
        return ancestor
        