Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104




# O(nlogn) Time and O(1) Space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        res = []
        merge_flag = False
        
        while not merge_flag:
            res = []
            i=0
            merge_flag = True
            while i < len(intervals):
                
                if i != len(intervals) - 1 and intervals[i][1] >= intervals[i + 1][0]:
                    new = [intervals[i][0], max(intervals[i + 1][1], intervals[i][1])]
                    res.append(new)
                    i += 2
                    merge_flag = False
                else:
                    res.append(intervals[i])
                    i += 1
            intervals = res
    
        return res