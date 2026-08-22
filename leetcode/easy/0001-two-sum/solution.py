class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap={}
        for i,n in enumerate(nums):
            if target-n in prevmap:
                return [prevmap[target-n],i]
            prevmap[n]=i   
        return     