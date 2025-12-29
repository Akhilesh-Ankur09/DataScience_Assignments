-- =========================
-- TABLE 1: Departments
-- =========================
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO Departments VALUES
(1, 'HR', 'Delhi'),
(2, 'IT', 'Bangalore'),
(3, 'Finance', 'Mumbai');

-- =========================
-- TABLE 2: Employees
-- =========================
CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    age INT,
    salary INT,
    dept_id INT
);

INSERT INTO Employees VALUES
(101, 'Amit', 28, 40000, 1),
(102, 'Neha', 32, 60000, 2),
(103, 'Rahul', 25, 35000, 2),
(104, 'Priya', 29, 50000, 3),
(105, 'Karan', 35, 70000, 1);

-- =========================
-- LOGICAL OPERATORS
-- =========================

-- AND operator
SELECT * FROM Employees
WHERE age > 30 AND salary > 50000;

-- OR operator
SELECT * FROM Employees
WHERE dept_id = 1 OR dept_id = 3;

-- NOT operator
SELECT * FROM Employees
WHERE NOT dept_id = 2;

-- =========================
-- ARITHMETIC FUNCTIONS
-- =========================

-- Total salary
SELECT SUM(salary) AS Total_Salary FROM Employees;

-- Average salary
SELECT AVG(salary) AS Average_Salary FROM Employees;

-- Count employees
SELECT COUNT(*) AS Total_Employees FROM Employees;

-- =========================
-- ORDER BY QUERIES
-- =========================

-- Order employees by salary (descending)
SELECT * FROM Employees
ORDER BY salary DESC;

-- Order employees by age (ascending)
SELECT * FROM Employees
ORDER BY age ASC;
