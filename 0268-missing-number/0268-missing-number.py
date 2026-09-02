class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        n = 0
        m = 0
        for i in nums:
            n = n ^ i
        for i in range(1,a+1):
            m = m ^ i
        return m ^ n