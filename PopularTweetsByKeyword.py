import tweepy
from tweepy import OAuthHandler


def popular(keyword):
    # from twitter app id
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_secret = ""
    # initializing contact point (api variable)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    for tech in api.search(keyword, result_type="popular", tweet_mode="extended"):
        # to print more than 140 chars, use tweet_mode=extended and .full_text
        print(tech.user.screen_name, end="")
        if(tech.user.verified):
            print(" ✓: ", end="")
        print(tech.full_text)
        print()


if __name__ == "__main__":
    keyword = input("Please enter the keyword to search for: ")
    popular(keyword)
