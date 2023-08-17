-- Lists all shows contained in hbtn_0d_tvshows to genre_id
-- And title
SELECT title, genre_id
FROM tv_shows INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;
