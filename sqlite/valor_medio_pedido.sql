WITH valores_pedidos as(
    select sum(p.payment_value) as pagamento_pedido, c.customer_state as estado from orders o 
        join payments p on o.order_id = p.order_id
        join customers c on o.customer_id = c.customer_id
        group by o.order_id, c.customer_state
    )
SELECT AVG(pagamento_pedido) as valor_medio_pedido, estado from valores_pedidos 
group by estado
