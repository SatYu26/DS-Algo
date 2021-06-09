#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY area as parameter.
#

def minimumDistance(area):
    # Write your code here
        
    r = len(area)
    c = len(area[0])
    
    global result
    result = float('inf')
    
    if not area:
        return -1
    if r <=0 or c <=0:
        return -1
    
    dp = [[0 for i in range(r)] for j in range(c)]
    
    def dfs(grid, i, j, dist):
        global result
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return
        
        if dp[i][j] > 0 and dist >= dp[i][j]:
            return
        if grid[i][j] == 9:
            result = min(result, dist)
            
        dp[i][j] = dist
        
        dfs(grid, i-1, j, dist+1)
        dfs(grid, i+1, j, dist+1)
        dfs(grid, i, j-1, dist+1)
        dfs(grid, i, j+1, dist+1)
        return result
        
    x = dfs(area, 0, 0, 0)
    
    if x == float('inf'):
        return -1
    else:
        return x
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    area_rows = int(input().strip())
    area_columns = int(input().strip())

    area = []

    for _ in range(area_rows):
        area.append(list(map(int, input().rstrip().split())))

    result = minimumDistance(area)

    fptr.write(str(result) + '\n')

    fptr.close()
