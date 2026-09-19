class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap= {};
        for c in nums:
            if c in myMap:
                return True;
            else:
                myMap[c] =1;



       
        return False;
      
