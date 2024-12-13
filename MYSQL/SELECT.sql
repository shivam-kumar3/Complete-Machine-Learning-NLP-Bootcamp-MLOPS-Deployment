SELECT * 
FROM parks_and_recreation.employee_demographics;

SELECT * 
FROM parks_and_recreation.employee_salary;

SELECT FIRST_NAME, LAST_NAME
FROM parks_and_recreation.employee_salary
order by first_name, last_name;

SELECT AGE,
AGE + 20
FROM parks_and_recreation.employee_demographics;

# PEMDAS 

SELECT  GENDER
FROM parks_and_recreation.employee_demographics;

SELECT DISTINCT GENDER
FROM parks_and_recreation.employee_demographics;



SELECT GENDER , FIRST_NAME
FROM parks_and_recreation.employee_demographics