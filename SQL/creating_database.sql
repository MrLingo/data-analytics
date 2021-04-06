CREATE DATABASE IF NOT EXISTS mechabots;
USE mechabots;


CREATE TABLE IF NOT EXISTS mechabots.employee (
    EmployeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(30) NOT NULL,
    SurName VARCHAR(30) NOT NULL,
    Sex VARCHAR(1) NOT NULL,
    Age INT(2) NOT NULL,
    Nationality VARCHAR(20) DEFAULT 'Unspecified',
    Department VARCHAR(25) NOT NULL,
    FieldOfExpertise VARCHAR(30) NOT NULL,
    Experience INT(2) NOT NULL,
    YearsInTheCompany INT(2) NOT NULL,
    ManagerID INT,
    ProjectID INT,
    PRIMARY KEY(EmployeeID, FirstName)
);

CREATE TABLE IF NOT EXISTS mechabots.project (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectName VARCHAR(20) NOT NULL,
    ProjectType VARCHAR(25) NOT NULL,
    DeadLine DATE NOT NULL,
    MaterialID INT
);


-- Finished projects.
CREATE TABLE IF NOT EXISTS mechabots.product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(20) NOT NULL UNIQUE,
    ProductType VARCHAR(25) NOT NULL,
    Price INT(4) NOT NULL
);


CREATE TABLE IF NOT EXISTS mechabots.purchase (
    PurchaseID INT AUTO_INCREMENT PRIMARY KEY,
    Amount INT(4) NOT NULL,
    EmployeeID INT,
    ClientID INT,
    ProductID INT
);

CREATE TABLE IF NOT EXISTS mechabots.company_client (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    ClientName VARCHAR(35) NOT NULL,
    ClientType VARCHAR(13) NOT NULL,    -- Corporate | Non-Corporate
    ClientMail VARCHAR(35) NOT NULL,
    Region VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS mechabots.material (
    MaterialID INT AUTO_INCREMENT PRIMARY KEY,
    MaterialType VARCHAR(30) NOT NULL,
    MaterialAmount INT(7) NOT NULL
);

CREATE TABLE IF NOT EXISTS mechabots.supplier (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(35) NOT NULL,
    DateOfDelivery DATE NOT NULL,
    MaterialID INT
);


-- Connect foreign keys AFTER inserting the records.
ALTER TABLE mechabots.employee
ADD FOREIGN KEY (ManagerID) REFERENCES mechabots.employee(EmployeeID) ON DELETE SET NULL;

ALTER TABLE mechabots.employee
ADD FOREIGN KEY (ProjectID) REFERENCES mechabots.project(ProjectID) ON DELETE SET NULL;

ALTER TABLE mechabots.project
ADD FOREIGN KEY (MaterialID) REFERENCES mechabots.material(MaterialID) ON DELETE CASCADE;

ALTER TABLE mechabots.purchase
ADD FOREIGN KEY (EmployeeID) REFERENCES mechabots.employee(EmployeeID) ON DELETE CASCADE;

ALTER TABLE mechabots.purchase
ADD FOREIGN KEY (ClientID) REFERENCES mechabots.company_client(ClientID) ON DELETE CASCADE;

ALTER TABLE mechabots.purchase
ADD FOREIGN KEY (ProductID) REFERENCES mechabots.product(ProductID) ON DELETE CASCADE;

ALTER TABLE mechabots.supplier
ADD FOREIGN KEY (MaterialID) REFERENCES mechabots.material(MaterialID) ON DELETE CASCADE;

ALTER TABLE mechabots.project
DROP FOREIGN KEY MaterialID;


-- Delete if necessary.
DROP DATABASE mechabots;
DROP TABLE mechabots.purchase;
DROP TABLE mechabots.supplier;
DROP TABLE mechabots.employee;
DROP TABLE mechabots.project;
DROP TABLE mechabots.product;
DROP TABLE mechabots.company_client;
DROP TABLE mechabots.material;

