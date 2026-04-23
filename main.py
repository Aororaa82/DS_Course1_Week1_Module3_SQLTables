# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# CodeGrade step1
# Replace None with your code
df_boston = pd.read_sql(""" 
SELECT firstName || ' ' || lastName AS name, jobTitle
FROM employees
JOIN offices ON employees.officeCode = offices.officeCode
WHERE city = 'Boston';

""",conn)
df_boston

# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql(""" 
SELECT offices.officeCode, city
FROM offices
LEFT JOIN employees ON offices.officeCode = employees.officeCode
WHERE employees.employeeNumber IS NULL;                          

""",conn)
df_zero_emp

# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql(""" 
SELECT firstName, lastName, city,state
FROM employees
LEFT JOIN offices ON employees.officeCode = offices.officeCode
ORDER BY firstName, lastName; 

""",conn)
df_employee

# CodeGrade step4
# Replace None with your code
df_contacts = pd.read_sql(""" 
SELECT contactFirstName, contactLastName, phone, salesRepEmployeeNumber
FROM customers 
LEFT JOIN orders ON customers.customerNumber = orders.customerNumber
WHERE orders.orderNumber IS NULL
ORDER BY contactLastName;                         

""",conn)
df_contacts

# CodeGrade step5
# Replace None with your code
df_payment = pd.read_sql(""" 
SELECT contactFirstName , contactLastName, amount, paymentDate
FROM customers
JOIN payments ON customers.customerNumber = payments.customerNumber
ORDER BY CAST (amount AS DECIMAL) DESC;
""",conn)
df_payment

# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql(""" 
SELECT employeeNumber, firstName, lastName , COUNT(customerNumber) AS number_of_customers
FROM employees
JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber                   
GROUP BY employeeNumber
HAVING AVG(creditLimit) > 90000
ORDER BY number_of_customers DESC;
""",conn)
df_credit

# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql(""" 
SELECT productName, COUNT(orderNumber) AS numorders, SUM(quantityOrdered) AS totalunits
FROM products
JOIN orderdetails ON products.productCode = orderdetails.productCode
GROUP BY products.productCode
ORDER BY totalunits DESC;
""",conn)
df_product_sold

# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql (""" 
SELECT productName, products.productCode, COUNT(DISTINCT orders.customerNumber) AS numpurchasers
FROM products
JOIN orderdetails ON products.productCode = orderdetails.productCode
JOIN orders ON orderdetails.orderNumber = orders.orderNumber
GROUP BY products.productCode
ORDER BY numpurchasers DESC;                                 

""",conn)
df_total_customers

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql(""" 
SELECT COUNT (customers.customerName) AS n_customers, offices.officeCode , offices.city
FROM offices
JOIN employees ON offices.officeCode = employees.officeCode
JOIN customers ON employees.employeeNumber = customers.salesRepEmployeeNumber
GROUP BY offices.officeCode                        

""",conn)
df_customers

# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql(""" 
SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, o.city, o.officeCode
FROM employees e
JOIN offices o ON e.officeCode = o.officeCode
JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
JOIN orders ord ON c.customerNumber = ord.customerNumber
JOIN orderdetails od ON ord.orderNumber = od.orderNumber
WHERE od.productCode IN (
    SELECT productCode
    FROM orderdetails
    JOIN orders ON orderdetails.orderNumber = orders.orderNumber
    GROUP BY productCode
    HAVING COUNT(DISTINCT customerNumber) < 20
);                          
""", conn)
df_under_20

# Run this cell without changes

conn.close()