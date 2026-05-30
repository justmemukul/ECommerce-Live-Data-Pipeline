
# End-to-End E-Commerce Live Data Pipeline & Predictive Analytics

## 📊 Quick Project Preview
👉 https://drive.google.com/file/d/1F93kSfz1Pj473Ri4KUf2-NkHkOcA9-2R/view?usp=drive_link *(Note: Because this enterprise architecture actively processes a high-volume dataset of **1,000,000+ live rows** via a local SQL Server instance, a high-resolution PDF artifact has been provided for instant, browser-based visual and layout review.)*

---

## 🚀 Project Overview
This full-stack data engineering and business intelligence project establishes a scalable operational data ecosystem. The project breaks down data silos by creating a normalized relational database, writing a continuous background pipeline engine in Python to simulate live e-commerce sales, compressing massive row footprints, and deploying time-series machine learning models to project financial trends into the future.

### 💼 Key Business Case Solutions:
* **Siloed Data Resolution:** Engineered a robust Star Schema layout to transition raw data into structured, clean fields.
* **Intraday Stream Simulation:** Developed a background Python automation engine to feed new, unique e-commerce transactions directly into local database storage.
* **Continuous Timeline Engineering:** Applied custom DAX expressions (`STARTOFMONTH`) to group daily data noise into smooth monthly trends, enabling accurate forward forecasting.

---

## 🛠️ Tech Stack & System Architecture
* **Database Management:** SQL Server Management Studio (SSMS)
* **Pipeline Automation:** Python (`pyodbc`, `pandas`, `datetime`, `random`)
* **Semantic Modeling & BI:** Power BI Desktop (VertiPaq Columnar Compression Engine)
* **Advanced Analytics:** Time-Series Predictive Forecasting (95% Confidence Interval)

---

## 🏗️ How to Recreate the Pipeline Locally

### 1. Database Architecture & Setup
Open your SQL Server Management Studio (SSMS) instance and connect locally. Create a database named `ECommerce_Logistics_DB` and execute the provided `schema_backup.sql` script to instantly construct the normalized schema baseline:

```sql
CREATE TABLE fact_orders (
    Order_ID INT PRIMARY KEY,
    Order_Date DATE,
    Customer_ID INT,
    Product_ID INT,
    Carrier_ID VARCHAR(10),
    Quantity INT,
    Shipping_Cost DECIMAL(10,2),
    Order_Status VARCHAR(30)
);

```

### 2. Launch the Background Live Data Engine

The standalone Python script acts as a real-time transaction engine. It continuously packages clean, randomized parameters and pushes new sales directly to your hard drive without duplication hazards:

```bash
pip install pyodbc pandas
python pipeline_automation.py

```

### 3. Open the Executive Reporting App

Launch `ECommerce_Dashboard.pbix` in Power BI Desktop. Click **Refresh** in the top ribbon to trigger the local database handshake line. Watch your total order counters climb and your timeline charts dynamically expand to capture the live incoming Python stream in real time.

---

## 📊 Deep-Dive Case Study Documentation

To see the step-by-step breakdown of how specific corporate problems were solved across the different engineering layers, check out our dedicated master guide:

* 📄 **[18 Core Business Problems & Multi-Language Technical Solutions]d)*https://docs.google.com/document/d/1vnZVvwoJZWO-0EPkdd6HnFf9CHADlmuGC8U9I6IfKaI/edit?usp=drive_link*

```

---
