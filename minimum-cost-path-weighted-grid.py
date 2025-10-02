#Problem: Minimum Cost Path in a Weighted Grid

#Problem Statement:
#Given a 2D grid grid of size m x n where each cell has a cost, find the minimum cost to reach the bottom-right cell (m-1, n-1) from the top-left cell (0,0). You can move in 4 directions: up, down, left, right.

#Example:

#grid = [
#    [1, 3, 1],
#    [1, 5, 1],
#    [4, 2, 1]
#]
#Output: 7
#Explanation: Path: 1→3→1→1→1, sum = 7

import heapq

def minCostPath(grid):
    m, n = len(grid), len(grid[0])
    directions = [(0,1), (1,0), (-1,0), (0,-1)]
    
    # Distance matrix
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = grid[0][0]
    
    pq = [(grid[0][0], 0, 0)]  # (cost, x, y)
    
    while pq:
        cost, x, y = heapq.heappop(pq)
        if x == m-1 and y == n-1:
            return cost
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                newCost = cost + grid[nx][ny]
                if newCost < dist[nx][ny]:
                    dist[nx][ny] = newCost
                    heapq.heappush(pq, (newCost, nx, ny))

# Example usage
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print("Minimum Cost Path:", minCostPath(grid))
