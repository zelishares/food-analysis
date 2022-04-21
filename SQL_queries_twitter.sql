---------------------------------------------
-- analysis of tasty_twitter and  tasty_twitter_history databases

select Count(*)
from tasty_twitter_history; --3252

select count(*)
from tasty_twitter; --600

select count(*)
from twitter_hashtags; --1161

select count (tweet)
from tasty_twitter
where tweet like '%Shop the recipe%'; --259

select count (tweet)
from tasty_twitter_history
where tweet like '%Shop the recipe%'; --1575

select additional_information  ->> 'hashtags' AS hashtags 
from tasty_twitter_history
where additional_information  ->> 'hashtags' not like '[]'; -- only 4 hashtags were used

select additional_information  ->> 'hashtags' AS hashtags 
from tasty_twitter
where additional_information  ->> 'hashtags' not like '[]'; -- no hashtags were used

select avg(count) 
from tasty_twitter; -- 37

select avg(count) 
from tasty_twitter_history; -- 48

select avg(favorites) 
from tasty_twitter; -- 157.91

select avg(favorites) 
from tasty_twitter_history; -- 209.7

---------------------------------------------
-- analysis of hashtag databases

select count(*)
from twitter_hashtags; --1161

select count(additional_information  ->> 'hashtags')
from twitter_hashtags
where additional_information  ->> 'hashtags' not like '[]'; -- only 189 contain hashtags

select count(tweet)
from twitter_hashtags 
where tweet like '%vegan%' --276 contain word vegan 

select count(tweet)
from twitter_hashtags 
where tweet like '%foodie%' --42 contain word foodie 

select count(tweet)
from twitter_hashtags 
where tweet like '%foodporn%' --2 contain word foodporn

select tweet
from twitter_hashtags 
where tweet like '%foodlover%' --0 contain word vegan 

select avg(count) 
from twitter_hashtags; -- 518

select avg(favorites) 
from twitter_hashtags; -- 167.8

select additional_information
from tasty_twitter_history

select additional_information  ->> 'hashtags' AS url 
from tasty_twitter_history
where additional_information  ->> 'hashtags' not like '[]'; 

