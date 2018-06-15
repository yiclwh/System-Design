"""
LFU (Least Frequently Used) is a famous cache eviction algorithm.

For a cache with capacity k, if the cache is full and need to evict a key in it, 
the key with the lease frequently used will be kicked out.

Implement set and get method for LFU cache.

Example
Given capacity=3
    set(2,2)
    set(1,1)
    get(2)
    >> 2
    get(1)
    >> 1
    get(2)
    >> 2
    set(3,3)
    set(4,4)
    get(3)
    >> -1
    get(2)
    >> 2
    get(1)
    >> 1
    get(4)
    >> 4
"""

PREV,NEXT,KEY,VAL,FREQ = 0,1,2,3,4
class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.freq_map = {}
        self.key_map = {}
        self.min_freq = 1

    def get(self, key):
        key_map, freq_map = self.key_map, self.freq_map
        if key not in key_map:
            return -1
        else:
            val_node = key_map[key]
            val_node[PREV][NEXT],val_node[NEXT][PREV] = val_node[NEXT],val_node[PREV]
            if freq_map[self.min_freq] is freq_map[self.min_freq][NEXT]:
                self.min_freq+=1
            freq = val_node[FREQ]
            root = freq_map.setdefault(freq+1,[])
            if not root:
                root[:] = [root,root,None,None,freq+1]
            val_node[PREV],val_node[NEXT] = root[PREV],root
            val_node[FREQ]+=1
            root[PREV][NEXT] = root[PREV] = val_node
            return key_map[key][VAL]

    def set(self, key, value):
        key_map, freq_map, cap = self.key_map, self.freq_map, self.capacity
        if not cap:
            return
        if key in key_map:
            key_map[key][VAL] = value
            self.get(key)
        else:
            if len(key_map) == cap:
                root = freq_map[self.min_freq]
                node_evict = root[NEXT]
                root[NEXT],node_evict[NEXT][PREV] = node_evict[NEXT], root
                del key_map[node_evict[KEY]]
            self.min_freq = 1
            val_node = [None,None,key,value,1]
            root = freq_map.setdefault(1,[])
            if not root:
                root[:] = [root,root,None,None,1]
            val_node[PREV],val_node[NEXT] = root[PREV],root
            root[PREV][NEXT] = root[PREV] = val_node
            key_map[key] = val_node