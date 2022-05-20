-- Showing the first 10 rows to get an idea of the table formatting
SELECT * FROM `deb-01-346121.netflix_titles.netflix_titles` LIMIT 10;

-- Using ORDER BY: to list all the movies in alphabetical order
SELECT title, type, country FROM `deb-01-346121.netflix_titles.netflix_titles` ORDER BY title;

-- Using WHERE: to show all the movies and names where they are rated G NOTE: doesnt include tv shows because it uses a different rating code.
SELECT title, rating FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE rating='G';
SELECT title, rating FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE rating='TV-MA';

-- Using IN: to list all movies that have country data set to Norway & ones where the data is missing and was replaced by our functions earlier
SELECT title, country FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE country IN ('Norway');
SELECT title, country FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE country IN ('NULL');

-- Using LIKE: to list movies where the cast includes John Wayne and directors that include the name Scorsese (just gives Martin)
SELECT title, `cast` FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE `cast` LIKE '%John Wayne%';
SELECT title, director FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE director LIKE '%Scorsese%';