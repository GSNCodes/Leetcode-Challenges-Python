Given n non-negative integers representing the histogram-s 
bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10

# O(n) Time and O(n) Space
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left, right = [-1 for i in range(n)], [-1 for i in range(n)]
        
        stack = []
        
        for i in range(n):
            
            if len(stack) == 0:
                stack.append(i)
                left[i] = 0
                
            else:
                
                while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                
                left[i] = 0 if len(stack)==0 else stack[-1]+1
                
                stack.append(i)
                
        stack = []
        
        for i in range(n-1, -1, -1):
            
            if len(stack) == 0:
                stack.append(i)
                right[i] = n-1
                
            else:
                
                while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                
                right[i] = n-1 if len(stack)==0 else stack[-1]-1
                
                stack.append(i)
                
        max_area = 0
        
        for i in range(n):
            max_area = max(max_area, (right[i]-left[i]+1)*heights[i])
            
        return max_area
                    