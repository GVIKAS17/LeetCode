class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        longest = 0

        while right < len(s):
            i = left
            while i < right:
                if s[i] == s[right]:
                    left += 1
                    break
                i += 1
            if i == right:
                cur_length = right - left + 1
                if cur_length > longest:
                    longest = cur_length
                right += 1
        return longest