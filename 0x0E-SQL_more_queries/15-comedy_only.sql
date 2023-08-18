-- lists all comedy showsb>n the database
SELECT title FROM tv_shows
LEFT JOIN tv_show_genres
NATURAL JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
AND tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC;
