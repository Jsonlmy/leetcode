'''
根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

链接：https://leetcode-cn.com/problems/daily-temperatures
'''
class Solution:
    def dailyTemperatures(self, T: list) -> list:
        '''
        解法1：栈辅助，建立一个栈存储索引
        '''
        # stack, res = [], [0] * len(T)
        # for i, t in enumerate(T):
        #     while stack and t > T[stack[-1]]:       # 当前温度 > 栈顶温度
        #         res[stack.pop()] = i - stack[-1]    # 出栈，将结果列表写入天数差
        #     else:                                   # 栈为空 or 当前温度 <= 栈顶温度
        #         stack.append(i)                     # 将当前温度及索引入栈
        # return res                                  # 栈中留存元素不用管，因为res初始化为0
        '''
        解法2：逆序遍历，跳跃对比，相比解法1，只需要O(1) 的空间
        75, 71, 69, 72, 76, 73
         ?,  2,  1,  1,  0,  0
        假设现在找75对应的结果，首先找其下一个温度进行比较，若比下一个温度高，则看它在res中对应的值，
        若为0，说明后面没有比它高的温度，自然也没有比当前高的温度。
        反之，则顺着res的索引找下去
        '''
        res = [0] * len(T)
        for i in range(len(T)-2, -1, -1):
            if T[i] < T[i+1]:       # 比下一个温度低
                res[i] = 1
            elif T[i] == T[i+1]:    # 等于下一个温度
                res[i] = res[i+1] + 1 if res[i+1] else 0
            else:
                offset = 1
                while res[i+offset] > 0 and T[i] > T[i+offset]:
                    offset += res[i+offset]
                if T[i] == T[i+offset]:
                    res[i] = res[i+offset] + offset if res[i+offset] else 0
                elif T[i] > T[i+offset]:
                    res[i] = 0
                else:
                    res[i] = offset
        return res
        
if __name__ == "__main__":
    temperatures = [34,80,80,34,34,80,80,80,80,34]
    res = Solution().dailyTemperatures(temperatures)
    print(res)