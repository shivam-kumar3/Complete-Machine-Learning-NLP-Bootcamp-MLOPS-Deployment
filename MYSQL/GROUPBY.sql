-- GROUP BY AND ORDER BY 

SELECT GENDER, AVG(AGE)
FROM employee_demographics
GROUP BY GENDER;

SELECT OCCUPATION , AVG(SALARY) , MAX(AGE)
FROM employee_salary
group by occupation, SALARY

