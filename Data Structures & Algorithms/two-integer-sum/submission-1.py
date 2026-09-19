class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        myMap={};
        for i in range(len(nums)):
            num = target- nums[i];
            if num in myMap:
                return [myMap[num], i];
            myMap[nums[i]]=i;
            