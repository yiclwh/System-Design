"""
Use Map Reduce to find anagrams in a given list of words.

Example
    Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"],["code"].

    Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba"], ["cd", "dc"], ["e"].
"""

class Anagram:

    # @param {str} line a text, for example "Bye Bye see you next"
    def mapper(self, _, line):
        # Write your code here
        # Please use 'yield key, value' here
        for word in line.split():
            yield ''.join(sorted(list(word))), word

    # @param key is from mapper
    # @param values is a set of value with the same key
    def reducer(self, key, values):
        # Write your code here
        # Please use 'yield key, value' here
        yield key, list(values)