-- script that converts hbtn_0c_0 database to UTF8
-- (utf8mb4, collate utf8mb4_unicode_ci)
-- displays teh average temp by city
-- ordered by temperature desc

SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
