# End-to-End E-Commerce Live Data Pipeline & Predictive Analytics

## 🚀 Project Overview
This full-stack data engineering and analytics project builds a scalable enterprise data ecosystem. It processes **1,000,000+ rows** of transactional data, automates real-time data ingestion using Python, optimizes storage layers via a normalized SQL Server Star Schema, and delivers predictive executive insights through a 6-page interactive Power BI application.

---

## 🛠️ Tech Stack & Architecture
* **Database Layer:** SQL Server (SSMS) – Normalized Star Schema design.
* **Pipeline Automation:** Python (`pyodbc`, `pandas`, `datetime`) – Live transaction simulation loop.
* **Semantic Modeling:** Power BI Desktop – VertiPaq columnar compression & Time-Intelligence DAX engine.
* **Advanced Analytics:** Time-Series Machine Learning Revenue Forecasting (95% Confidence Interval).

---

## 🏗️ How to Recreate the Pipeline Locally

### 1. Database Setup
Execute the `schema_backup.sql` script inside SQL Server Management Studio to instantly generate the relational schema baseline (`fact_orders`, `dim_customers`, `dim_products`, `dim_carriers`).

### 2. Launch the Automation Stream
Ensure you have the prerequisites installed, update your local server authentication string inside the script, and fire up the engine:
```bash
pip install pyodbc pandas
python pipeline_automation.py
