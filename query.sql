-- Showing the first 10 rows to get an idea of the table formatting
SELECT * 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
LIMIT 10;

-- Using ORDER BY: to list all the movies in alphabetical order
SELECT title, type, country 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
ORDER BY title;

SELECT release_year,
    COUNT(release_year) AS release_count 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE type='Movie' 
GROUP BY release_year 
ORDER BY release_count DESC;

-- Using WHERE: to show all the movies and names where they are rated G NOTE: doesnt include tv shows because it uses a different rating code.
SELECT title, rating 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE rating='G';

SELECT title, rating 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE rating='TV-MA';

-- Using IN: to list all movies that have country data set to Norway & ones where the data is missing and was replaced by our functions earlier
SELECT title, country 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE country IN ('Norway');

SELECT title, country 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE country IN ('NULL');

-- Using LIKE: to list movies where the cast includes John Wayne and directors that include the name Scorsese (just gives Martin)
SELECT title, `cast` 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE `cast` LIKE '%John Wayne%';

SELECT title, director 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE director LIKE '%Scorsese%';

-- Using COUNT & GROUP BY: to list movies ratings count & country count to see occurances of each
SELECT rating, COUNT(rating) AS rating_count 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
GROUP BY rating 
ORDER BY rating_count DESC;

SELECT country, COUNT(country) AS country_count 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
GROUP BY country 
ORDER BY country_count DESC;

-- Using MAX: to show the most recent year on netflix that has Robert De Niro listed in the cast
SELECT Max(release_year) AS max_release 
FROM `deb-01-346121.netflix_titles.netflix_titles` 
WHERE `cast` LIKE '%Robert De Niro%';