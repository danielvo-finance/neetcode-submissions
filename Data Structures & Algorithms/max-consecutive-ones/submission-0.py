class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ret = 0
        concur = 0

        for i in nums:
            if i:
                concur += 1
                if concur > ret:
                    ret = concur
            
            else:
                concur = 0
        
        return ret
