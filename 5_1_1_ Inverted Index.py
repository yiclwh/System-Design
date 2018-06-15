"""
Create an inverted index with given documents.

Given a list of documents with id and content. (class Document)

[
  {
    "id": 1,
    "content": "This is the content of document 1 it is very short"
  },
  {
    "id": 2,
    "content": "This is the content of document 2 it is very long bilabial bilabial heheh hahaha ..."
  },
]
Return an inverted index (HashMap with key is the word and value is a list of document ids).

{
   "This": [1, 2],
   "is": [1, 2],
   ...
}
"""



'''
Definition of Document
class Document:
    def __init__(self, id, cotent):
        self.id = id
        self.content = content
'''
from collections import defaultdict
class Solution:
    # @param {Document[]} docs a list of documents
    # @return {dict(string, int[])} an inverted index
    def invertedIndex(self, docs):
        # Write your code here
        res = defaultdict(list)
        for doc in docs:
            words = doc.content.split()
            for w in words:
                if w in res:
                    if res[w][-1] != doc.id:
                        res[w].append(doc.id)
                else:
                    res[w] = [doc.id]
        return res