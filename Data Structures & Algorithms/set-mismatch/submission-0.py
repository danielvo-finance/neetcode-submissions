class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()

        dupe = None
        for i in range(len(nums) - 1):
            if nums[i] == nums [i+1]:
                dupe = nums[i]
                break
        
        missing = None
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                missing = nums[i] + 1
                break

        if nums[0] != 1:
            missing = 1
        elif nums[-1] != len(nums):
            missing = len(nums)

        return [dupe, missing]