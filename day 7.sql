use northwind;

#1
SELECT product_name, unit_price
FROM products
ORDER BY unit_price DESC
LIMIT 5;

#2
SELECT product_name
FROM products
WHERE units_in_stock = 0;

#3
SELECT title_of_courtesy, COUNT(*) AS employee_count
FROM employees
GROUP BY title_of_courtesy
HAVING COUNT(*) > 1;

#4
SELECT customer_id, AVG(freight) AS avg_freight 
FROM orders
GROUP BY customer_id;

#5
SELECT product_name, unit_price
FROM products
ORDER BY unit_price DESC
LIMIT 1 OFFSET 1;

#6
SELECT p.product_name, p.unit_price, p.category_id
FROM products p
WHERE p.unit_price > (
    SELECT AVG(p2.unit_price)
    FROM products p2
    WHERE p2.category_id = p.category_id
);

#7
SELECT 
    product_name, 
    supplier_id, 
    unit_price,
    RANK() OVER (PARTITION BY supplier_id ORDER BY unit_price DESC) AS price_rank
FROM products;

#8
SELECT first_name, COUNT(*) AS name_count
FROM employees
GROUP BY first_name
HAVING COUNT(*) > 1;

#9
SELECT product_name, unit_price
FROM products
WHERE unit_price > (
    SELECT AVG(unit_price) * 3
    FROM products
);

#10
SELECT order_id, order_date, freight
FROM orders
WHERE freight = (
    SELECT MAX(freight)
    FROM orders AS o2
    WHERE YEAR(o2.order_date) = YEAR(orders.order_date)
);

#11
SELECT c.customer_id, c.company_name, e.first_name, e.last_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN employees e ON o.employee_id = e.employee_id;

#12
SELECT p.product_name, s.company_name AS supplier_name, c.category_name
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id
JOIN categories c ON p.category_id = c.category_id;

#13
SELECT c.customer_id, c.company_name, COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.company_name
ORDER BY total_orders DESC;

#14
SELECT c.customer_id, c.company_name, SUM(o.freight) AS total_freight
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.company_name
ORDER BY total_freight DESC
LIMIT 5;

#15
SELECT p.product_name, SUM(od.quantity) AS total_quantity_sold
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;

#16
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees e
LEFT JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
ORDER BY order_count DESC;

#17
SELECT DISTINCT c.customer_id, c.company_name, p.product_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
WHERE p.product_name = 'Tofu';

#18
SELECT p.product_name, SUM(od.unit_price * od.quantity) AS total_revenue
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC
LIMIT 3;

#19
SELECT e.employee_id, e.first_name, e.last_name, COUNT(DISTINCT o.customer_id) AS customer_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name;

#20
SELECT c.category_name, COUNT(p.product_id) AS product_count, AVG(p.unit_price) AS average_price
FROM categories c
JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_name
ORDER BY product_count DESC;