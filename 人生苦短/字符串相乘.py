'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

链接：https://leetcode-cn.com/problems/multiply-strings
'''
MOD = 998244353

class Solution(object):
    def qpow(a: int, b: int) -> int:
        ans = 1
        while b:
            if b & 1: ans = ans*a % MOD
            a = a*a % MOD
            b >>= 1
        return ans

    def resize(self, A: list, size: int, val=0):
        if len(A) > size: A[:] = A[size]
        elif len(A) < size: A += [val] * (size-len(A))

    def fastFourierTransform(self, A: list, d=1, rev=[]):
        if len(rev) != len(A):
            self.resize(rev, len(A))
            rev[0] = 0
            for i in range(1, len(A)):
                rev[i] = (rev[i >> 1] >> 1) | ((i & 1) * (len(A) >> 1))
            
        for i in range(len(A)):
            if i < rev[i]:
                A[i], A[rev[i]] = A[rev[i]], A[i]

        i = 1
        while i < len(A):
            wn = self.qpow(3, (MOD-1)) / (i << 1)
            for j in range(0, len(A), i<<1):
                w = 1
                for k in range(i):
                    x = A[j+k]
                    y = w * A[i+j+k] % MOD
                    A[j+k] = (x+y) % MOD
                    A[i+j+k] = (x-y+MOD) % MOD
                    w = w*wn % MOD
            i <<= 1

        if d == -1:
            A[1:] = A[:0:-1]
            inv = self.qpow(len(A), MOD-2)
            for i in range(len(A)):
                A[i] = A[i] inv % MOD

    def polyMultiply(self, A: list, B: list):
        length = len(A) + len(B) - 1
        n = 1
        while n <= length: n <<= 1

        self.resize(A, n)
        self.resize(B, n)
        self.fastFourierTransform(A)
        self.fastFourierTransform(B)
        
        for i in range(n):
            A[i] = A[i] * B[i] % MOD
            
        self.fastFourierTransform(A, -1)
        self.resize(length)

    def multiply(self, num1: str, num2: str) -> str:
        '''
        解法1：模拟乘法竖式，太慢O(n^2)
        '''
        # if num1 == '0' or num2 == '0': return '0'
        # if len(num1) > len(num2):
        #     num1, num2 = num2, num1
        # multiplier = [int(c) for c in num1]
        # multiplicand = [int(c) for c in num2]
        # results = []
        # for i, m in enumerate(multiplier[::-1]):
        #     tmp = 0
        #     lis = []
        #     for n in multiplicand[::-1]:
        #         tmp += m * n
        #         lis.insert(0, tmp % 10)
        #         tmp = tmp // 10
        #     if tmp:
        #         lis.insert(0, tmp)
        #     results.append(lis)
        
        # for i, r in enumerate(results):
        #     r.extend([0] * i)

        # ret = []
        # idx = -1
        # s = 0
        # while True:
        #     for i in range(len(results)-1, -1, -1):
        #         lis = results[i]
        #         s += lis[idx]
        #         if len(lis) == -idx: del results[i]
        #     ret.insert(0, s % 10)
        #     s = s // 10
        #     if len(results) == 0: break
        #     idx -= 1
        # ret_string = ''.join([str(i) for i in ret])
        # if s:
        #     ret_string = str(s) + ret_string
        # return ret_string
        '''
        解法2：快速傅里叶变换，https://zhuanlan.zhihu.com/p/76622485，O(n logn)
        '''
        A, B = [], []
        

        vector<int> A, B;
        reverse(num1.begin(), num1.end());
        A.resize(num1.size());
        for (size_t i = 0; i < A.size(); ++i) {
            A[i] = num1[i] - '0';
        }
        reverse(num2.begin(), num2.end());
        B.resize(num2.size());
        for (size_t i = 0; i < B.size(); ++i) {
            B[i] = num2[i] - '0';
        }
        polyMultiply(A, B);
        string str;
        for (size_t i = 0; i < A.size(); ++i) {
            str += A[i] % 10 + '0';
            if (A[i] >= 10 && i + 1 >= A.size())
                A.push_back(A[i] / 10);
            else if (A[i] >= 10)
                A[i + 1] += A[i] / 10;
        }
        while (*str.rbegin() == '0')
            str.pop_back();
        reverse(str.begin(), str.end());
        if (str == "")
            str = "0";
        return str;


if __name__ == "__main__":
    ret = Solution().multiply('123', '456')
    print(ret)
