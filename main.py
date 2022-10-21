# Import Libraries
import tweepy 
## import csv 
import config

## Preprocessing 
import pandas as pd 
from langdetect import detect

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
    '''This function returns the WOEID of a place'''
    try:
        # Get the available trends
        trends = api.available_trends()
        # Match the place with the trends location
        for val in trends:
            if (val['name'].lower() == place.lower()):
                return(val['woeid']) 
        print('Location Not Found')
    except Exception as e:
        print('Exception:',e)
        return(0)
      

def get_trends_by_location(loc_id,count):
    '''This function returns the top trends of a location'''
    
    try:
        # Get the trends
        trends = api.get_place_trends(loc_id)
        # Get the trends list
        df = pd.DataFrame([trending['name'],  trending['tweet_volume']] for trending in trends[0]['trends'])
        df.columns = ['Trends','Volume']
        return(df[:count])
    except Exception as e:
        print("An exception occurred",e)


def get_translation(text):
    ''' Translate text in English'''
    try:
        translator = Translator(service_urls=['translate.googleapis.com']) # Create object of Translator.
        translated = translator.translate(text)
        return(translated.text)
    except Exception as e:
        print("Exception", e)

# Get the WOEID of the Pakistan
locationID = get_woeid('Pakistan')

# Get the top 15 trends of Pakistan
df_world_trends = get_trends_by_location(locationID,15)
# Translate the trends in English
df_world_trends["Translated_Trends"] = [get_translation(val) for val in df_world_trends.Trends] 
# Display the trends
print(df_world_trends)