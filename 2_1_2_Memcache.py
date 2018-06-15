"""
Implement a memcache which support the following features:

1. get(curtTime, key). Get the key's value, return 2147483647 if key does not exist.
2. set(curtTime, key, value, ttl). Set the key-value pair in memcache with a time to live (ttl). The key will be valid from curtTime to curtTime + ttl - 1 and it will be expired after ttl seconds. if ttl is 0, the key lives forever until out of memory.
3. delete(curtTime, key). Delete the key.
4. incr(curtTime, key, delta). Increase the key's value by delta return the new value. Return 2147483647 if key does not exist.
5. decr(curtTime, key, delta). Decrease the key's value by delta return the new value. Return 2147483647 if key does not exist.
It's guaranteed that the input is given with increasingcurtTime.

Clarification
Actually, a real memcache server will evict keys if memory is not sufficient, and it also supports variety of value types like string and integer. In our case, let's make it simple, we can assume that we have enough memory and all of the values are integers.

Search "LRU" & "LFU" on google to get more information about how memcache evict data.

Try the following problem to learn LRU cache:
http://www.lintcode.com/problem/lru-cache

Example
    get(1, 0)
    >> 2147483647
    set(2, 1, 1, 2)
    get(3, 1)
    >> 1
    get(4, 1)
    >> 2147483647
    incr(5, 1, 1)
    >> 2147483647
    set(6, 1, 3, 0)
    incr(7, 1, 1)
    >> 4
    decr(8, 1, 1)
    >> 3
    get(9, 1)
    >> 3
    delete(10, 1)
    get(11, 1)
    >> 2147483647
    incr(12, 1, 1)
    >> 2147483647
"""


class Node:
    def __init__(self, v, e):
        self.value = v
        self.exp_time = e

class Memcache:
    def __init__(self):
        # do intialization if necessary
        self.errorValue = 2147483647
        self.map = {}
    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        # write your code here
        if key not in self.map:
            return self.errorValue
        v = self.map[key].value
        e = self.map[key].exp_time
        
        if e != 0 and e < curtTime:
            return self.errorValue
        else:
            return v
        
    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        # write your code here
        exp_time = curtTime + ttl - 1
        if ttl == 0:
            exp_time = 0
        n = Node(value, exp_time)
        self.map[key] = n
    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        # write your code here
        if key in self.map:
            del self.map[key]
        
    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        # write your code here
        if key not in self.map:
            return self.errorValue
        v = self.map[key].value
        e = self.map[key].exp_time
        if e != 0 and e < curtTime:
            return self.errorValue
        else:
            n = Node(v + delta, e)
            self.map[key] = n
            return v + delta
    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        # write your code here
        if key not in self.map:
            return self.errorValue
        v = self.map[key].value
        e = self.map[key].exp_time
        if e != 0 and e < curtTime:
            return self.errorValue
        else:
            n = Node(v - delta, e)
            self.map[key] = n
            return v - delta