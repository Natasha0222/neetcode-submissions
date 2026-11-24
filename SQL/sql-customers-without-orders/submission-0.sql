-- Write your query below
SELECT name
FROM orders
RIGHT JOIN customers
ON orders.customer_id=customers.id
WHERE customer_id IS NULL
