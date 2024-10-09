SELECT * FROM Customer c LIMIT 10;
SELECT COUNT(*) FROM Customer c;
SELECT State, COUNT(*) AS Total FROM Customer c GROUP BY 1 ORDER BY Total DESC limit 10; 

SELECT FirstName, Address FROM Customer c;
SELECT COUNT(*) FROM Customer c WHERE Address LIKE '%Broadway%';

SELECT COUNT(*) FROM Customer c WHERE Company is NOT NULL;
SELECT FirstName FROM Customer c WHERE Company IS NULL;
