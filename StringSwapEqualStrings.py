class Solution(object):
    def areAlmostEqual(self, s1, s2):
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
        if count > 2:
            return False
        return all(s1.count(c) == s2.count(c) for c in s1)
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

s = Solution()
if s.areAlmostEqual("bank","kanb") == True:
    print("It can be done")
else:
    print("It can't be done")