-- USE restaurant_db
-- 1. View menu_items table.
-- SELECT * FROM order_details

-- 2.

-- SELECT COUNT(DISTINCT order_id) FROM order_details 

-- 3.
/*SELECT 
COUNT(item_id) AS orders,
order_id 
FROM order_details 
GROUP BY order_id
ORDER BY orders desc*/

-- 4.

/*SELECT 
COUNT(item_id) AS orders,
order_id 
FROM order_details 
GROUP BY order_id
ORDER BY orders desc*/

-- 5.
SELECT 
COUNT(*)
FROM
(SELECT
COUNT(item_id) AS orders,
order_id 
FROM order_details 
GROUP BY order_id
HAVING orders >12) AS num_orders
