-- Write your query below


select employee_id, 0 as bonus
from employees
where employee_id % 2 = 0 or left(name, 1) = 'M'

union all

select employee_id, salary as bonus
from employees
where employee_id % 2 != 0 and left(name, 1) != 'M'

order by employee_id asc
