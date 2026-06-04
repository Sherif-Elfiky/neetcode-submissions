class Node:
    def __init__(self, is_ending = False):
        self.is_ending = is_ending
        self.children = {}

class PrefixTree:

    def __init__(self):

        self.dummy = Node()
        

    def insert(self, word: str) -> None:
        current = self.dummy

        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            
            current = current.children[letter]
        current.is_ending = True


    def search(self, word: str) -> bool:
        current = self.dummy
        for letter in word:
            if letter not in current.children:
                return False
            
            current = current.children[letter]
        
        return current.is_ending

        

    def startsWith(self, prefix: str) -> bool:
        current = self.dummy
        for letter in prefix:
            if letter not in current.children:
                return False
            
            current = current.children[letter]
        return True

        
        