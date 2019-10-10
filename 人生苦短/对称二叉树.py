'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

链接：https://leetcode-cn.com/problems/symmetric-tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''
        解法1：递归，root左子树以 中-左-右 的顺序遍历，右子树以 中-右-左 的顺序遍历，
        将遍历的节点值存入两个列表中，最后两个列表相等说明二叉树对称
        '''
        # nodes = ([], [])
        # def dfs(node: TreeNode, right_first: bool):
        #     nodes[right_first].append(node.val if node else 0)
        #     if node:
        #         dfs(node.left if right_first else node.right, right_first)
        #         dfs(node.right if right_first else node.left, right_first)

        # if root:
        #     dfs(root.right, True)
        #     dfs(root.left, False)
        # return nodes[0] == nodes[1]
        '''
        解法2：递归，不适用辅助列表，同时向左右子树以对称方向进行深度优先探索
        '''
        # def isEqual(node1: TreeNode, node2: TreeNode) -> bool:
        #     if node1 is None and node2 is None: return True
        #     if node1 is None or node2 is None: return False
        #     return (node1.val == node2.val) and isEqual(node1.left, node2.right) and isEqual(node1.right, node2.left)
        # return isEqual(root, root)
        '''
        解法3：迭代
        '''
        queue = [root, root]
        while queue:
            n1 = queue.pop()
            n2 = queue.pop()
            if n1 is None and n2 is None: continue
            if n1 is None or n2 is None: return False
            if n1.val != n2.val: return False
            queue.append(n1.left)
            queue.append(n2.right)
            queue.append(n1.right)
            queue.append(n2.left)
        return True


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))