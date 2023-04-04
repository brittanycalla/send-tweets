# this program will send a tweet to twitter
# import the tweepy library
import tweepy

# import config file
import config

# create client with tweepy.Client consumer key, consumer secret, access token, access token secret as arguments
client = tweepy.Client(
    consumer_key = config.CONSUMER_KEY,
    consumer_secret = config.CONSUMER_KEY_SECRET,
    access_token = config.ACCESS_TOKEN,
    access_token_secret = config.ACCESS_TOKEN_SECRET
)

# create a variable with the text to tweet "I wrote this tweet with Copilot - thank you @blackgirlbytes!"
tweet = "I wrote this tweet with Copilot - thank you @blackgirlbytes!"

# send the tweet
response = client.create_tweet(text = tweet)

# print response
print(response)