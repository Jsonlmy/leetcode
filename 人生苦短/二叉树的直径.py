'''
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \     
      4   5    
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

注意：两结点之间的路径长度是以它们之间边的数目表示。

链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        '''
        解法1：递归，获取左子树和右子树的深度，两者相加与保存的最大直径进行比较
        '''
        self.max_diam = 0
        def dfs(node: TreeNode) -> int:
            if node is None: return 0
            left_depth, right_depth = dfs(node.left), dfs(node.right)
            self.max_diam = max(self.max_diam, left_depth+right_depth)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return self.max_diam


if __name__ == "__main__":
    print(Solution().diameterOfBinaryTree(TreeNode(1)))