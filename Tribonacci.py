class Solution():
    def Tribonacci(self, n):
        first = 0
        second = 1
        third = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        for i in range(n-2):
            fib = first + second + third
            first = second
            second = third
            third = fib
        return fib

s = Solution()
print(s.Tribonacci(4))