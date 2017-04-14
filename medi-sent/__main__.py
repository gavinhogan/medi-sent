
from tweepy import API, OAuthHandler

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""


def main():
    print("Hello World")
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = API(auth)
    tweets = api.search("EllisMedicine")
    #print(tweets)
    for tweet in tweets:
        print(tweet.author.screen_name)
        print(tweet.text)

if __name__ == "__main__":
    main()
