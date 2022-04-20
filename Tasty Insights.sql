-- check if there are no duplicates
SELECT id, name, COUNT(id) FROM tasty
GROUP BY id, name
HAVING COUNT(id) >1;

-- Number of entries in the db
SELECT COUNT(*) FROM tasty; -- 816

-- Number of recipes with most important info
SELECT * FROM tasty
WHERE name IS NOT NULL
AND user_ratings_count_positive IS NOT NULL
AND user_ratings_count_negative IS NOT NULL
AND user_ratings_score IS NOT NULL
AND tags IS NOT NULL
AND instructions IS NOT NULL
AND sections IS NOT NULL; --782

-- Average of score and ratings
select avg(user_ratings_count_positive) 
from tasty; -- 330

select avg(user_ratings_count_negative) 
from tasty; -- 27

select avg(user_ratings_score) 
from tasty; -- 0.85

-- Average calories in recipes
select avg(nutrition_calories) 
from tasty; -- 530

-- count number of null values per column
SELECT COUNT(*)-COUNT(name) AS name,
	COUNT(*)-COUNT(original_video_url) AS video,
	COUNT(*)-COUNT(topics) AS topics,
	COUNT(*)-COUNT(keywords) AS keywords,
	COUNT(*)-COUNT(tags) AS tags,
	COUNT(*)-COUNT(num_servings) AS num_servings,
	COUNT(*)-COUNT(total_time_minutes) AS total_time_minutes,
	COUNT(*)-COUNT(yields) AS yields,
	COUNT(*)-COUNT(country) AS country,
	COUNT(*)-COUNT(tips_and_ratings_enabled) AS tips,
	COUNT(*)-COUNT(aspect_ratio) AS aspect_ratio,
	COUNT(*)-COUNT(sections) AS sections,
	COUNT(*)-COUNT(instructions) AS instructions,
	COUNT(*)-COUNT(prep_time_minutes) AS prep_time_minutes,
	COUNT(*)-COUNT(description) AS description,
	COUNT(*)-COUNT(cook_time_minutes) AS cook_time_minutes,
	COUNT(*)-COUNT(nutrition_fiber) AS nutrition_fiber,
	COUNT(*)-COUNT(nutrition_protein) AS nutrition_protein,
	COUNT(*)-COUNT(nutrition_fat) AS nutrition_fat,
	COUNT(*)-COUNT(nutrition_calories) AS nutrition_calories,
	COUNT(*)-COUNT(nutrition_sugar) AS nutrition_sugar,
	COUNT(*)-COUNT(nutrition_carbohydrates) AS nutrition_carbohydrates,
	COUNT(*)-COUNT(user_ratings_count_positive) AS user_ratings_positive,
	COUNT(*)-COUNT(user_ratings_score) AS user_ratings_score,
	COUNT(*)-COUNT(user_ratings_count_negative) AS user_ratings_negative,
	COUNT(*)-COUNT(total_time_tier_display_tier) AS total_time_tier
FROM tasty; 

-- count number of recipes with positive = 0
SELECT user_ratings_count_positive, COUNT(user_ratings_count_positive) from tasty
WHERE user_ratings_count_positive = 0
GROUP BY user_ratings_count_positive;

-- count number of recipes with negative = 0
SELECT user_ratings_count_negative, COUNT(user_ratings_count_negative) from tasty
WHERE user_ratings_count_negative = 0
GROUP BY user_ratings_count_negative;
