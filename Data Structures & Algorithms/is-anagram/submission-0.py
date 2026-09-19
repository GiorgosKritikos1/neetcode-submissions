class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myMap1={};
        myMap2={};
        for c in s:
            if c in myMap1:
                myMap1[c]+=1;
            else:
                myMap1[c]=1;
        for c in t:
            if c in myMap2:
                myMap2[c]+=1;
            else:
                myMap2[c]=1;
        if len(myMap1)!=len(myMap2):
            return False;
        else:
            for c in myMap1:
                if c not in myMap2:
                    return False;
                if myMap1[c]!=myMap2[c]:
                    return  False;

        return True;
       

        