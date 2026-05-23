class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> holder;
        for (int i = 0; i < nums.size(); i++) {
            if (holder[nums[i]] == 1) {
                return true;
            }
            else {
                holder[nums[i]] = 1;
            }
        }
        return false;
    }
};