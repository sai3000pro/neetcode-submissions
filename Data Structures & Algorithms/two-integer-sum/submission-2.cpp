class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> storage;
        int index1, index2;
        for (int i = 0; i < nums.size(); i++) {
            storage[target - nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++) {
                if (storage.count(nums[i]) && i != storage[nums[i]]) {
                    index1 = i;
                    index2 = storage[nums[i]];
                    break;
                }
        }
        vector<int> res;
        res.emplace_back(index1);
        res.emplace_back(index2);
        return res;
    }
};
