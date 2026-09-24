class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0;
        elif len(nums)==1:
            return 1;
        else:
            output=sorted(nums);
            counter=1;
            max=1;
            for i in range(len(output)-1):
                if abs(output[i+1]-output[i])==1:
                    counter+=1;
                elif output[i + 1] == output[i]:
                    continue
                else:
                    counter=1;
                if max<counter:
                    max=counter;
            return max;