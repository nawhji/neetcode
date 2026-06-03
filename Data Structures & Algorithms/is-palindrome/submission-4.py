class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        def is_valid(c):
            c = c.lower()
            return (
                ord("a") <= ord(c) <= ord("z")
                or ord("0") <= ord(c) <= ord("9")
            )

        while l < r:
            if not is_valid(s[l].lower()):
                l += 1
                continue
            if not is_valid(s[r].lower()):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True