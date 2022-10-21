# Import Libraries
import tweepy 
## import csv 
import config

## Preprocessing 
import pandas as pd 
from langdetect import detect
import iso639

from googletrans import Translator  # Import Translator module from googletrans package

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
      

def get_trends_by_location(loc_id,count):
    '''Get Trending Tweets by Location'''
    
    try:
        trends = api.get_place_trends(loc_id)
        df = pd.DataFrame([trending['name'],  trending['tweet_volume'], iso639.to_name(detect(trending['name']))] for trending in trends[0]['trends'])
        df.columns = ['Trends','Volume','Language']
        return(df[:count])
    except Exception as e:
        print("An exception occurred",e)


def get_translation(text):
    ''' Translate text in English'''
    try:
        translator = Translator() # Create object of Translator.
        translated = translator.translate(text,dest='en')
        return(translated.text)
    except Exception as e:
        print("Exception", e)


locationID = get_woeid('Pakistan')

trends = get_trends_by_location(locationID,10)


trends['Trends'] = [get_translation(trend) for trend in trends['Trends']]

print(trends)