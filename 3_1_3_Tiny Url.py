"""
Given a long url, make it shorter. To make it simpler, let's ignore the domain name.

You should implement two methods:

longToShort(url). Convert a long url to a short url.
shortToLong(url). Convert a short url to a long url starts with http://tiny.url/.
You can design any shorten algorithm, the judge only cares about two things:

The short key's length should equal to 6 (without domain and slash). 
And the acceptable characters are [a-zA-Z0-9]. For example: abcD9E
No two long urls mapping to the same short url and no two short urls mapping to the same long url.

Example
Given url = http://www.lintcode.com/faq/?id=10, run the following code (or something similar):

    short_url = longToShort(url) // may return http://tiny.url/abcD9E
    long_url = shortToLong(short_url) // return http://www.lintcode.com/faq/?id=10
    The short_url you return should be unique short url and start with http://tiny.url/ and 6 acceptable characters. For example "http://tiny.url/abcD9E" or something else.

The long_url should be http://www.lintcode.com/faq/?id=10 in this case.
"""

class TinyUrl:

    def __init__(self):
        self.dict = {}

    def getShortKey(self, url):
        return url[-6:]

    def idToShortKey(self, id):
        ch = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        s = ""
        while id > 0:
            s = ch[id % 62] + s
            id //= 62
        while len(s) < 6:
            s = 'a' + s
        return s

    def shortkeyToid(self, short_key):
        id = 0
        for c in short_key:
            if 'a' <= c and c <= 'z':
                id = id * 62 + ord(c) - ord('a')
            if 'A' <= c and c <= 'Z':
                id = id * 62 + ord(c) - ord('A') + 26
            if '0' <= c and c <= '9':
                id = id * 62 + ord(c) - ord('0') + 52

        return id

    # @param {string} url a long url
    # @return {string} a short url starts with http://tiny.url/
    def longToShort(self, url):
        # Write your code here
        ans = 0
        for a in url:
            ans = (ans * 256 + ord(a)) % 56800235584

        while ans in self.dict and self.dict[ans] != url:
            ans = (ans + 1) % 56800235584

        self.dict[ans] = url
        return "http://tiny.url/" + self.idToShortKey(ans)

    # @param {string} url a short url starts with http://tiny.url/
    # @return {string} a long url
    def shortToLong(self, url):
        # Write your code here
        short_key = self.getShortKey(url)
        return self.dict[self.shortkeyToid(short_key)]
