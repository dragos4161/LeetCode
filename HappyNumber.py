class Solution(object):
    def isHappy(self, n):
        suma = 0
        seen = {}
        nr = n
        while nr != 1:
            suma = 0
            while n != 0:
                suma += (n % 10) ** 2
                n /= 10
            nr = suma
            n = suma
            if suma not in seen:
                seen[suma] = 1
            else:
                return False
        return True

s = Solution()
if s.isHappy(2) == True:
    print("Happy number")
else:
    print("Not so happy number")