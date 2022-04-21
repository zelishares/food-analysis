import json
import pandas as pd
import numpy as np
import requests
import psycopg2
import os
import sqlalchemy
import tweepy

#database credentials
ENDPOINT = os.environ['ENDPOINT']
DB_NAME = os.environ['DB_NAME']
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

#twitter credentials
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCES_TOKEN_SECRET = os.environ['ACCES_TOKEN_SECRET']
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

def lambda_handler(event, context):
    
    # building connection to twitter api
    try:
        # Creating the authentication object
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        # Setting your access token and secret
        auth.set_access_token(ACCESS_TOKEN, ACCES_TOKEN_SECRET)
        # Creating the API object while passing in auth information
        api = tweepy.API(auth, wait_on_rate_limit = True) 
    
    except:
        print('Error: Problem with twitter connection')
        
    # defining the language of the tweets
    language = 'en'
        
    # list which is appended with the fetch tweets
    tweet_list_hashtags = []
    
    # defining the keywords for the search
    query = "recipe OR foodporn OR foodie OR foodlover OR vegan"
    
    # defining an empty list to append for the results
    tweet_list_hashtags= []
    
    # gets the result of the query and appends it to the tweet_list_hashtags list
    for tweets in tweepy.Cursor(api.search_tweets, q=query, lang=language, result_type= 'mixed').items(500):
        tweet_list_hashtags.append([tweets.text,
                             tweets.created_at.date(),
                             tweets.favorite_count,
                             tweets.retweet_count,
                             tweets.entities])
        
    # creating a pandas dataframe out of the list
    df_hashtags = pd.DataFrame(tweet_list_hashtags, columns=["tweet", "created", "favorites", "count",'additional_information'])
    
    #allowing the 'additional_information' to have json as a datatype
    df_hashtags['additional_information'] = df_hashtags['additional_information'].apply(json.dumps)
    
    
    #making a connection to the database
    try:
        conn = psycopg2.connect("host={} dbname={} user={} password={}".format(ENDPOINT, DB_NAME, USERNAME, PASSWORD))
    
    except psycopg2.Error as e:
        print("Error: Could not make connection to the Postgres database")
        print(e)
    
    try:
        cur = conn.cursor()
    
    except psycopg2.Error as e:
        print("Error: Could not get curser to the Database")
        print(e)
    
    # Create sqlalchemy engine
    engine = sqlalchemy.create_engine("postgresql://{}:{}@{}:5432/{}".format(USERNAME,PASSWORD,ENDPOINT,DB_NAME))
    
    conn.set_session(autocommit=True)
    
    #tests if the table exists or creats a new one
    cur.execute("CREATE TABLE IF NOT EXISTS twitter_hashtags (tweet TEXT, created DATE, favorites INT, count INT, additional_information jsonb);")
    
    #putting the data from the dataframe into the database
    df_hashtags.to_sql('twitter_hashtags', engine, if_exists = 'append', index = False)
    
    #close the connection
    cur.close()
    conn.close()
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
