class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        cumsum=0
        for i in nums:
            if cumsum<0:
                cumsum=0
            cumsum+=i
            maxsub=max(maxsub,cumsum)
        return maxsub        
        