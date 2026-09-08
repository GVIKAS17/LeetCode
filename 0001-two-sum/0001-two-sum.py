class Solution(object):
    def twoSum(self, nums, target):
        hash = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash:
                return [hash[comp],i]
            hash[nums[i]] = i