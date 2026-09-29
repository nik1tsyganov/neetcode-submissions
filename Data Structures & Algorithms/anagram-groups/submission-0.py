class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for string in strs:
            temp = ''.join(sorted(string))
            if temp in group:
                group[temp].append(string)
            else:
                group[temp] = [string]
        
        return [s for i, s in group.items()]
