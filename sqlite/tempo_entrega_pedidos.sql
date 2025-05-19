-- SQLite
select 
COALESCE(
    ROUND(
        julianday(order_delivered_customer_date)-julianday(order_purchase_timestamp)
        ), 0) as tempo_entrega_dias, count(*) as pedidos from orders 
where order_delivered_customer_date is not null 
group by ROUND(julianday(order_delivered_customer_date)-julianday(order_purchase_timestamp)) 