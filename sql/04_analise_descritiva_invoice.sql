SELECT * FROM Invoice i LIMIT 10;
SELECT * FROM InvoiceLine il LIMIT 10;

SELECT UnitPrice, COUNT(*) AS Record FROM InvoiceLine il GROUP BY UnitPrice;

SELECT i.CustomerId, c.FirstName, COUNT(*) AS Record FROM Invoice i 
INNER JOIN Customer c ON c.CustomerId = i.CustomerId
GROUP BY 1 ORDER BY Record;

SELECT i.InvoiceId, il.InvoiceLineId FROM Invoice i 
INNER JOIN InvoiceLine il 
INNER JOIN Customer c ON c.CustomerId = i.CustomerId 
GROUP BY 1 LIMIT 10;