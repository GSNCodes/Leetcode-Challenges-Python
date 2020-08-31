Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] 
and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:
1 <= A.length <= 20000
1 <= A[i] <= 100000


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        ma = max(A)
        N = len(A)
        m = list(range(ma + 1))
        for a in A:
            for k in range(2, int(math.sqrt(a)) + 1):
                if a % k == 0:
                    self.u(m, a, k)
                    self.u(m, a, a // k)
        count = collections.defaultdict(int)
        for a in A:
            count[self.f(m, a)] += 1
        return max(count.values())
        
    def f(self, m, a):
        while m[a] != a:
            m[a] = m[m[a]]
            a = m[a]
        return a
    
    def u(self, m, a, b):
        if m[a] == m[b]: return
        pa = self.f(m, a)
        pb = self.f(m, b)
        m[pa] = pb