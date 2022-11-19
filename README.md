# django_testovoe
В корне docker-compose up
xhionity/django_testovoe

#sql 1
SELECT brand.title AS title, COUNT(SELECT notebook.title FROM notebook, brand WHERE brand.title IN notebook.title) AS count
FROM brand, notebooks
GROUP BY title
ORDER BY count DESC


#sql 2
SELECT ROUND(width, 0) AS width n, ROUND(depth, 0) AS depth n, ROUND(height, 0) AS height n, COUNT(*) AS count n
FROM notebook
GROUP BY width n, depth n, height n
ORDER BY width n
IF width n % 5 != 0 THEN
ROUND(width n, -1)
IF depth n % 5 != 0 THEN
ROUND(depth n, -1)
IF height % 5 != 0 THEN
ROUND(height n, -1)
