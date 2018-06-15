"""
Implement a trie with insert, search, and startsWith methods.

Example
    insert("lintcode")
    search("code")
    >>> false
    startsWith("lint")
    >>> true
    startsWith("linterror")
    >>> false
    insert("linterror")
    search("lintcode)
    >>> true
    startsWith("linterror")
    >>> true
"""

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.next = dict()

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()
        
    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        node = self.root
        for c in word:
            if c not in node.next:
                child = TrieNode()
                node.next[c] = child
            node = node.next[c]
        node.is_word = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        node = self.root
        for c in word:
            node = node.next.get(c)
            if not node:
                return False
        return node.is_word

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        node = self.root
        for c in prefix:
            node = node.next.get(c)
            if not node:
                return False
        return True
