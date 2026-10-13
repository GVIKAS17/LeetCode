class Solution(object):
    def maxAlternatingSum(self, nums):
        nums.sort(key = abs, reverse = True)
        n = len(nums)
        k = (n + 1) // 2
        ans = 0
        for i, x in enumerate(nums):
            if i < k:
                ans += x * x
            else:
                ans -= x * x
        return ans