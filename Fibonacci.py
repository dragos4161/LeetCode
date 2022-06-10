class Solution():
    def Fibonacci(self, n):
        first = 0
        second = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(n-1):
            fib = first + second
            first = second
            second = fib
        return fib

s = Solution()
print(s.Fibonacci(12))