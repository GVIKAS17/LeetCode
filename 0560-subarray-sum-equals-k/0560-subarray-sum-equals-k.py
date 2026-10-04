class Solution(object):
    def subarraySum(self, nums, k):
        total = 0
        count = 0

        mp = {0:1}
        for num in nums:
            total += num
            
            if total - k in mp:
                count += mp[total - k]
            
            if total in mp:
                mp[total] += 1
            else:
                mp[total] = 1
        return count