class Solution(object):
    def threeSum(self, nums):
        
        for i in range(1, len(nums)):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
        res = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                elif  total < 0:
                    left += 1
                else:
                    right -= 1
        return res