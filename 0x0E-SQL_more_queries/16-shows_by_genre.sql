-- list all shows and genres linked to the show
-- from the database
SELECT title, name FROM tv_shows
LEFT JOIN tv_show_genres
NATURAL JOIN tv_genres
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NULL
OR tv_show_genres.genre_id = tv_genres.id
ORDER BY title, name ASC;
