# Write your MySQL query statement below
select round(count(distinct temp.player_id)/(select count(distinct player_id) from Activity),2) as fraction
from (select player_id, min(event_date) as min_date from activity group by player_id) as temp
join Activity a on temp.player_id = a.player_id and a.event_date = temp.min_date + INTERVAL 1 DAY