class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        for ch1,ch2 in zip(s,t):
            if ch1 in map_s_to_t:
                if map_s_to_t[ch1] !=ch2:
                    return False
            else:
                map_s_to_t[ch1] = ch2

            if ch2 in map_t_to_s:
                if map_t_to_s[ch2] != ch1:
                    return False
            else:
                map_t_to_s[ch2] = ch1

        return True


        