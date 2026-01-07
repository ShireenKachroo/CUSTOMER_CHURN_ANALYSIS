CREATE DATABASE IF NOT EXISTS customer_churn;
USE customer_churn;

CREATE TABLE customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    gender VARCHAR(10),
    senior_citizen TINYINT,
    partner VARCHAR(5),
    dependents VARCHAR(5),
    tenure INT,
    phone_service VARCHAR(5),
    internet_service VARCHAR(20),
    contract VARCHAR(20),
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(10,2),
    churn VARCHAR(5)
);

SELECT * FROM customers

SELECT *FROM customers LIMIT 5

SELECT churn, COUNT(*) FROM customers GROUP BY churn


