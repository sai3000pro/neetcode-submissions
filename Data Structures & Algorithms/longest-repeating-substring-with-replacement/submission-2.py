class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int) # number of specific chars in the sliding window
        left, longest = 0, 0
        n = len(s)

        for right in range(n):
            freq[s[right]] += 1
            while (right - left + 1) - max(freq.values()) > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)


        return longest
                

