class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        longest = 0
        last_seen = {}
        for right in range(len(s)):
            if s[right] in last_seen:
                left = max(left, last_seen[s[right]] + 1)
            last_seen[s[right]] = right
            longest = max(longest, right - left + 1)
        return longest