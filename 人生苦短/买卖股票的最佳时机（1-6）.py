class Solution(object):
    '''
    买卖股票的最佳时机

    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

    注意你不能在买入股票前卖出股票。

    示例 1:

    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
        注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
    示例 2:

    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
    '''
    def maxProfit(self, prices: list) -> int:
        '''
        解法1：暴力搜索
        '''
        # profit = 0
        # for i in range(len(prices) - 1):
        #     if prices[i] >= prices[i+1]: continue   # 如果是递减部分直接跳过，否则TLE
        #     for p in prices[i+1:]:
        #         if p - prices[i] > profit: profit = p - prices[i]
        # return profit
        '''
        解法2：一次遍历，实时更新找到的最小价格，然后将当前价格的差价与最大利润比较，大于就更新
        '''
        # max_profit = 0
        # min_price = 2**30 -1 + 2**30
        # for p in prices:
        #     if p < min_price: min_price = p
        #     if p - min_price > max_profit: max_profit = p - min_price
        # return max_profit
        '''
        通杀解法：动态规划，团灭6道题目。
        dp[i][k][s]为最有利润表，i为天数，k为允许交易次数，s为持有股票的状态
        '''
        dp = [0, float('-inf')]
        for p in prices:
            dp[0] = max(dp[0], dp[1]+p)
            dp[1] = max(dp[1], -p)
        return dp[0]


    '''
    买卖股票的最佳时机 II

    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

    注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1:

    输入: [7,1,5,3,6,4]
    输出: 7
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
         随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
    示例 2:

    输入: [1,2,3,4,5]
    输出: 4
    解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
         注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
         因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    示例 3:

    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
    '''
    def maxProfit2(self, prices: list) -> int:
        '''
        解法1：常规思路，遍历数组，若明天涨就（继续）持有，跌就抛出（如果买了）
        '''
        # if len(prices) < 2: return 0
        # buy, profit = -1, 0
        # for i in range(len(prices)-1):
        #     if prices[i+1] - prices[i] < 0:
        #         if buy != -1:
        #             profit += prices[i] - buy
        #             buy = -1
        #     else:
        #         if buy == -1:
        #             buy = prices[i]
        # if buy != -1:
        #     profit += prices[-1] - buy
        # return profit
        '''
        解法2：应为同一天可以多次交易，所以肯定可以利润最大化，直接遍历数组，如果比前一天高，则进行累加
        '''
        # return sum(b - a for a, b in zip(prices, prices[1:]) if a < b)
        '''
        通杀解法：同1。
        dp[i][k][s]为最有利润表，i为天数，k为允许交易次数，s为持有股票的状态
        '''
        dp = [0, float('-inf')]
        for p in prices: dp[0], dp[1] = max(dp[0], dp[1]+p), max(dp[1], dp[0]-p)
        return dp[0]

    '''
    买卖股票的最佳时机 III

    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1:

    输入: [3,3,5,0,0,3,1,4]
    输出: 6
    解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
         随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
    示例 2:

    输入: [1,2,3,4,5]
    输出: 4
    解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
         注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
         因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
    示例 3:

    输入: [7,6,4,3,1] 
    输出: 0 
    解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
    '''
    def maxProfit3(self, prices: list, k=2) -> int:
        '''
        通杀解法：同1。
        dp[i][k][s]为最有利润表，i为天数，k为允许交易次数，s为持有股票的状态
        '''
        dp = [[[0,0] if i and j else [0, float('-inf')] for j in range(k+1)] for i in range(len(prices)+1)]
        for j in range(1, k+1):
            for i, p in enumerate(prices):
                dp[i+1][j][0] = max(dp[i][j][0], dp[i][j][1]+p)
                dp[i+1][j][1] = max(dp[i][j][1], dp[i][j-1][0]-p)
        return dp[-1][k][0]

    '''
    买卖股票的最佳时机 IV

    给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

    注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

    示例 1:

    输入: [2,4,1], k = 2
    输出: 2
    解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
    示例 2:

    输入: [3,2,6,5,0,3], k = 2
    输出: 7
    解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
         随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
    '''
    def maxProfit4(self, k: int, prices: list) -> int:
        '''
        通杀解法：同1。
        dp[i][k][s]为最有利润表，i为天数，k为允许交易次数，s为持有股票的状态
        '''
        if k > (len(prices)//2):    # 当k大于prices长度一半时，等同于无限制
            return sum(b - a for a, b in zip(prices, prices[1:]) if a < b)

        dp = [[[0, 0 if i else -p] for j in range(k+1)] for i, p in enumerate(prices)]
        for j in range(1, k+1):
            for i, p in enumerate(prices[1:]):
                dp[i+1][j][0] = max(dp[i][j][0], dp[i][j][1]+p)
                dp[i+1][j][1] = max(dp[i][j][1], dp[i][j-1][0]-p)
            if dp[-1][j][0] == dp[-1][j-1][0]: return dp[-1][j][0]  # 如过允许交易k次和允许交易k-1次收益是一样的，那么k+1次也是一样的
        return dp[-1][-1][0]

    '''
    最佳买卖股票时机含冷冻期

    给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

    设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

    你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
    卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
    示例:

    输入: [1,2,3,0,2]
    输出: 3 
    解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    '''
    def maxProfit5(self, prices: list) -> int:
        '''
        同2
        '''
        dp = [0, float('-inf')]
        pre = 0
        for p in prices:
            pre_0 = dp[0]
            dp[0] = max(dp[0], dp[1]+p)
            dp[1] = max(dp[1], pre-p)
            pre = pre_0
        return dp[0]

    '''
    买卖股票的最佳时机含手续费
    
    给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

    你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

    返回获得利润的最大值。

    示例 1:

    输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
    输出: 8
    解释: 能够达到的最大利润:  
    在此处买入 prices[0] = 1
    在此处卖出 prices[3] = 8
    在此处买入 prices[4] = 4
    在此处卖出 prices[5] = 9
    总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
    注意:

    0 < prices.length <= 50000.
    0 < prices[i] < 50000.
    0 <= fee < 50000.

    链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
    '''
    def maxProfit5(self, prices: list, fee: int) -> int:
        '''
        同2
        '''
        dp = [0, float('-inf')]
        for p in prices: dp[0], dp[1] = max(dp[0], dp[1]+p-fee), max(dp[1], dp[0]-p)
        return dp[0]

        


if __name__ == "__main__":
    prices = [1,2]
    
    print(Solution().maxProfit4(1, prices))