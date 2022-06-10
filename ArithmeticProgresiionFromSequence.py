class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        seen = {}
        arrSet = set(arr)
        if len(arrSet) == 1:
            return True

        if len(arrSet) != len(arr):
            return False

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                diff = abs(arr[i] - arr[j])
                if diff not in seen:
                    seen[diff] = 1
                else:
                    seen[diff] += 1
        for s in seen:
            if seen[s] == len(arr) - 1:
                return True

        return False

s = Solution()
if s.canMakeArithmeticProgression([0,0,0,0]) == True:
    print("Da")
else:
    print("Nu")
