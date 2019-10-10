'''
给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 
其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。
以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。

链接：https://leetcode-cn.com/problems/evaluate-division
'''
class Solution:
    def calcEquation(self, equations: list, values: list, queries: list) -> list:
        '''
        解法1：Floyd算法，通过equations，values构造一个邻接矩阵，matrix[a][b] = a / b，
        然后遍历所有相通的路径完善矩阵，最后根据queries查找矩阵
        '''
        index_map = {}
        for eq in equations:
            for c in eq:
                if c not in index_map:
                    index_map[c] = len(index_map)

        matrix = [[-1.0]*len(index_map) for i in range(len(index_map))]
        for eq, val in zip(equations, values):
            numerator, dinominator = eq
            idx_numerator = index_map[numerator]
            idx_dinominator = index_map[dinominator]
            matrix[idx_numerator][idx_dinominator] = val
            matrix[idx_dinominator][idx_numerator] = 1 / val
            matrix[idx_numerator][idx_numerator] = 1
            matrix[idx_dinominator][idx_dinominator] = 1

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                if matrix[i][j] == -1:
                    for k, v in enumerate(matrix[j]):
                        if k != j and v != -1 and matrix[i][k] != -1:
                            matrix[i][j] = matrix[i][k] / v
                            matrix[j][i] = v / matrix[i][k]
                            break

        # for i in range(len(matrix)):
        #     for j in range(len(matrix)):
        #         if i == j:
        #             matrix[i][j] == 1
        #         else:
        #             if matrix[i][j] != -1:
        #                 base = matrix[i][j]
        #                 for k, v in enumerate(matrix[j]):
        #                     if v != -1:
        #                         matrix[i][k] = base*v

        return [matrix[index_map[numerator]][index_map[dinominator]] if numerator in index_map and dinominator in index_map else -1.0 for numerator, dinominator in queries]
            


if __name__ == "__main__":
    res = Solution().calcEquation([['a', 'b'], ['b', 'c']], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    print(res)