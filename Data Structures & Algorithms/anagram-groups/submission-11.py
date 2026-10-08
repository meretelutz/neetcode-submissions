class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}

        for s in strs:
            s_s = str(sorted(s))
            if s_s in sorted_strs:
                sorted_strs[s_s].append(s)
            else:
                sorted_strs[s_s] = [s]
        
        return list(sorted_strs.values())
            
            