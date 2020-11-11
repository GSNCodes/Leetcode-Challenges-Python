Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.


# My Solution
# O(1) Time and O(1) Space
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        def find_square_distance(pt1, pt2):
            
            return (pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2
        
        
        side_set = set([find_square_distance(p1,p2), find_square_distance(p2,p3), find_square_distance(p3,p4),
                       
                    find_square_distance(p4, p1), find_square_distance(p1, p3), find_square_distance(p2, p4)])
        
        # print(side_set)
        if 0 not in side_set and len(side_set)==2:
            return True
        
        else:
            return False