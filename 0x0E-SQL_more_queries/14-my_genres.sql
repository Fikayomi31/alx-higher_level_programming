-- list all the genres of the show Dexter
SELECT name FROM tv_shows
LEFT JOIN tv_show_genres
NATURAL JOIN tv_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
AND tv_genres.id = tv_show_genres.genre_id
ORDER BY name ASC;
