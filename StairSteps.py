class Solution():
    def getPossibleWais(self, n):
        wais = []
        wais.append(1)
        wais.append(2)
        for i in range(2,n):
            wais.append(wais[i-2] + wais[i-1])
        return wais[n-1]

s = Solution()
print(s.getPossibleWais(6))