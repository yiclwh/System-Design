"""
Implement a standard bloom filter. Support the following method:
1. StandardBloomFilter(k),The constructor and you need to create k hash functions.
2. add(string). add a string into bloom filter.
3. contains(string). Check a string whether exists in bloom filter.

Example
    StandardBloomFilter(3)
    add("lint")
    add("code")
    contains("lint") // return true
    contains("world") // return false
"""

import random

class HashFunction:
    
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed
        
    def hash(self, value):
        ret = 0
        for i in value:
            ret += self.seed * ret + ord(i)
            ret %= self.cap
        return ret


class StandardBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.bitset = dict()
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(random.randint(10000, 20000), i * 2 + 3))

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bitset[position] = 1
    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        # write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            if position not in self.bitset:
                return False
       
        return True