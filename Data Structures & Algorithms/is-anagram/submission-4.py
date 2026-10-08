from sortedcontainers import SortedDict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = SortedDict()
        for char in s:
            if char in s_count:
                s_count[char] += 1
            else:
                s_count[char] = 1

        t_count = SortedDict()
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        
        # for key, value in t_count.items():
        #     if key in s_count:
        #         if s_count[key] != t_count[key]:
        #             return False
        #     else:
        #         return False

        if s_count == t_count:
            return True
        else:
            return False
        
        # return True