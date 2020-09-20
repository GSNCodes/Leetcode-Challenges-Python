On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:
1 <= grid.length * grid[0].length <= 20

# My Solution
# O(3^n) Time and O(n) Space
class Solution:
    
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.num_paths = 0
        num_zeros = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 0:
                    num_zeros += 1
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, num_zeros)
                
        
        return self.num_paths
    
    
    def dfs(self, grid, x, y, num_zeros):
        if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]) :
            return
        
        if grid[x][y] == -1 or (grid[x][y] == 2 and num_zeros != 0) or grid[x][y] == '*':
            return

        if grid[x][y] == 2 and num_zeros == 0:
            self.num_paths += 1

        if grid[x][y] == 0:
            num_zeros -= 1


        temp = grid[x][y]
        grid[x][y] = '*';
        self.dfs(grid, x-1, y, num_zeros)
        self.dfs(grid, x+1, y, num_zeros)
        self.dfs(grid, x, y-1, num_zeros)
        self.dfs(grid, x, y+1, num_zeros)
        grid[x][y] = temp