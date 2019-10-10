'''
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

链接：https://leetcode-cn.com/problems/min-stack
'''
class MinStack:
    '''
    解法1：一个栈，但是不单纯的存储整数，而是存储一个元组，
    其第一个元素是要存储的整数，第二个元素是记录以来的最小元素
    '''
    # def __init__(self):
    #     self.data = [(None, float('inf'))]        

    # def push(self, x: int) -> None:
    #     self.data.append((x, min(x, self.data[-1][1])))     # 遇到更小的元素添加进来时，更新元组的第二项

    # def pop(self) -> None:
    #     if len(self.data) > 1: self.data.pop()

    # def top(self) -> int:
    #     return self.data[-1][0]

    # def getMin(self) -> int:
    #     return self.data[-1][1]
    '''
    解法2：两个栈，一个正常栈，一个存记录的最小值
    '''
    def __init__(self):
        self.data = []
        self.mins = []      

    def push(self, x: int) -> None:
        if self.data:
            self.mins.append(min(x, self.mins[-1]))
        else:
            self.mins.append(x)
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop()
        self.mins.pop()

    def top(self) -> int:
        if self.data: return self.data[-1]

    def getMin(self) -> int:
        if self.mins: return self.mins[-1]

        
