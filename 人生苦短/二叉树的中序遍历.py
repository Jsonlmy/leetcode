'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        '''
        解法1：递归
        '''
        # res = []
        # def inorder(node: TreeNode):
        #     if node.left: inorder(node.left)
        #     res.append(node.val)
        #     if node.right: inorder(node.right)
        # if root: inorder(root)
        # return res
        '''
        一行写法
        '''
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        '''
        解法2：迭代
        '''
        stack, res = [], []
        cur = root
        while stack or cur is not None:
            while cur is not None:  # 往左边探到底
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right         # 尝试右节点
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(Solution().inorderTraversal(root))