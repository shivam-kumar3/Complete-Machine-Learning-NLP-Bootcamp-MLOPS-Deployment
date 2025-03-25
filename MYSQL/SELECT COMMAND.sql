USE PARKS_AND_RECREATION;
SELECT * 
FROM EMPLOYEE_DEMOGRAPHICS;

-- BEST PRACTICE IS USE THE DATABASE NAME BEFORE THE TABLE NAME
 
SELECT * 
FROM parks_and_recreation.employee_demographics;

SELECT *
FROM parks_and_recreation.employee_salary;

SELECT first_NAME
FROM parks_and_recreation.employee_demographics;

SELECT 
    FIRST_NAME, LAST_NAME, AGE, AGE + 10
FROM
    parks_and_recreation.employee_demographics;


SELECT distinct GENDER 
FROM parks_and_recreation.employee_demographics;


