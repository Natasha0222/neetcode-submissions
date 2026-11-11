class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=s.replace(" ","")
        t=t.replace(" ","")

        if sorted(s)==sorted(t):
            return True
        return False
        