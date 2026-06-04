-- Bottom 10 States

SELECT Location,
AVG(CAST("Data Value" AS REAL)) AS Avg_Diabetes
FROM diabetes_data
WHERE "Short Indicator Text"='Diabetes Prevalence'
AND "Data Type"='Age-adjusted Rate (per 100)'
GROUP BY Location
ORDER BY Avg_Diabetes ASC
LIMIT 10;


-- National Average

SELECT ROUND(
AVG(CAST("Data Value" AS REAL)),2
) AS National_Average
FROM diabetes_data
WHERE "Short Indicator Text"='Diabetes Prevalence'
AND "Data Type"='Age-adjusted Rate (per 100)';


-- High Risk States

SELECT Location,
AVG(CAST("Data Value" AS REAL)) AS Avg_Diabetes
FROM diabetes_data
WHERE "Short Indicator Text"='Diabetes Prevalence'
AND "Data Type"='Age-adjusted Rate (per 100)'
GROUP BY Location
HAVING Avg_Diabetes > 12
ORDER BY Avg_Diabetes DESC;