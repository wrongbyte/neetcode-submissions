from collections import deque

# O(n) solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        l = 0
        r = len(s) - 1
        s = list(s)

        while r > l:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True