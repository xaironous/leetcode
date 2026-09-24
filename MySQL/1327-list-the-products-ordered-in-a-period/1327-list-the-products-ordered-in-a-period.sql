# Write your MySQL query statement below
select a.product_name, sum(b.unit) as unit
from Products a join orders b on b.product_id = a.product_id
where b.order_date like '2020-02-%'
group by a.product_name
having sum(b.unit) >= 100