"""
Implement a webpage Crawler to crawl webpages of http://www.wikipedia.org/. To simplify the question, let's use url instead of the the webpage content.

Your crawler should:

1. Call HtmlHelper.parseUrls(url) to get all urls from a webpage of given url.
2. Only crawl the webpage of wikipedia.
3. Do not crawl the same webpage twice.
4. Start from the homepage of wikipedia: http://www.wikipedia.org/


"""

from threading import Thread
from Queue import Queue
from urlparse import urlparse

queue = Queue()
results = {}

class CrawlerThread(Thread):
    def run(self):
        global queue, results
        while True:
            url = queue.get()
            if url not in results \
                and urlparse(url).hostname.endswith("wikipedia.org"):
                results[url] = True
                urls = HtmlHelper.parseUrls(url)
                for url in urls:
                    queue.put(url)
            queue.task_done()
            

#class HtmlHelper:
#    @classmethod
#    def parseUrls(cls, url)
#       # Get all urls from a webpage of given url.
class Solution:
    # @param {string} url a url of root page
    # @return {string[]} all urls
    def crawler(self, url):
        # Write your code here
        global queue, results
        thread_pools = []
        for i in range(10):
            thread_pools.append(CrawlerThread())
            thread_pools[i].setDaemon(True)
            thread_pools[i].start()

        queue.put(url)

        queue.join()
        rt = []
        for key, value in results.items():
            rt.append(key)
        return rt