'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

链接：https://leetcode-cn.com/problems/group-anagrams
'''
class Solution:
    def groupAnagrams(self, strs: list) -> list:
        '''
        解法1：对每一个字符串先排序，按排序后的结果归类，n * klogk
        '''
        # dic = {}
        # for s in strs:
        #     key = tuple(sorted(s))
        #     if key in dic:
        #         dic[key].append(s)
        #     else:
        #         dic[key] = [s]
        # return list(dic.values())
        '''
        解法2：因为每个字符串只有小写字母，所以将字符串中的每个字母的数量进行统计建立一个元组作为字典的key
        '''
        # dic = {}
        # for s in strs:
        #     lis = [0] * 26
        #     for c in s:
        #         lis[ord(c)-97] += 1
        #     key = tuple(lis)
        #     if key in dic:
        #         dic[key].append(s)
        #     else:
        #         dic[key] = [s]
        # return list(dic.values())
        '''
        解法3：唯一分解定理。将字符串中的每个字母对应一个质数，然后相乘，相同的字母异位词对应的就是同一个结果
        prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103}
        '''
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        dic = {}
        for s in strs:
            key = 1
            for c in s:
                key *= prime[ord(c)-97]
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]
        return list(dic.values())


if __name__ == "__main__":
    res = Solution().groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])
    for r in res: print(r)