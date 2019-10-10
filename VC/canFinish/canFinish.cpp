// canFinish.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
	bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
		vector<int> indegrees(numCourses);
		vector<vector<int>> adjacency{ (size_t)numCourses, vector<int>() };

		for (auto pre : prerequisites)
		{
			indegrees[pre[1]]++;
			adjacency[pre[0]].push_back(pre[1]);
		}
		vector<int> q;
		for (size_t i = 0; i < indegrees.size(); i++)
		{
			if (indegrees[i] == 0) q.push_back(i);
		}
		while (!q.empty())
		{
			auto last = q.back();
			q.pop_back();
			for (auto nxt : adjacency[last])
			{
				if (--indegrees[nxt] == 0) q.push_back(nxt);
			}
		}
		for (auto c : indegrees)
			if (c > 0) return false;
		return true;
	}
};

int main()
{
	vector<vector<int>> prerequisites;
	prerequisites.push_back(vector<int> {0, 1});
	prerequisites.push_back(vector<int> {1, 0});
	bool res = Solution().canFinish(2, prerequisites);
	std::cout << res << endl;
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
