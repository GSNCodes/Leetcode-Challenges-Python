Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.


class TrieNode(object):
    def __init__(self):
        self.child = {}
        self.val = ""
        
class WordDictionary:
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.val = word
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def match(word, depth, node):
            if depth == len(word): 
                return not (node.val=='')
            if word[depth] != '.':
                return word[depth] in node.child and match(word, depth + 1, node.child[word[depth]])
            else:
                for c in node.child:
                    if match(word, depth+1, node.child[c]):
                        return True
            return False
        return match(word, 0, self.root)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        self.wordSet = set()
        

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)
            self.wordSet.add(word)

    def search(self, word):
        if word in self.wordSet:
            return True
        else:
            for v in self.word_dict[len(word)]:
                # match xx.xx.x with yyyyyyy
                for i, ch in enumerate(word):
                    if ch != v[i] and ch != '.':
                        break
                else:
                    return True
            return False