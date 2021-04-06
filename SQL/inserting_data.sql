-- Set primary key starting value.
ALTER TABLE mechabots.company_client AUTO_INCREMENT = 1;
ALTER TABLE mechabots.product AUTO_INCREMENT = 1;
ALTER TABLE mechabots.supplier AUTO_INCREMENT = 1;
ALTER TABLE mechabots.material AUTO_INCREMENT = 1;
ALTER TABLE mechabots.project AUTO_INCREMENT = 1;
ALTER TABLE mechabots.employee AUTO_INCREMENT = 1;
ALTER TABLE mechabots.purchase AUTO_INCREMENT = 1;

-- Delete records if necessary.
DELETE FROM mechabots.employee;
DELETE FROM mechabots.purchase;
DELETE FROM mechabots.company_client;
DELETE FROM mechabots.product;
DELETE FROM mechabots.supplier;
DELETE FROM mechabots.material;
DELETE FROM mechabots.project;

-- First the tables without foreign keys.
INSERT INTO mechabots.company_client (ClientName, ClientType, ClientMail, Region)
VALUES ('JTech', 'Corporate', 'jtech@jt.com', 'US'),
       ('HCom', 'Corporate', 'hcom@hc.com', 'US'),
       ('Stoqn Georgiev', 'Non-Corporate', 'stoqnge@abv.bg', 'BG'),
       ('Space Age IT', 'Corporate', 'spaceait@spit.com', 'US'),
       ('John Carmack', 'Non-Corporate', 'johncar@gmail.com', 'US'),
       ('Digital Advantage', 'Corporate', 'digitala@dga.com', 'ES'),
       ('Integrative Choices', 'Corporate', 'integchoice@intgchoice.com', 'UK'),
       ('TechIQ', 'Corporate', 'techq@tq.com', 'RU'),
       ('JTech', 'Corporate', 'jtech@jt.com', 'FR'),
       ('Digital Advantage', 'Corporate', 'digitala@dga.com', 'US'),
       ('Quantum Corp', 'Corporate', 'quant@qcorp.com', 'UK'),
       ('Charlie Standing', 'Non-Corporate', 'charlie_stand@gmail.com', 'UK'),
       ('Bespoke IT', 'Corporate', 'bespoke@bsp.com', 'UK'),
       ('Cloud Solutions', 'Corporate', 'cloudsol@clds.com', 'UK'),
       ('Bogdan Abramov', 'Non-Corporate', 'bogdan.a@gmail.com', 'RU'),
       ('Cloud Solutions', 'Corporate', 'cloudsol@clds.com', 'UK'),
       ('JTech', 'Corporate', 'jtech@jt.com', 'US'),
       ('Ben Fischer', 'Non-Corporate', 'benfish@gmail.com', 'DE'),
       ('Angelo Alberici', 'Non-Corporate', 'angeloalb@gmail.com', 'IT'),
       ('TechIQ', 'Corporate', 'techq@tq.com', 'RU');


INSERT INTO mechabots.product (ProductName, ProductType, Price)
VALUES ('ZebraBot', 'Quadrupedal', 1800),
       ('Vector', 'Social robot', 600),
       ('SpotMini', 'Quadrupedal', 5400),
       ('Atlas', 'Bipedal', 7900),
       ('Aibo', 'Quadrupedal', 1150),
       ('G-rex', 'Robot cleaner', 970),
       ('Ziibo', 'Social robot', 480);

--------------------------------------------

INSERT INTO mechabots.material (MaterialType, MaterialAmount)
VALUES ('Iron', 100),
       ('Plastic', 150),
       ('Iron', 350),
       ('Copper', 140),
       ('Copper', 240),
       ('Plastic', 190),
       ('Iron', 310);

INSERT INTO mechabots.supplier (SupplierName, DateOfDelivery, MaterialID)
VALUES ('ModernTools', '2021-06-14', 2),
       ('DeliverySolution', '2021-04-09', 3),
       ('JeromyEx', '2021-06-14', 5);

INSERT INTO mechabots.project (ProjectName, ProjectType, DeadLine, MaterialID)
VALUES ('Vector 2.0', '', '2023-07-13', 2),
       ('VertoSwipe', 'Windows Robot Cleaner', '2025-01-23', 3),
       ('Hector', 'House builder robot', '2026-11-03', 3);

INSERT INTO mechabots.employee (FirstName, SurName, Sex, Age, Nationality, Department, FieldOfExpertise, Experience, YearsInTheCompany, ManagerID, ProjectID)
VALUES ('Gregory', 'Adams', 'M', 34, 'American', 'Hardware', 'Electrical Engineering', 13, 11, NULL, 2),
       ('Hannah', 'Stark', 'F', 25, 'English', 'Hardware', 'Mechanical Engineering', 3, 3, 1, 3),
       ('Cvetomir', 'Stoqnov', 'M', 26, 'Bulgarian', 'Software' , 'Software Engineering', 8, 8, 2, 1),
       ('Gabby', 'Stone', 'M', 38, 'American', 'Software', 'Software Engineering', 10, 8, NULL, 3),
       ('Xiang', 'Lee', 'F', 43, 'Chinese', 'Software', 'Machine Learning', 15, 11, NULL, 1),
       ('Hristo', 'Ivanov', 'M', 29, 'Bulgarian', 'Hardware', 'Mechanical Engineering', 6, 5, 2, 3),
       ('Viktoriq', 'Kirilova', 'F', 23, 'Bulgarian', 'Hardware', 'Electrical Engineering', 1, 1, 1, 2),
       ('Maksim', 'Olochenko', 'M', 34, 'Russian', 'Hardware', 'Electrical Engineering', 4, 4, NULL, 1),
       ('Steve', 'Parker', 'M', 48, 'American', 'Software', 'Machine Learning', 14, 11, 3, 2),
       ('Valerie', 'Hamilton', 'F', 20, 'American', 'Hardware' , 'Mechanical Engineering', 1, 1, 1, 2),
       ('Olga', 'Ivanova', 'F', 31, 'Russian', 'Hardware' , 'Mechanical Engineering', 6, 6, 6, 3),
       ('Tom', 'Oliver', 'M', 22, 'English', 'Software', 'Machine Learning', 2, 2, 3, 1),
       ('Stacy', 'James', 'F', 30, 'American', 'Sales', 'Sales', 12, 10, NULL, NULL),
       ('Emma', 'Carrington', 'F', 27, 'American', 'Sales' , 'Sales', 5, 4, 13, NULL),
       ('Daniel', 'Tomphosn', 'M', 32, 'American', 'Sales' , 'Sales', 2, 2, 13, NULL);
       
INSERT INTO mechabots.purchase (Amount, EmployeeID, ClientID, ProductID)
VALUES (1800, 13, 1, 1),
       (480, 13, 15, 7),
       (5400, 14, 1, 3),
       (480, 15, 2, 1),
       (480, 14, 12, 7);