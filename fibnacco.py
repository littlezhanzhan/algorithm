class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            a =0
            b =1
            while n > 1:
                b, a= b + a, b
                n = n-1
            return b % 1000000008


a = Solution()
print(a.fib(10))
