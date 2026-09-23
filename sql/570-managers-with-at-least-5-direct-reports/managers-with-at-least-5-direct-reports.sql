# Write your MySQL query statement below
select e.name from Employee e
inner join Employee a on a.managerId = e.id
group by a.managerId
having count(*) >= 5