-- Top 10 States

SELECT Location,
AVG([Data Value]) AS Avg_Diabetes
FROM diabetes_data
GROUP BY Location
ORDER BY Avg_Diabetes DESC
LIMIT 10;


-- Bottom 10 States

SELECT Location,
AVG([Data Value]) AS Avg_Diabetes
FROM diabetes_data
GROUP BY Location
ORDER BY Avg_Diabetes ASC
LIMIT 10;


-- National Average

SELECT AVG([Data Value]) AS National_Average
FROM diabetes_data;


-- Highest Diabetes State

SELECT Location,
MAX([Data Value]) AS Highest_Rate
FROM diabetes_data
GROUP BY Location
ORDER BY Highest_Rate DESC
LIMIT 1;


-- Lowest Diabetes State

SELECT Location,
MIN([Data Value]) AS Lowest_Rate
FROM diabetes_data
GROUP BY Location
ORDER BY Lowest_Rate ASC
LIMIT 1;