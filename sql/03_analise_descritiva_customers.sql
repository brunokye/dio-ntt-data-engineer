SELECT * FROM Employee e;

SELECT c.FirstName, c.LastName FROM Customer c 
WHERE Company IS NULL AND c.FirstName 
IN (SELECT e.FirstName FROM Employee e);
		
SELECT c.FirstName, c.LastName FROM Customer c 
INNER JOIN Employee e WHERE c.FirstName  = e.FirstName;