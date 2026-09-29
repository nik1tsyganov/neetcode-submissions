class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        res1, res2 = {}, {}
        for i in range(len(s)):
            res1[s[i]] = res1.get(s[i], 0) + 1
            res2[t[i]] = res2.get(t[i], 0) + 1
        
        return res1 == res2