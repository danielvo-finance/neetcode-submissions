class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        missing_num = []
        
        for i in range(1, nums[0]):
            missing_num.append(i)
        
        for i in range(1, n):
            if nums[i] > nums[i-1] + 1:
                for val in range(nums[i - 1] + 1, nums[i]):
                    missing_num.append(val)

        for i in range(nums[-1] + 1, n + 1):
            missing_num.append(i)

        return missing_num