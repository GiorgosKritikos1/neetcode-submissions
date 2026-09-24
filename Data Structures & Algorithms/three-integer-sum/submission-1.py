class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums=sorted(nums);
        myset= set();
        for i in range(len(nums)):
            j=i+1; # left pointer
            k=len(nums)-1; # right pointer
            while j < k: 
                if -nums[i]==nums[j]+nums[k]:
                    myset.add((nums[i],nums[j],nums[k]));
                    k-=1;
                    j+=1;
                elif -nums[i]>nums[j]+nums[k]:
                    j+=1;
                else:
                    k-=1;
        return [list(t) for t in myset];