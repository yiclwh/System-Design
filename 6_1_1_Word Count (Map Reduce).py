"""
Using map reduce to count word frequency.

https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html#Example%3A+WordCount+v1.0

Example
    chunk1: "Google Bye GoodBye Hadoop code"
    chunk2: "lintcode code Bye"


    Get MapReduce result:
        Bye: 2
        GoodBye: 1
        Google: 1
        Hadoop: 1
        code: 2
        lintcode: 1
"""

class WordCount:
        
    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value'
        for token in line.split():
            yield token, 1

    # @param key is from mapper 
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value'
        s = sum(values)
        yield key, s