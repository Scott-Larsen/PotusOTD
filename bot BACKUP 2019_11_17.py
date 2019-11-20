# from generate_advertisement import get_ad
import tweepy, credentials, datetime

INTERVAL = 60 * 60 * 6  # tweet every 6 hours
# INTERVAL = 15  # every 15 seconds, for testing

auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
api = tweepy.API(auth)

username = 'potus'
startDate = datetime.datetime(2018, 11, 17, 0, 0, 0)
endDate =   datetime.datetime(2018, 11, 18, 0, 0, 0)

tweets = []
tmpTweets = api.user_timeline(username)

for tweet in tmpTweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet)

while (tmpTweets[-1].created_at > startDate):
    tmpTweets = api.user_timeline(username, max_id = tmpTweets[-1].id)
    for tweet in tmpTweets:
        if tweet.created_at < endDate and tweet.created_at > startDate:
            tweets.append(tweet)

print(tweets)

# account_list = [@potus]
# if len(account_list) > 0:
#   for target in account_list:
#     print("Getting data for " + target)
#     item = auth_api.get_user(target)
#     print("name: " + item.name)
#     print("screen_name: " + item.screen_name)
#     print("description: " + item.description)
#     print("statuses_count: " + str(item.statuses_count))
#     print("friends_count: " + str(item.friends_count))
#     print("followers_count: " + str(item.followers_count))

# #Send Tweet Out
# # while True:
# print("about to get tweet...")
# # ad = get_ad()
# tweet = "test"
# api.update_status(tweet)
# # time.sleep(INTERVAL)