-- HAVING VS WHERE 


SELECT OCCUPATION , AVG(SALARY)
FROM employee_salary
group by occupation
HAVING AVG(SALARY) > 75000;



