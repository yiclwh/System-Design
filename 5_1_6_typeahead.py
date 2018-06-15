"""
Implement typeahead. Given a string and a dictionary, return all words that contains the string as a substring. 
The dictionary will give at the initialize method and wont be changed. The method to find all words with given substring would be called multiple times.

Example
Given dictionary = {"Jason Zhang", "James Yu", "Bob Zhang", "Larry Shi"}

search "Zhang", return ["Jason Zhang", "Bob Zhang"].

search "James", return ["James Yu"].
"""

class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        # do intialization if necessary
        self.mp = {}
        for s in dict:
            l = len(s)
            for i in range(l):
                for j in range(i + 1, l + 1):
                    tmp = s[i:j]
                    if tmp not in self.mp:
                        self.mp[tmp] = [s]
                    elif self.mp[tmp][-1] != s:
                        self.mp[tmp].append(s)
    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        # write your code here
        if str not in self.mp:
            return []
        else:
            return self.mp[str]