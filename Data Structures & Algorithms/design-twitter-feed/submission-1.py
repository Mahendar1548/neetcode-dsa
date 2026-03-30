import heapq


class Twitter:

    def __init__(self):
        self.tweet_counter = -1
        self.user_wise_following_list = defaultdict(set)
        self.user_wise_posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_wise_posts[userId].append(
            (self.tweet_counter, tweetId))
        self.tweet_counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.user_wise_following_list[userId].add(userId)
        user_posts_to_fetch = list(self.user_wise_following_list[userId])
        all_post_to_consider = []
        for user in user_posts_to_fetch:
            all_post_to_consider.extend(self.user_wise_posts[user])

        heapq.heapify(all_post_to_consider)
        posts = []
        for i in range(10):
            if all_post_to_consider:
                posts.append(heapq.heappop(all_post_to_consider)[1])

        return posts


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_wise_following_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_wise_following_list[followerId].remove(followeeId)

