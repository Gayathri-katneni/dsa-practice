class Solution(object):
    def isMatch(self, s, p):
        """
        Greedy two-pointer with backtracking to the last '*'.
        Time: O(m * n) worst case, Space: O(1)
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = j = 0
        star = -1   # index of last '*' in p
        match = 0   # index in s that the last '*' currently covers up to

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            elif star != -1:
                # Let the last '*' absorb one more character
                j = star + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)
