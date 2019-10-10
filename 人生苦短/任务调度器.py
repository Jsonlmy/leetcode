'''
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.

注：
任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。

链接：https://leetcode-cn.com/problems/task-scheduler
'''
from collections import Counter

class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        '''
        解法1：桶思想，设计桶的大小为 n+1，相同的任务不能放入同一个桶，因此桶的个数就是重复次数最多的任务的个数。
        一个桶不管是否放满，其占用的时间均为 n+1，这是因为后面桶里的任务需要等待冷却时间。
        最后一个桶是个特例，由于其后没有其他任务需等待，所以占用的时间为桶中的任务个数。
        最终得到：
        总排队时间 = (桶个数 - 1) * (n + 1) + 最后一桶的任务数
        最后，当任务重复率很低，种类很多时。可以保证不需要待命，因此任务的总等待时间即为任务的总个数。
        '''
        ct = Counter(tasks)
        nbucket = ct.most_common(1)[0][1]
        last_bucket_size = list(ct.values()).count(nbucket)
        res = (nbucket - 1) * (n + 1) + last_bucket_size
        return max(res, len(tasks))


if __name__ == "__main__":
    print(Solution().leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))


