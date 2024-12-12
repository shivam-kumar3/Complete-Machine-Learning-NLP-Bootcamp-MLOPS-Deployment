-- WHERE CLAUSE 

SELECT * 
FROM employee_salary
WHERE first_name = 'LESLIE';

SELECT * 
FROM employee_salary
WHERE SALARY <= 50000;


SELECT * 
FROM employee_demographics
WHERE GENDER = 'FEMALE';

SELECT * 
FROM employee_demographics
WHERE GENDER != 'FEMALE';

SELECT * 
FROM employee_demographics
WHERE birth_date > '1985-01-01';

-- AND OR NOT -- LOGICAL OPERATORS

SELECT * 
FROM employee_demographics
WHERE birth_date > '1985-01-01'
AND GENDER = 'MALE';

SELECT * 
FROM employee_demographics
WHERE birth_date > '1985-01-01'
OR GENDER = 'MALE';

SELECT *
FROM employee_demographics
WHERE (FIRST_NAME = 'LESLIE' AND AGE = 44) OR AGE > 50;

-- LIKE STATEMENT
-- % AND __
SELECT *
FROM employee_demographics
WHERE FIRST_NAME LIKE 'JER%'; -- THIS MEANS ANYTHINGS STARTS WITH JER 


SELECT *
FROM employee_demographics
WHERE FIRST_NAME LIKE '%ER%'; -- THIS MEANS ANYWHERE WITH THIS ALPHA 

SELECT * 
FROM employee_demographics
WHERE FIRST_NAME LIKE '%RY'; -- THIS MEANS THE NAME SHOULD END WITH RY 

SELECT *
FROM employee_demographics
WHERE FIRST_NAME LIKE 'A___'; -- THIS MEANS THE NAME SHOULD STARTS WITH A AND THEN HAVE 3 ALPHA AGTER THE A 

SELECT *
FROM employee_demographics
WHERE FIRST_NAME LIKE 'A___%';


SELECT *
FROM employee_demographics
WHERE FIRST_NAME LIKE 'A__%';

















