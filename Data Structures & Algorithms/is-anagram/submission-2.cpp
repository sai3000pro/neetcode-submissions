class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> counter;
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            counter[s[i]]++;
        }
        for (int i = 0; i < t.length(); i++) {
            if (counter.count(t[i]) && counter[t[i]] > 0) {
                counter[t[i]] -= 1;
            }
            else {
                return false;
            }
        }
        return true;

    }
};
