class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            smallest = nums[i]
            pos = i
            for j in range(i, len(nums)):
                if nums[j] < smallest:
                    smallest = nums[j]
                    pos = j
            nums[i], nums[pos] = nums[pos], nums[i]
        return nums