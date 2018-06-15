"""
Cassandra is a NoSQL storage. The structure has two-level keys.

    1. Level 1: raw_key. The same as hash_key or shard_key.
    2. Level 2: column_key.
    3. Level 3: column_value
raw_key is used to hash and can not support range query. let's simplify this to a string.
column_key is sorted and support range query. let's simplify this to integer.
column_value is a string. you can serialize any data into a string and store it in column value.

implement the following methods:

    1. insert(raw_key, column_key, column_value)
    2. query(raw_key, column_start, column_end) // return a list of entries

Example
    insert("google", 1, "haha")
    query("google", 0, 1)
    >> [（1, "haha")]
"""

"""
Definition of Column:
"""
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MiniCassandra:
    
    def __init__(self):
        # do intialization if necessary
        self.map = {}
        
    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    def insert(self, raw_key, column_key, column_value):
        # write your code here
        if raw_key not in self.map:
            self.map[raw_key] = []
        
        if self.map[raw_key]:
            for i, n in enumerate(self.map[raw_key]):
                if n.key >= column_key:
                    if n.key == column_key:
                        self.map[raw_key][i] = Column(column_key, column_value)
                        return
                    self.map[raw_key].insert(i, Column(column_key, column_value))
                    return
        self.map[raw_key].append(Column(column_key, column_value))
        
    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, raw_key, column_start, column_end):
        # write your code here
        res = []
        if raw_key not in self.map:
            return res
        for n in self.map[raw_key]:
            if n.key >= column_start and n.key <= column_end:
                res.append(n)
        return res
        