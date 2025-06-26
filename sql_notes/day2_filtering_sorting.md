NOT – Negates the condition

SELECT * 
FROM Customers
WHERE NOT Country = 'Germany';

(Also same as Country <> 'Germany')

. Sorting with ORDER BY

➤ Sort in ascending order (default)

SELECT * 
FROM Customers
ORDER BY CustomerName;
