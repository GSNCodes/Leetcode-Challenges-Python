In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
If this is impossible, return -1 instead.

 
Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, 
because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0

Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.


# My solution
class orange:
    
    def __init__(self, time, x, y):
        self.time = time
        self.x = x
        self.y = y
    
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten_oranges = []
        flag = False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    rotten_oranges.append(orange(0, i, j))
                
                if grid[i][j] == 1:
                    flag = True
        
        if len(rotten_oranges) == 0 and not flag:
            return 0
                            
                        
                    
        
        for element in rotten_oranges:
            
            if element.x > 0 and grid[element.x - 1][element.y]==1:
                grid[element.x - 1][element.y] = 2
                rotten_oranges.append(orange(element.time+1, element.x-1, element.y))
            
            if element.x < len(grid)-1 and grid[element.x + 1][element.y]==1:
                grid[element.x + 1][element.y] = 2
                rotten_oranges.append(orange(element.time+1, element.x+1, element.y))
                
            if element.y > 0 and grid[element.x][element.y-1]==1:
                grid[element.x][element.y-1] = 2
                rotten_oranges.append(orange(element.time+1, element.x, element.y-1))
                
            if element.y < len(grid[0])-1 and grid[element.x][element.y+1]==1:
                grid[element.x][element.y+1] = 2
                rotten_oranges.append(orange(element.time+1, element.x, element.y+1))
                
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return rotten_oranges[-1].time
                
                    
        


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    count+=1
        step=0
        while q:
            i,j,step=q.pop(0)
            for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                    grid[r][c]=2
                    count-=1
                    q.append((r,c,step+1))
        if count>0:
            return -1
        else:
            return step