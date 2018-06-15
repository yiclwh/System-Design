"""
Implement a simple twitter. Support the following method:

1. postTweet(user_id, tweet_text). Post a tweet.
2. getTimeline(user_id). Get the given user's most recently 10 tweets posted by himself, order by timestamp from most recent to least recent.
3. getNewsFeed(user_id). Get the given user's most recently 10 tweets in his news feed (posted by his friends and himself). Order by timestamp from most recent to least recent.
4. follow(from_user_id, to_user_id). from_user_id followed to_user_id.
5. unfollow(from_user_id, to_user_id). from_user_id unfollowed to to_user_id.

Example
    postTweet(1, "LintCode is Good!!!")
    >> 1
    getNewsFeed(1)
    >> [1]
    getTimeline(1)
    >> [1]
    follow(2, 1)
    getNewsFeed(2)
    >> [1]
    unfollow(2, 1)
    getNewsFeed(2)
    >> []
"""
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
         pass

class MiniTwitter:

    def __init__(self):
        # do intialization if necessary
        self.order = 0
        self.follows = {}
        self.timeline = {}
    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        # write your code here
        t = Tweet.create(user_id, tweet_text)
        self.order += 1
        # self.tweets.append(t)
        
        if user_id not in self.timeline:
            self.timeline[user_id] = [(self.order, t)]
        else:
            self.timeline[user_id].append((self.order, t))
        return t
        
    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
        # write your code here
    def getNewsFeed(self, user_id):
        res = []
        if user_id in self.timeline:
            res = self.timeline[user_id][-10:]
        # print(self.tweets, user_id)
        if user_id in self.follows:
            for f in self.follows[user_id]:
                if f in self.timeline:
                    res.extend(self.timeline[f][-10:])
        
        res.sort(key = lambda x : x[0])
        return [tweet[1] for tweet in res[-10:][::-1]]
        
    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        # write your code here
        # print(user_id, self.timelines)
        # print(self.timelines)
        if user_id in self.timeline:
            return [tweet[1] for tweet in self.timeline[user_id][-10:][::-1]]
        return []
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id not in self.follows:
            self.follows[from_user_id] = []
        self.follows[from_user_id].append(to_user_id)
    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        # write your code here
        if from_user_id in self.follows:
            self.follows[from_user_id].remove(to_user_id)
