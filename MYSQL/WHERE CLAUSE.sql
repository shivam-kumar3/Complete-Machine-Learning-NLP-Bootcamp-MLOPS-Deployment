-- WHERE CLAUSE

SELECT * 
FROM EMPLOYEE_SALARY
WHERE SALARY >= 50000;

SELECT * 
FROM EMPLOYEE_DEMOGRAPHICS
WHERE GENDER != "fEMALE";

-- DATES 

SELECT * 
FROM EMPLOYEE_DEMOGRAPHICS
WHERE BIRTH_DATE > "1985-01-01"
OR NOT GENDER = "MALE";


SELECT * 
FROM employee_demographics
WHERE FIRST_NAME = 'Leslie' and age = 44;

SELECT * 
FROM employee_demographics
WHERE (FIRST_NAME = 'Leslie' and age = 44) or age > 55;


-- LIKE STATEMENT
-- % AND _ 

SELECT * 
FROM employee_demographics
WHERE FIRST_NAME  like '%r%';

select * 
from employee_demographics
where first_name like 'a___%';


select * 
from employee_demographics
where birth_date like '1989%';