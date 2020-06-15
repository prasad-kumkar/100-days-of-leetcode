'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach 
the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''
from collections import defaultdict
routes = defaultdict()

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < 1 or n < 1:
            return 0
        elif m is 1 and n is 1:
            return 1
        elif (m, n) not in routes:
            routes[(m,n)] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return routes[(m,n)]