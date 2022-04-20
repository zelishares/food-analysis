# food-analysis
This gitHub repository contains the code of the group NoName for the group work in the modul Data Warehouse and Data Lake System. The following files are included:

## Twitter API
1. Lamda_tasty_twitter_fetch.zip --- which contains the python code for the lamda function that fetches data from the twitter user tasty
2. Lamda_tasty_twitter_fetch.ymal --- which contains the same code as 1 in a different format
3. lamda_twitter_tweets.zip --- contains the python code for the lambda function that fetches keywords from twitter
4. lamda_twitter_tweets.ymal --- which contains the same code as 1 in a different format

## Tasty API
1. Get data from Tasty API for first insights.ipynb --- This Jupyter Notebook was used to gain first insights about the Tasty API (tags, etc.)
2. AWS Tasty Lambda_cuisine.ipynb --- A Jupyter Notebook file which contains the python code for the aws lambda function that fetches data for all cuisine tags from the Tasty API.
3. AWS Tasty Lambda_diet.ipynb  --- A Jupyter Notebook file which contains the python code for the aws lambda function that fetches data for all diet tags from the Tasty API.
4. Tasty Insights.sql --- SQL Queries for first data analysis

## MyFoodData csv
1. lambda_MyFoodData.yaml --- Lamda function exported from AWS
12. Nutrition Facts MyFoodData.ipynb --- A Jupiter Notebook file wich contains the python code whchich served as a basis for the lambda function that fetches an Excel from MyFoodData.com with nutrition information of food
