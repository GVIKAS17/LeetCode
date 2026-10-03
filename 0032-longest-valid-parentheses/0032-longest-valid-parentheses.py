class Solution(object):
    def longestValidParentheses(self, s):
        res = [-1]
        count = 0
        max_count = 0
        for i in range(len(s)):
            if s[i] == '(':
                res.append(i)
            else:
                res.pop()

                if not res:
                    res.append(i)
                else:
                    count = i - res[-1]
                    max_count = max(count, max_count)

        return max_count