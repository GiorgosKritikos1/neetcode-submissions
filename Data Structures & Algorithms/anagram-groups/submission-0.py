class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap={};
        for i in range(len(strs)):
            ns=''.join(sorted(strs[i]));
            if ns in myMap:
                myMap[ns].append(strs[i]);
            else:
                myMap[ns]=[strs[i]];
        output=[];
        for i in myMap.values():
            output.append(i);
        return output;