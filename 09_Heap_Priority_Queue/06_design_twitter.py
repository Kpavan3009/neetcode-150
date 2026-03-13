"""
Problem: Design Twitter (LeetCode #355)
Difficulty: Medium

CLARIFYING QUESTIONS:
- getNewsFeed returns 10 most recent tweets from user + followees? (Yes)
- User implicitly follows themselves? (Yes)
- Tweets have unique IDs? (Yes, each tweet gets a unique timestamp)

APPROACH / PSEUDOCODE:
- Store tweets per user as list of (timestamp, tweetId), most recent first
- Store followees in a set per user
- getNewsFeed: merge-k-sorted-lists using a max-heap
    - Start with latest tweet from each followee (including self)
    - Pop max, add next tweet from same user

Time Complexity: postTweet O(1), getNewsFeed O(F log F + 10 log F) where F = followees
Space Complexity: O(users * tweets)
"""

import heapq
from collections import defaultdict


class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)  # userId -> [(timestamp, tweetId)]
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list:
        followees = self.following[userId] | {userId}
        heap = []

        for uid in followees:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                ts, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts, tid, uid, idx - 1))

        result = []
        while heap and len(result) < 10:
            ts, tid, uid, idx = heapq.heappop(heap)
            result.append(tid)
            if idx >= 0:
                nts, ntid = self.tweets[uid][idx]
                heapq.heappush(heap, (-nts, ntid, uid, idx - 1))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Test cases
if __name__ == "__main__":
    tw = Twitter()
    tw.postTweet(1, 5)
    print(tw.getNewsFeed(1))  # [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    print(tw.getNewsFeed(1))  # [6, 5]
    tw.unfollow(1, 2)
    print(tw.getNewsFeed(1))  # [5]
