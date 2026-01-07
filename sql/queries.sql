-- finding total customers 
SELECT COUNT(*) AS total_customers
FROM customers;

-- number of customers churned
SELECT churn, COUNT(*) AS count FROM customers GROUP BY churn;

-- churn rate
SELECT  ROUND( SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS churn_rate_percentage FROM customers;

-- churn by contract type
SELECT contract, COUNT(*) AS total_customers, SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers FROM customers GROUP BY contract;

-- churn by internet service
SELECT internet_service, COUNT(*) AS total_customers, SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers FROM customers GROUP BY internet_service;

-- Avg monthly charges (churn Vs not churn)
SELECT  churn, ROUND(AVG(monthly_charges), 2) AS avg_monthly_charges FROM customers GROUP BY churn;

-- Tenure analysis
SELECT CASE 
        WHEN tenure < 12 THEN '0-1 year'
        WHEN tenure BETWEEN 12 AND 24 THEN '1-2 years'
        ELSE '2+ years'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers
FROM customers
GROUP BY tenure_group;




