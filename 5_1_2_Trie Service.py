"""
Build tries from a list of pairs. Save top 10 for each node.

Example
Given a list of

<"abc", 2>
<"ac", 4>
<"ab", 9>
Return <a[9,4,2]<b[9,2]<c[2]<>>c[4]<>>>, and denote the following tree structure:

         Root
         / 
       a(9,4,2)
      /    \
    b(9,2) c(4)
   /
 c(2)
"""

import collections
"""
Definition of TrieNode:
"""
class TrieNode:
    def __init__(self):
        # <key, value>: <Character, TrieNode>
        self.children = collections.OrderedDict()
        self.top10 = []

class TrieService:

    def __init__(self):
        self.root = TrieNode()

    def get_root(self):
        # Return root of trie root, and 
        # lintcode will print the tree struct.
        return self.root

    # @param {str} word a string
    # @param {int} frequency an integer
    # @return nothing
    def insert(self, word, frequency):
        # Write your your code here
        node = self.root
        for letter in word:
            child = node.children.get(letter, None)
            
            if not child:
               child = TrieNode()
               
            node.children[letter] = child
            self.add_frequency(child.top10, frequency)
            node = child
    
    def add_frequency(self, top10, frequency):
        top10.append(frequency)
        index = len(top10) - 1
        while index > 0:
            if top10[index] > top10[index - 1]:
                top10[index], top10[index - 1] = top10[index - 1], top10[index]
                index -= 1
            else:
                break
        if len(top10) > 10:
            top10.pop()
            