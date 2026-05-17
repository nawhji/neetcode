class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        from collections import defaultdict

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for char_s in s:
            s_dict[char_s] += 1
        for char_t in t:
            t_dict[char_t] += 1

        for c in s_dict:
            if s_dict[c] != t_dict[c]:
                return False
        return True