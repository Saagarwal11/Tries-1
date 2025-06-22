
## Problem1 
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isend = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()
   
    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            position = ord(w) - ord('a')
            if not curr.children[position]:
                curr.children[position] = TrieNode()
            curr = curr.children[position]
        curr.isend = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            position = ord(w) - ord('a')
            mynode = curr.children[position]
            if not mynode:
                return False
            curr = mynode
        return mynode.isend 
          
            
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for p in prefix:
            position = ord(p) - ord('a')
            mynode = curr.children[position]
            if not mynode:
                return False
            curr = curr.children[position]
        return True

##Problem2 
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isend = False 
class Trie:
    def __init__(self,TrieNode):
        self.root = TrieNode

class Solution:
    def longestWord(self, words: List[str]) -> str:
        mytrie = Trie(TrieNode())
        words.sort()
        for w in words:
            self.addWord(mytrie.root,w)
        mytrie.root.isend = True
        self.ret = ""


        def dfs(node, path):
            if not node or not node.isend:
                return
            if len(path) > len(self.ret):
                self.ret = "".join(path)
            for i in range(len(node.children)):
                dfs(node.children[i], path+[chr(i + ord('a'))])

        dfs(mytrie.root,[])
        return self.ret
        
## Problem3

class Trie:
    def __init__(self):
        self.children = [None]*26
        self.isend = False 


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        myroot = Trie()
        retstring = ""
        for word in dictionary:
            self.addWord(word,myroot)
        
        rwords = sentence.split(' ')

        for i,r in enumerate(rwords):
            retval = self.findword(myroot,r)

            rwords[i] = retval if retval != "" else rwords[i]

        return ' '.join(rwords)
        
    def addWord(self,word,root):

        curr = root

        for w in word:
            position = ord(w) - ord('a')

            if not curr.children[position]:
                mynode = Trie()
                curr.children[position] = mynode
            curr = curr.children[position]
        curr.isend = True 

    def findword(self,myroot,wordtofind):

        curr = myroot
        ret = ""
        mycurr = ""

        for w in wordtofind:
            position = ord(w) - ord('a')
            if not curr.children[position]:
                break

            mycurr += w
            if curr.children[position] and curr.children[position].isend:
                ret = mycurr
                break
                
            curr = curr.children[position]
        return ret
            






        

