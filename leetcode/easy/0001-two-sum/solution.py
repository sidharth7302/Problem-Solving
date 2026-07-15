class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       prevmap={}
       for i,n in enumerate(nums):
                      
            n2=target-n
            if n2 in prevmap:
                 return [prevmap[n2],i]
            prevmap[n]=i    
