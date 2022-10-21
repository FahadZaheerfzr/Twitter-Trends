# Import Libraries
import tweepy 
## import csv 
import sys 
import config
## Preprocessing 
import pandas as pd 
from langdetect import detect

# initialize api instance
consumer_key= config.consumer_key 
consumer_secret= config.consumer_secret 
access_token=config.access_token 
access_token_secret =config.access_token_secret 

#Connect to Twitter through the API 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth,wait_on_rate_limit=True)


def get_woeid(place):
    '''Get woeid by location'''
    try:
        trends = api.available_trends()
        for val in trends:
            if (val['name'].lower() == place.lower()):
                return(val['woeid']) 
        print('Location Not Found')
    except Exception as e:
        print('Exception:',e)
        return(0)
      
           
get_woeid('Pakistan')