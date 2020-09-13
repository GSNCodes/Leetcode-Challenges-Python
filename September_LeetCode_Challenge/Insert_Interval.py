Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# O(n) Time and O(n) Space
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = list()
        for i, interval in enumerate(intervals):
            
            if newInterval is None or interval[1] < newInterval[0]:
                result.append(interval)
                
            elif newInterval[1]<interval[0]:
                result.append(newInterval)
                newInterval = None
                result.append(interval)
                
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
                
        
        if newInterval:
            result.append(newInterval)
            return result
        
        return result