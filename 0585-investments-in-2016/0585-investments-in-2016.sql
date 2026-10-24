# Write your MySQL query statement below
WITH PolicyMetrics AS (
    SELECT 
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS count_2015,
        COUNT(*) OVER(PARTITION BY lat, lon) AS count_loc
    FROM Insurance
)
SELECT 
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM PolicyMetrics
WHERE count_2015 > 1 AND count_loc = 1;
