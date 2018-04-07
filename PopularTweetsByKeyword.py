def popular(keyword):
    #importing tweepy to connect to twitter
    import tweepy
    from tweepy import OAuthHandler
    #from twitter app id
    consumer_key=""
    consumer_secret=""
    access_token=""
    access_secret=""
    #initializing contact point (api variable)
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    api=tweepy.API(auth)
    
    for tech in api.search(keyword,result_type="popular",tweet_mode="extended"):
        print(tech.user.screen_name,end="")  #to print more than 140 chars, use 
        if(tech.user.verified):              #tweet_mode=extended and .full_text
            print(" ✓: ",end="")
        print(tech.full_text)        
        print()                    