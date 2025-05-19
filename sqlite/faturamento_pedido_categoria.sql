-- SQLite
select sum(i.price) as faturamento, p.product_category_name as categoria from items i join products p on i.product_id = p.product_id
group by p.product_category_name order by 1 desc
