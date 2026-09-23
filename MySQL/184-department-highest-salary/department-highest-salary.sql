# Write your MySQL query statement below
SELECT b.name AS Department, a.name AS Employee, a.salary AS Salary
FROM Department b
JOIN Employee a ON b.id = a.departmentId
WHERE a.salary IN (SELECT MAX(salary) FROM Employee WHERE departmentId = b.id)
