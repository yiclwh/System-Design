"""
Implement a counting bloom filter. Support the following method:
1. add(string). Add a string into bloom filter.
2. contains(string). Check a string whether exists in bloom filter.
3. remove(string). Remove a string from bloom filter.

Example
    CountingBloomFilter(3) 
    add("lint")
    add("code")
    contains("lint") // return true
    remove("lint")
    contains("lint") // return false
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

class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.hashFunc = []
        for i in range(k):
            self.hashFunc.append(HashFunction(random.randint(10000, 20000), i * 2 + 3))
        
        self.bits = [0 for i in range(20000)]
    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] += 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        # write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            self.bits[position] -= 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        # write your code here
        for f in self.hashFunc:
            position = f.hash(word)
            if self.bits[position] <= 0:
                return False
        return True
        