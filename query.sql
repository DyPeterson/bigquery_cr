-- Showing the first 10 rows to get an idea of the table formatting
SELECT * FROM `deb-01-346121.netflix_titles.netflix_titles` LIMIT 10;
-- Using WHERE: to show all the movies and names where they are rated G NOTE: doesnt include tv shows because it uses a different rating code.
SELECT title, rating FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE rating='G';
SELECT title, rating FROM `deb-01-346121.netflix_titles.netflix_titles` WHERE rating='TV-MA';
-- Using ORDER BY: