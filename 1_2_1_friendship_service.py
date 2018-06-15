"""
Support follow & unfollow, getFollowers, getFollowings.

Example
    follow(1, 3)
    getFollowers(1) // return [3]
    getFollowings(3) // return [1]
    follow(2, 3)
    getFollowings(3) // return [1,2]
    unfollow(1, 3)
    getFollowings(3) // return [2]
"""


class FriendshipService:
    
    def __init__(self):
        # initialize your data structure here.
        self.followers = dict()
        self.followings = dict()

        
    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowers(self, user_id):
        # Write your code here
        if user_id not in self.followers:
            return []
        results = list(self.followers[user_id])
        results.sort()
        return results

    # @param {int} user_id
    # return {int[]} all followers and sort by user_id
    def getFollowings(self, user_id):
        # Write your code here
        if user_id not in self.followings:
            return []
        results = list(self.followings[user_id])
        results.sort()
        return results
        
    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id not in self.followers:
            self.followers[from_user_id] = set()
        self.followers[from_user_id].add(to_user_id)

        if to_user_id not in self.followings:
            self.followings[to_user_id] = set()
        self.followings[to_user_id].add(from_user_id)

    # @param {int} from_user_id
    # @param {int} to_user_id
    # from_user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id in self.followers:
            if to_user_id in self.followers[from_user_id]:
                self.followers[from_user_id].remove(to_user_id)

        if to_user_id in self.followings:
            if from_user_id in self.followings[to_user_id]:
                self.followings[to_user_id].remove(from_user_id)