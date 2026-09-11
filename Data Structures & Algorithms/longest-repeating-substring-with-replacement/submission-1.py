class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int) # number of specific chars in the sliding window
        left, longest = 0, 0
        n = len(s)
        max_freq = 0

        for right in range(n):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)


        return longest
                

