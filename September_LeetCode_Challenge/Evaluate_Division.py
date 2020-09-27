You are given equations in the format A / B = k, where A and B are variables represented as strings, 
and k is a real number (floating-point number). Given some queries, return the answers. 
If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries will result in no division 
by zero and there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], 
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], 
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        
        grid = defaultdict(dict)
        
        for index, [u, v] in enumerate(equations):
            value = values[index]
            # print(value)
            grid[u][v] = value
            grid[v][u] = 1/value
            
        # print(grid)
        
        visited_nodes = set()
        
        # Just for optimization
        @lru_cache(None)
        def helper(start, end):
            if start in visited_nodes:
                return -1
            
            visited_nodes.add(start)
            
            if start not in grid:
                return -1
            
            if start == end:
                return 1
            
            return max(grid[start][y] * helper(y, end) for y in grid[start])
            
            
            
        result = []
        
        for [start, end] in queries:
            visited_nodes.clear()
            
            helper.cache_clear()
            val = helper(start, end)
            if val>0:
                result.append(val)
            else:
                result.append(-1)
            
        return result