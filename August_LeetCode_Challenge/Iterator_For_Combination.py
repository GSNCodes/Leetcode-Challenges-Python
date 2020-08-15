Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 

Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false
 

Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It-s guaranteed that all calls of the function next are valid.

#My Solution
from itertools import permutations, combinations 
class CombinationIterator:
    
    def preprocess(self, characters, length):
        
        result = list(combinations(list(characters), length))
       
        return result
    
    
    def __init__(self, characters: str, combinationLength: int):
        
        self.combination = self.preprocess(characters, combinationLength)
        self.current_index = 0
        

    def next(self) -> str:
        val = self.combination[self.current_index]
        self.current_index += 1
            
        return ''.join(val)
        

    def hasNext(self) -> bool:
        return self.current_index < len(self.combination)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()



class CombinationIterator:

    def __init__(self, c: str, combinationLength: int):
        self.combs = list(map(''.join, itertools.combinations(c, combinationLength)))[::-1]

    def next(self) -> str:
        return self.combs.pop(-1)

    def hasNext(self) -> bool:
        return bool(self.combs)