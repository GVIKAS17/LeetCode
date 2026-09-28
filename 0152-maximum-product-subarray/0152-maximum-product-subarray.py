class Solution(object):
    def maxProduct(self, nums):
        n = len(nums)
        prefix = 0
        suffix = 0
        res = float('-inf')
        for i in range(len(nums)):
            if (prefix == 0): prefix = 1
            if (suffix == 0): suffix = 1
            prefix *= nums[i]
            suffix *= nums[n-1-i]
            res = max(res, max(prefix, suffix))
        return res