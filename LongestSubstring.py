class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        maxi = 0
        i = 0
        while i < len(s) - 1:
            seen[s[i]] = 1
            count = 1
            j = i + 1
            while j < len(s):
                if s[j] in seen:
                    seen.clear()
                    i += 1
                    j = len(s) + 1
                else:
                    seen[s[j]] = 1
                    count += 1
                    j += 1
            maxi = max(maxi,count)
        return maxi
        """
        :type s: str
        :rtype: int
        """
s = Solution()
print(s.lengthOfLongestSubstring(""))