# Write your MySQL query statement below
SELECT 
    contest_id, 
    ROUND(COUNT(user_id) * 100.0 / total.user_count, 2) AS percentage
FROM 
    Register
CROSS JOIN 
    (SELECT COUNT(*) AS user_count FROM Users) total
GROUP BY 
    contest_id
ORDER BY 
    percentage DESC, 
    contest_id ASC;
