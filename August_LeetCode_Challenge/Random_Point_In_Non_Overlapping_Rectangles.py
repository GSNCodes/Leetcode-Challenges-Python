Given a list of non-overlapping axis-aligned rectangles rects, write a function pick 
which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates. 
A point on the perimeter of a rectangle is included in the space covered by the rectangles. 
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] 
are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates 
of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.

Example 1:

Input: 
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]

Output: 
[null,[4,1],[4,1],[3,3]]

Example 2:

Input: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]

Output: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. 
Solution-s constructor has one argument, the array of rectangles rects. pick has no arguments. 
Arguments are always wrapped with a list, even if there aren-t any.


import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.num_pts = 0
        self.cumulative_num_pts = []
        
        for rect in rects:
            self.num_pts += (rect[2]-rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.cumulative_num_pts.append(self.num_pts)
            
            
            
        
    def pick(self) -> List[int]:
        index = random.randint(0, self.num_pts-1)
        l, r = 0, len(self.rects)-1
        
        while l<r:
            mid = l + (r-l)//2
            if self.cumulative_num_pts[mid] <= index:
                l = mid + 1
            else:
                r = mid
                
            
        num_x = self.rects[l][2] - self.rects[l][0] + 1
        num_y = self.rects[l][3] - self.rects[l][1] + 1
        
        total_pts = num_x * num_y
        
        starting_pt = self.cumulative_num_pts[l] - total_pts
        pt_offset = index - starting_pt
        
        return [self.rects[l][0] + pt_offset%num_x, self.rects[l][1] + pt_offset//num_x]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()