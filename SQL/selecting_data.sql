SELECT * FROM mechabots.company_client;
SELECT * FROM mechabots.product;
SELECT * FROM mechabots.supplier;
SELECT * FROM mechabots.material;
SELECT * FROM mechabots.project;
SELECT * FROM mechabots.employee;
SELECT * FROM mechabots.purchase;


-- The number of employees and their respective age. 
SELECT COUNT(employee.EmployeeID) as '# of employees', employee.Age  
FROM mechabots.employee
GROUP BY employee.Age
ORDER BY employee.Age DESC;


-- The biggest purchase a client made, which employee sold it and the sold product.
SELECT MAX(purchase.Amount) as Amount, employee.FirstName as Employee, company_client.ClientName as Client_Name, product.ProductName as Product
FROM mechabots.purchase
JOIN mechabots.employee
ON purchase.EmployeeID = employee.EmployeeID
JOIN mechabots.company_client
ON purchase.ClientID = company_client.ClientID
JOIN mechabots.product
ON purchase.ProductID = product.ProductID;


-- Average price of every product of type - quadrupepal.
SELECT CAST(AVG(product.Price) as DECIMAL(6, 2)) AS 'Average price', product.ProductType as 'Product Type'
FROM mechabots.product
GROUP BY 'Product Type'
HAVING product.ProductType = 'Quadrupedal';


-- Which employee, works on which project.
SELECT project.ProjectName, emp.FirstName, emp.SurName
FROM mechabots.project
JOIN (SELECT employee.FirstName, employee.SurName, employee.ProjectID
      FROM mechabots.employee) as emp
ON project.ProjectID = emp.ProjectID;


-- Every client's name who contains 'tech' in it.
SELECT company_client.ClientName
FROM mechabots.company_client
WHERE ClientName LIKE '%tech%';


-- Every employee that have experience over 9 years, using wildcard.
SELECT employee.Experience
FROM mechabots.employee
WHERE Experience LIKE '1_' OR Experience LIKE '2_';


-- Employee name and client name.
SELECT employee.FirstName as 'Employee And ClientName'
FROM mechabots.employee
UNION 
SELECT company_client.ClientName
FROM mechabots.company_client
ORDER BY 'Employee And ClientName';


-- Identify whether a client is corporate one or not, only by email.
SELECT ClientMail AS Mail, CASE
WHEN ClientMail LIKE '%gmail%' OR ClientMail LIKE '%abv%' THEN 'This client is non-coprorate one.'
ELSE 'This client is a corporate one.' 
END AS TypeOfClient
FROM mechabots.company_client;


-- Fire an employee, using stored procedure.
CALL mechabots.spFireEmployee('Gregory', 'Adams');