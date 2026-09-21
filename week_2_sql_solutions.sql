-- Week 2 SQL for Data Analysis
-- Table name assumed: sales
-- Columns: order_id, customer_name, order_date, category, sub_category,
-- product_name, quantity, unit_price, total_price, region

-- 1. Basic SELECT
SELECT * FROM sales;
SELECT order_id, customer_name, category, total_price FROM sales;

-- 2. WHERE
SELECT order_id, customer_name, total_price
FROM sales
WHERE total_price > 20000;

SELECT *
FROM sales
WHERE category = 'Electronics';

-- 3. GROUP BY + SUM
SELECT category, SUM(total_price) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- 4. AVG and COUNT
SELECT AVG(total_price) AS average_order_value FROM sales;
SELECT COUNT(*) AS order_count FROM sales;

SELECT category, AVG(total_price) AS average_order_value
FROM sales
GROUP BY category
ORDER BY average_order_value DESC;

-- 5. Highest-value orders
SELECT order_id, customer_name, category, total_price
FROM sales
ORDER BY total_price DESC;

-- 6. Top customers
SELECT customer_name, SUM(total_price) AS total_revenue
FROM sales
GROUP BY customer_name
ORDER BY total_revenue DESC
LIMIT 10;

-- 7. Orders above average
SELECT order_id, customer_name, total_price
FROM sales
WHERE total_price > (SELECT AVG(total_price) FROM sales)
ORDER BY total_price DESC;

-- 8. CASE classification
SELECT order_id, customer_name, total_price,
       CASE
           WHEN total_price >= 30000 THEN 'High'
           WHEN total_price >= 15000 THEN 'Medium'
           ELSE 'Low'
       END AS order_size
FROM sales
ORDER BY total_price DESC;

-- 9. JOIN example (requires a customers table)
SELECT s.order_id, s.customer_name, c.customer_segment, s.total_price
FROM sales AS s
JOIN customers AS c
  ON s.customer_name = c.customer_name;

-- 10. Combined category summary
SELECT category,
       COUNT(*) AS order_count,
       SUM(total_price) AS total_revenue,
       AVG(total_price) AS average_order_value
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;

-- 11. Missing-value checks
SELECT
    SUM(CASE WHEN customer_name IS NULL THEN 1 ELSE 0 END) AS missing_customer,
    SUM(CASE WHEN category IS NULL THEN 1 ELSE 0 END) AS missing_category,
    SUM(CASE WHEN total_price IS NULL THEN 1 ELSE 0 END) AS missing_total_price
FROM sales;

-- 12. Duplicate order IDs
SELECT order_id, COUNT(*) AS occurrences
FROM sales
GROUP BY order_id
HAVING COUNT(*) > 1;
