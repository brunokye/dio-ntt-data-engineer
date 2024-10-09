SELECT * FROM Album a;
SELECT COUNT(*) AS Records FROM Album a;

SELECT COUNT(*) FROM Album a WHERE Column1 IS NOT NULL;
SELECT AlbumId, Title FROM Album a WHERE Column1 is NULL;


SELECT * FROM Artist a;

SELECT a2.ArtistId, a2.Name, COUNT(*) AS Records
FROM Album a
INNER JOIN Artist a2 ON a.ArtistId = a2.ArtistId
GROUP BY a2.ArtistId, a2.Name;
