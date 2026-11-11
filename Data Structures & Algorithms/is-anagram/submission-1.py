class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sub_s = list(s)
        sub_s.sort()
        sub_t = list(t)
        sub_t.sort()
        return sub_s == sub_t