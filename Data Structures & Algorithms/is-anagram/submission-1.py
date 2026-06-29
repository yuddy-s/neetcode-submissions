class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = {}
        l2 = {}
        length = len(s)
        length2 = len(t)

        if (length != length2):
            return False

        for i in range(0, length):
            if (s[i] not in l1.keys()):
                l1.update({s[i]: 1})
            elif (s[i] in l1.keys()):
                l1[s[i]] += 1

            if (t[i] not in l2.keys()):
                l2.update({t[i]: 1})
            elif (t[i] in l2.keys()):
                l2[t[i]] += 1

        for item in l1:
            if (item not in l2.keys()) or (l1[item] != l2[item]):
                return False

        return True