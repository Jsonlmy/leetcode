'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

链接：https://leetcode-cn.com/problems/counting-bits
'''
class Solution:
    def countBits(self, num: int) -> list:
        '''
        解法1：bin函数
        '''
        # return [bin(i).count('1') for i in range(num+1)]
        '''
        解法2：动态规划-最高有效位。
        0，1的二进制位分别有0和1个1，2-3与0-1相比只是最高位多了一个1，4-7与0-3相比也是最高位多了一个1：
        [a(k+1), a(k+2), ..., a(2k-1)] = [a(0), a(1), ..., a(k-1)]，   k = 2^n
        '''
        # res = [0]
        # while len(res) <= num: res += [1 + i for i in res[:num-len(res)+1]]
        # return res
        '''
        解法3：动态规划-最低有效位。
        11(1011)、10(1010)的前三位与5(101)是一样的，区别在于最低位多了一个1或0，规律如下：
        a[i] = a[i//2] + i mod 2
        '''
        # res = [0] * (num+1)
        # for i in range(1, num+1): res[i] = res[i//2] + i%2
        # return res
        # 列表生成式写法
        # res = [0, 1]
        # while len(res) <= num: res += res[len(res)//2:] + [i+1 for i in res[len(res)//2:]]
        # return res[:num+1]
        '''
        解法4：动态规划+最后设置位。
        公式：a[i] = a[i&(i-1)] + 1，例子：
        1100 & 1011 = 1000
        11010 & 11001 = 11000
        可以发现 x & (x-1)，二进制上只少1个1
        '''
        res = [0] * (num+1)
        for i in range(1, num+1): res[i] = res[i&(i-1)] + 1
        return res

if __name__ == "__main__":
    print(Solution().countBits(15))