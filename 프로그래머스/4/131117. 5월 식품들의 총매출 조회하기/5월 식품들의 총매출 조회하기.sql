-- 코드를 입력하세요
SELECT f_product.product_id, f_product.product_name, sum(f_order.amount * f_product.price) as total_sales
FROM FOOD_PRODUCT f_product
JOIN FOOD_ORDER f_order
ON f_product.product_id = f_order.product_id
WHERE f_order.PRODUCE_DATE LIKE '2022-05%'
GROUP BY product_id
ORDER BY total_sales desc, f_product.product_id