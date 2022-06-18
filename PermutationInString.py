from itertools import permutations

class Solution(object):

    def getLetters(self,s1):
        letters = {}
        for s in s1:
            if s not in letters:
                letters[s] = 1
            else:
                letters[s] += 1
        return letters
    def checkInclusion(self, s1, s2):
        #s = ["".join(p) for p in permutations(s1)]
        #for perm in s:
        #    if perm in s2:
        #        return True
        #return False

        letters = {}
        ok = True
        for i in range(len(s2)-len(s1) + 1):
            letters = self.getLetters(s1)
            ok = False
            if s2[i] in letters and letters[s2[i]] > 0:
                ok = True
                letters[s2[i]] -= 1
                for j in range(i+1,i+len(s1)):
                    if s2[j] not in letters:
                        ok = False
                    elif letters[s2[j]] > 0:
                        letters[s2[j]] -= 1
                    else:
                        ok = False
            if ok == True:
                return True

        return False

sol = Solution()
if sol.checkInclusion("abca","bbbcadbbac") == True:
    print("Da")
else:
    print("Nu")