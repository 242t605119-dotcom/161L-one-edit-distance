class Solution:
    def isOneEditDistance(self, s, t):
        if abs(len(s) - len(t)) > 1:
            return False

        if len(s) > len(t):
            s, t = t, s

        i = 0
        j = 0
        difference = 0

        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                difference += 1

                if difference > 1:
                    return False

                if len(s) == len(t):
                    i += 1
                    j += 1
                else:
                    j += 1
            else:
                i += 1
                j += 1

        if j < len(t):
            difference += 1

        return difference == 1
