class Solution(object):
    def rearrangeArray(self, nums):
        pos = 0
        neg = 1
        res = [0] * len(nums)
        for i in nums:
            if i > 0:
                res[pos] = i
                pos += 2
            else:
                res[neg] = i
                neg += 2
        return res