#importing of libraries
from ast import keyword
from distutils.command.config import config
import tweepy
import pandas as pd
import configparser

# read configs
config                    = configparser.ConfigParser()
config.read('config.ini')

api_key                   = config['twitter']['api_key']
api_key_secret            = config['twitter']['api_key_secret']

access_token              = config['twitter']['access_token']
access_token_secret       = config['twitter']['access_token_secret']

#authentication
auth                      = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api                       = tweepy.API(auth)

#search tweets
keywords                  = "Ghana's inflation" 
limit                     = 2000

tweets                    =tweepy.Cursor(api.search_tweets, q=keywords, lang="en",).items(2000)

#create DataFrame
columns                   =['User_ID', 'Name', 'Username', 'Tweet_Date', 'Tweet_language', 'Tweet_text', 'Bio']
data                      =[]


for tweet in tweets:
    data.append([str(tweet.user.id),str(tweet.user.name),str(tweet.user.screen_name), str(tweet.created_at), str(tweet.lang),str(tweet.text), str(tweet.user.description)])
    
df                        = pd.DataFrame(data, columns=columns
)

print(df)
df.to_csv('inflationGhana.csv')