class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        for (int i = 0; i < size(prices); i++) {
            for (int j = i + 1; j < size(prices); j++) {
                int potential_profit = prices[j] - prices[i];
                if (potential_profit > max_profit) {
                    max_profit = potential_profit;
                }
            }
        }
        return max_profit;
    }
};
