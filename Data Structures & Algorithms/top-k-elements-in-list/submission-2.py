class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap={};
        for i in range(len(nums)):
            if nums[i] in myMap:
                myMap[nums[i]]+=1;
            else:
                myMap[nums[i]]=1;
        toplist=top_keys = sorted(myMap, key=myMap.get, reverse=True);
        return toplist[:k];