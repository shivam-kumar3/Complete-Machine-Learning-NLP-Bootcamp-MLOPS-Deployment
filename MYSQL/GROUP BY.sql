-- GROUP BY 


SELECT *
FROM employee_demographics;


SELECT GENDER
FROM employee_demographics
group by GENDER;

SELECT GENDER, AVG(AGE)
FROM employee_demographics
GROUP BY GENDER;

SELECT * 
FROM employee_salary;

SELECT OCCUPATION , min(SALARY)
FROM employee_salary
GROUP BY OCCUPATION;


SELECT GENDER , MIN(AGE), MAX(AGE),AVG(AGE), COUNT(AGE)
FROM employee_demographics
GROUP BY GENDER;


-- ORDER BY 

SELECT * 
FROM employee_demographics
ORDER BY GENDER, AGE DESC;

-- BY USING COLUMNS NUMBER (NOT THE BEST PRACTICE)
SELECT * 
FROM employee_demographics
ORDER BY 5,4;


