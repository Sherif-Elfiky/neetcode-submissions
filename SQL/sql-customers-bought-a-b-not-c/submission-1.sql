-- Write your query below


select customer_id, customer_name from orders
join customers using(customer_id)
group by customer_id, customer_name

having 
    sum(case when product_name = 'A' then 1 else 0 end) >= 1
    and sum(case when product_name = 'B' then 1 else 0 end) >= 1
    and sum(case when product_name = 'C' then 1 else 0 end) = 0
order by customer_name
