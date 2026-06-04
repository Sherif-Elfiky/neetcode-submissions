-- Write your query below


with customer_ids as (
select id from customers
where id not in (select customer_id as id from orders)

)

select name from customers
where id in (select * from customer_ids)


