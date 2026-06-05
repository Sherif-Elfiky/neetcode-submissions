-- Write your query below
with sellers as (
select seller_id from orders
where extract(year from sale_date) = 2020
)
select seller_name from seller
where seller_id not in (select * from sellers)
order by seller_name asc
