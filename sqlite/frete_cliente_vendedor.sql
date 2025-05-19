-- SQLite
select i.freight_value as valor_frete, 
    c.customer_city as cidade_cliente,
    c.customer_state as estado_cliente,
    s.seller_city as cidade_vendedor,
    s.seller_state as estado_vendedor
     from orders o 
    join items i on i.order_id = o.order_id
    join customers c on o.customer_id = c.customer_id
    join sellers s on i.seller_id = s.seller_id
    where i.freight_value > 0 
    order by i.freight_value
    
