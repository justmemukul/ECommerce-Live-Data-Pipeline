USE ECommerce_Logistics_DB;
GO

-- 1. Create View for Products
CREATE VIEW v_Dim_Products AS 
SELECT Product_ID, Product_Name, Category, Sub_Category, Base_Cost, Unit_Price 
FROM Dim_Products;
GO

-- 2. Create View for Customers
CREATE VIEW v_Dim_Customers AS 
SELECT Customer_ID, Customer_Name, Gender, City, State 
FROM Dim_Customers;
GO

-- 3. Create View for Carriers
CREATE VIEW v_Dim_Carriers AS 
SELECT Carrier_ID, Carrier_Name, Ship_Mode, Avg_Delivery_Days 
FROM Dim_Carriers;
GO

-- 4. Create View for Orders (The Fact Table)
CREATE VIEW v_Fact_Orders AS 
SELECT Order_ID, Order_Date, Customer_ID, Product_ID, Carrier_ID, Quantity, Shipping_Cost, Order_Status 
FROM Fact_Orders;
GO