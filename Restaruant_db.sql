
-- Explore the items table --

USE restaurant_db;
-- 1. View menu_items table.
SELECT *
FROM menu_items;

-- 2. Find the number of items in the menu.
SELECT 
COUNT(menu_item_id)	
FROM menu_items;

-- 3. What are the least and most expensive items on the menu.

SELECT 
*
FROM menu_items
ORDER BY price;

SELECT 
*
FROM menu_items
ORDER BY price DESC;
-- 4. How many Italian dishes are on the menu.
SELECT 
COUNT(*)
FROM menu_items
WHERE category = "Italian";
-- 5. What are the least and most expensive Italian dishes on the menu.
SELECT 
*
FROM menu_items
WHERE category = "Italian"
GROUP BY category;

SELECT 
*
FROM menu_items
WHERE category = "Italian"
GROUP BY category DESC;  
-- 6. How many dishes are in each catefory.
SELECT 
category,
COUNT(menu_item_id)
FROM menu_items
GROUP BY category;
-- 7. What is the average dish price within each category.
SELECT 
category,
AVG(price)
FROM menu_items
GROUP BY category;

-- Explore the orders table --

USE restaurant_db;
-- 1. View menu_items table. 
SELECT * 
FROM order_details;



-- 2. What is the date range of the table?

SELECT 
MIN(order_date),
MAX(order_date)
FROM order_details;

-- 3.  How many orders were made in the date range?
SELECT 
COUNT(DISTINCT order_id) 
FROM order_details; 



-- 4. How many items were ordered within the date range?


SELECT 
COUNT(*) 
FROM order_details; 


-- 5. Which orders had the most number of items?
SELECT
COUNT(item_id) AS orders,
order_id 
FROM order_details 
GROUP BY order_id
ORDER BY orders DESC;

-- 6. How many orders had more than 12 items?

SELECT 
COUNT(*)
FROM
(SELECT
COUNT(item_id) AS orders,
order_id 
FROM order_details 
GROUP BY order_id
HAVING orders >12) AS num_orders;


-- Analyze customer behavior --

USE restaurant_db;
-- 1. Combine the menu_items and order_details tables into a single table
SELECT * 
FROM order_details
	LEFT JOIN menu_items 
		ON menu_items.menu_item_id = order_details.item_id;

-- 2. What were the least and most ordered items? What categories were they in?

SELECT 
item_name,
category,
COUNT(order_details_id)AS orders
FROM order_details
	LEFT JOIN menu_items 
		ON menu_items.menu_item_id = order_details.item_id
	GROUP BY 
		item_name, category
	ORDER BY 
		orders DESC;


-- 3. What were the top 5 orders that spent the most money?

SELECT 
order_id, 
SUM(price)
FROM order_details
	LEFT JOIN menu_items 
		ON menu_items.menu_item_id = order_details.item_id
	GROUP BY order_id
	ORDER BY SUM(price) DESC
	LIMIT 5;

-- 4. View the details of the highest spend order. Which specific items were purchased?

SELECT 
category,
COUNT(item_id)
FROM order_details
	LEFT JOIN menu_items 
		ON menu_items.menu_item_id = order_details.item_id
	WHERE order_id = 440
    GROUP BY category;
    
-- 5. View the details of the top 5 highest spend orders

SELECT 
category,
order_id,
COUNT(item_id)
FROM order_details
	LEFT JOIN menu_items 
		ON menu_items.menu_item_id = order_details.item_id
	WHERE order_id IN(440, 2075, 1957, 330, 2675)
    GROUP BY order_id, category;