'''Implement pow(x, n), which calculates x raised to the power n (xn).
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n<0:
            return x**n
        
        res = 1
        while n > 0:
            if n % 2 != 0: 
                res = res * x
            n = n//2 
            x = x*x
            
        return res
        