class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevmap={}
        flag=0
        for i,nu in enumerate(nums):
            if nu in prevmap:
                flag+=1
            else:
                prevmap[nu]=i
        if flag==0:
            return False
        else:
            return True   


