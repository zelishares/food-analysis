import json
import pandas as pd
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
BEARER_TOKEN= os.environ['BEARER_TOKEN']


def lambda_handler(event, context):
    
    # building connection to twitter api
    try:
        # Creating the authentication object
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        # Setting your access token and secret
        auth.set_access_token(ACCESS_TOKEN, ACCES_TOKEN_SECRET)
        # Creating the API object while passing in auth information
        api = tweepy.API(auth) 
    
    except:
        print('Error: Problem with twitter connection')
        
    # fetching tweets from the api
    result = api.user_timeline(screen_name='tasty', count = 250)
    
    # append the tweets to a list
    tweet_list_tasty = []
    for tweets in result:
        tweet_list_tasty.append([tweets.text,
        tweets.created_at.date(),
        tweets.favorite_count,
        tweets.retweet_count,
        tweets.entities])
    
    # putting the tweets into a df
    df_tasty = pd.DataFrame(tweet_list_tasty, columns=["tweet", "created", "favorites", "count",'additional_information'])
    
    #enable datatype of additional_ifnormation to be in json form
    df_tasty['additional_information'] = df_tasty['additional_information'].apply(json.dumps)
    
    
    # building connection to database
    try:
        print("host={} dbname={} user={} password={}".format(ENDPOINT, DB_NAME, USERNAME, PASSWORD))
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

    
    #creating table if not existent
    conn.set_session(autocommit=True)
    cur.execute("CREATE TABLE IF NOT EXISTS tasty_twitter (tweet TEXT, created DATE, favorites INT, count INT, additional_information jsonb);")
  
    #adding the df into the database
    df_tasty.to_sql('tasty_twitter', engine, if_exists = 'append', index = False)
    
    #close the connections
    cur.close()
    conn.close()
   
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')}
