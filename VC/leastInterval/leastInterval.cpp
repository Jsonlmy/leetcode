// leastInterval.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
	int leastInterval(vector<char>& tasks, int n) {
		unordered_map<char, int> counter;
		for (auto c : tasks)
		{
			counter[c] = counter[c] + 1;
		}
		int nbucket = 0, last_bucket_size = 0;
		for (auto p : counter)
		{
			if (p.second > nbucket)
			{
				nbucket = p.second;
				last_bucket_size = 1;
			}
			else if (p.second == nbucket)
			{
				last_bucket_size++;
			}
		}
		return max((nbucket - 1) * (n + 1) + last_bucket_size, static_cast<int>(tasks.size()));
	}
};

int main()
{
	auto s = Solution();
	auto tasks = vector<char>{ 'A','A','A','B','B','B' };
	auto res = s.leastInterval(tasks, 2);
	cout << res << endl;
}

// 运行程序: Ctrl + F5 或调试 >“开始执行(不调试)”菜单
// 调试程序: F5 或调试 >“开始调试”菜单

// 入门提示: 
//   1. 使用解决方案资源管理器窗口添加/管理文件
//   2. 使用团队资源管理器窗口连接到源代码管理
//   3. 使用输出窗口查看生成输出和其他消息
//   4. 使用错误列表窗口查看错误
//   5. 转到“项目”>“添加新项”以创建新的代码文件，或转到“项目”>“添加现有项”以将现有代码文件添加到项目
//   6. 将来，若要再次打开此项目，请转到“文件”>“打开”>“项目”并选择 .sln 文件
