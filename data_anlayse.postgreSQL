--- Top 12 Users Who USED Thier Phones ; 
SELECT "User_ID",
	"Daily_Phone_Hours"
FROM public.data_anlayse 
ORDER BY "Daily_Phone_Hours" DESC 
FETCH FIRST 12 ROWS ONLY ;

--- Average_work_productivity Depending on Device_Type and Job ;
SELECT AVG ("Work_Productivity_Score") as AVERAGE ,
	"Device_Type" ,
	"Occupation"
FROM public.data_anlayse
GROUP BY "Device_Type" , "Occupation"
ORDER BY AVERAGE DESC;

--- Average Sleep_Hours Depending on the Job;
SELECT "Occupation" ,
	avg ("Sleep_Hours") as sleep
FROM public.data_anlayse 
GROUP BY "Occupation";

--- if social media hours increased what's the impact on the work productivity;
SELECT 
CASE
WHEN "Social_Media_Hours" >= 0 AND 2 >= "Social_Media_Hours" THEN 'low'
WHEN "Social_Media_Hours" >= 2 AND 4 >= "Social_Media_Hours" THEN 'med' 
WHEN "Social_Media_Hours" >= 4 THEN 'high' 
END as ratings,
count(*) as Num_of_Users,
	round(avg("Work_Productivity_Score"),2) as avg_productivity
FROM public.data_anlayse
GROUP by ratings;

---sleep hours relation with stress levels;
SELECT 
CASE
WHEN "Sleep_Hours" <=4 THEN 'very low'
WHEN "Sleep_Hours" <=6 And "Sleep_Hours" > 4 THEN 'low'
WHEN "Sleep_Hours" <=8 And "Sleep_Hours" > 6 THEN 'med'
WHEN "Sleep_Hours" > 8 THEN 'good'
END as sleep,
 avg("Stress_Level") as avg_stress,
 ROUND(STDDEV("Stress_Level"),2) AS stress_stddev,
 count(*) as num_of_Users
from public.data_anlayse
GROUP by sleep;

--- Caffiene intake and it's affect on average sleep_hours;
SELECT 
CASE 
	WHEN "Caffeine_Intake_Cups" <= 1 THEN 'FINE'
	WHEN "Caffeine_Intake_Cups" <= 2 AND "Caffeine_Intake_Cups" > 1 THEN 'NORMAL'
	WHEN "Caffeine_Intake_Cups" <= 3 AND "Caffeine_Intake_Cups" > 2 THEN 'ABOVE NORMAL'
	WHEN "Caffeine_Intake_Cups" <= 4 AND "Caffeine_Intake_Cups" > 3 THEN 'DANGER'
	WHEN "Caffeine_Intake_Cups" <= 5 AND "Caffeine_Intake_Cups" > 4 THEN 'RIKSY'
	WHEN "Caffeine_Intake_Cups" > 5  THEN 'SUPER_RISKY'
END AS CAFFEINE,
	AVG("Sleep_Hours") as avg_sleep,
	ROUND(STDDEV("Sleep_Hours"),2) AS stress_stddev, 
	COUNT(*) AS NUMBERR
FROM public.data_anlayse
group by CAFFEINE;

--- Which age_genre Uses the Phone more;
WITH age_groups AS (SELECT 
CASE 
	WHEN "Age" <= 20 THEN 'young'
	WHEN "Age" <= 30 AND "Age" > 20 THEN 'adults'
	WHEN "Age" <= 40 AND "Age" > 30 THEN 'elders'
	else 'old'
	end as ages_genre,
	count(*) as numpeople,
	AVG("Daily_Phone_Hours") AS AVG_HOURS
FROM public.data_anlayse
group by ages_genre),
ranked AS (SELECT ages_genre  , AVG_HOURS ,
DENSE_RANK() OVER(order by AVG_HOURS DESC) AS RN
FROM age_groups
) 
SELECT RN , ages_genre , AVG_HOURS
FROM ranked
WHERE RN = 1 ;

--- Device_Type affect on work_productivity and Screen_Time;
SELECT "Device_Type",CASE
WHEN "Device_Type" = 'Android' THEN CORR ("Work_Productivity_Score","Daily_Phone_Hours")
ELSE CORR ("Work_Productivity_Score","Daily_Phone_Hours")
END AS RELATION,
avg("Daily_Phone_Hours") AS avgdaily,
avg("Work_Productivity_Score")as workavg
FROM public.data_anlayse
GROUP BY "Device_Type";

-- Top 5 users with highest stress, highest productivity, and highest phone usage 
WITH top_work AS (
    SELECT 
        "User_ID",
        "Work_Productivity_Score" AS value,
        'Work_Productivity' AS category,
        ROW_NUMBER() OVER (ORDER BY "Work_Productivity_Score" DESC) AS rank
    FROM public.data_anlayse),
	
top_stress AS (SELECT "User_ID",
        "Stress_Level" AS value,
        'Stress_Level' AS category,
        ROW_NUMBER() OVER (ORDER BY "Stress_Level" DESC) AS rank
    FROM public.data_anlayse),
	
top_use AS (SELECT "User_ID",
        "Daily_Phone_Hours" AS value,
        'Phone_Usage' AS category,
        ROW_NUMBER() OVER (ORDER BY "Daily_Phone_Hours" DESC) AS rank
    FROM public.data_anlayse)
	
SELECT * FROM top_work where rank <= 5 
UNION all
SELECT * FROM top_stress where rank <=5
UNION all
SELECT * FROM top_use WHERE rank <= 5
order by value,category;

---info about each person;
create VIEW general_info AS SELECT "User_ID",
	"Daily_Phone_Hours",
	"Social_Media_Hours",
	"Stress_Level",
	"Work_Productivity_Score",
	case 
	when "Sleep_Hours" <= 4 then 'low'
	when "Sleep_Hours" <=6 AND "Sleep_Hours" > 4 then 'med'
	ELSE 'good'
	end as sleep_rate,
	case 
	when "Caffeine_Intake_Cups" <= 2 then 'normal'
	when "Caffeine_Intake_Cups" <=4 AND "Caffeine_Intake_Cups" > 2 then 'high'
	else 'danger'
	end as caffeine_rate 
from public.data_anlayse;
SELECT * FROM general_info;

