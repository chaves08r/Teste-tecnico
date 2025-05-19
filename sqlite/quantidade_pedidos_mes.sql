-- SQLite
select count(*) as num_pedidos, strftime('%Y-%m', order_purchase_timestamp) as mesano from orders group by strftime('%Y-%m', order_purchase_timestamp)