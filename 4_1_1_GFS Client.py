"""
Implement a simple client for GFS (Google File System, a distributed file system), it provides the following methods:

    read(filename). Read the file with given filename from GFS.
    write(filename, content). Write a file with given filename & content to GFS.
There are two private methods that already implemented in the base class:

    readChunk(filename, chunkIndex). Read a chunk from GFS.
    writeChunk(filename, chunkIndex, chunkData). Write a chunk to GFS.
To simplify this question, we can assume that the chunk size is chunkSize bytes. 
(In a real world system, it is 64M). The GFS Client's job is splitting a file into multiple chunks (if need) and 
save to the remote GFS server. chunkSize will be given in the constructor. 
You need to call these two private methods to implement read & write methods.

Example
    GFSClient(5)
    read("a.txt")
    >> null
    write("a.txt", "World")
    >> You don't need to return anything, but you need to call writeChunk("a.txt", 0, "World") to write a 5 bytes chunk to GFS.
    read("a.txt")
    >> "World"
    write("b.txt", "111112222233")
    >> You need to save "11111" at chink 0, "22222" at chunk 1, "33" at chunk 2.
    write("b.txt", "aaaaabbbbb")
    read("b.txt")
    >> "aaaaabbbbb"
"""

'''
Definition of BaseGFSClient
'''
class BaseGFSClient:
    def readChunk(self, filename, chunkIndex):
        # Read a chunk from GFS
        pass
    def writeChunk(self, filename, chunkIndex, content):
        # Write a chunk to GFS
        pass

class GFSClient(BaseGFSClient):
    """
    @param: chunkSize: An integer
    """
    def __init__(self, chunkSize):
        # do intialization if necessary
        BaseGFSClient.__init__(self)
        self.chunkSize = chunkSize
        self.chunkNum = dict()

    """
    @param: filename: a file name
    @return: conetent of the file given from GFS
    """
    def read(self, filename):
        # write your code here
        if filename not in self.chunkNum:
            return
        content = ''
        for index in range(self.chunkNum[filename]):
            sub_content = BaseGFSClient.readChunk(self, filename, index)
            if sub_content:
                content += sub_content
        return content

    """
    @param: filename: a file name
    @param: content: a string
    @return: nothing
    """
    def write(self, filename, content):
        # write your code here
        length = len(content)
        chunkNum = length//self.chunkSize + 1
        self.chunkNum[filename] = chunkNum
        for index in range(chunkNum):
            sub_content = content[index * self.chunkSize : (index + 1) * self.chunkSize]
            BaseGFSClient.writeChunk(self, filename, index, sub_content)