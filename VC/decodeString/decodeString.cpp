// decodeString.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#include <string>
#include <tuple>
#include <stack>

using namespace std;

class Solution {
public:
	string decodeString(string s) {
		int num = 0;
		string res = "";
		stack<pair<int, string>> st;

		for (auto c : s) 
		{
			if (isdigit(c))
				num = 10 * num + (c - '0');
			else if (isalpha(c))
				res += c;
			else if (c == '[')
			{
				st.push(make_pair(num, res));
				num = 0;
				res = "";
			}
			else
			{
				auto t = st.top();
				st.pop();
				string tmp = "";
				for (size_t i = 0; i < t.first; i++)
					tmp += res;

				res = t.second + tmp;
			}
		}
		return res;
	}
};


int main()
{
	auto s = Solution();
    std::cout << s.decodeString("100[leetcode]") << endl; 
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
