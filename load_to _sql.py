{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d483a049-1626-4807-973f-83f8db1ea845",
   "metadata": {},
   "source": [
    "## Creating a automation for importing data into sql from csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2f21fcd9-3b8a-47c2-8687-2175601f4d77",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🔌 Establishing connection to SQL Server...\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd \n",
    "from sqlalchemy import create_engine,text\n",
    "import urllib\n",
    "\n",
    "print(\"🔌 Establishing connection to SQL Server...\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c279afdc-b1de-4d8a-ad30-861c495b0d70",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sqlalchemy import create_engine\n",
    "import urllib\n",
    "\n",
    "print(\"🔌 Establishing connection to SQL Server...\")\n",
    "\n",
    "# UPDATE THESE DETAILS TO MATCH YOUR OWN SSMS INSTANCE NAME\n",
    "server_name = 'YOUR_SERVER_NAME_HERE'  # e.g., 'localhost' or 'DESKTOP-XXXXX'\n",
    "database_name = 'ECommerce_Logistics_DB'\n",
    "\n",
    "params = urllib.parse.quote_plus(\n",
    "    f\"DRIVER={{ODBC Driver 17 for SQL Server}};\"\n",
    "    f\"SERVER={server_name};\"\n",
    "    f\"DATABASE={database_name};\"\n",
    "    f\"Trusted_Connection=yes;\"\n",
    ")\n",
    "engine = create_engine(f\"mssql+pyodbc:///?odbc_connect={params}\")\n",
    "\n",
    "# Function to safely load chunks into SQL\n",
    "def load_table_to_sql(csv_filename, table_name, if_exists_mode='append'):\n",
    "    print(f\"📥 Loading {csv_filename} into SQL table [{table_name}]...\")\n",
    "    # chunksize is used so python doesn't load all 1M rows into memory at once\n",
    "    for chunk in pd.read_csv(csv_filename, chunksize=100000):\n",
    "        chunk.to_sql(name=table_name, con=engine, if_exists=if_exists_mode, index=False)\n",
    "    print(f\"✅ Finished loading {table_name}.\")\n",
    "\n",
    "# Load tables in order (Dimensions first, Fact last)\n",
    "load_table_to_sql('dim_products.csv', 'Dim_Products')\n",
    "load_table_to_sql('dim_customers.csv', 'Dim_Customers')\n",
    "load_table_to_sql('dim_carriers.csv', 'Dim_Carriers')\n",
    "load_table_to_sql('fact_orders.csv', 'Fact_Orders')\n",
    "\n",
    "print(\"🎉 Data pipeline pipeline complete. All data resides safely inside SQL Server!\")"
   ]
  },
  {
   "cell_type": "raw",
   "id": "421ba1d8-4b83-489e-a05b-8752c4f8b6b4",
   "metadata": {},
   "source": [
    "== use it when i stuck with half field data\n",
    "server_name = 'SHIVE\\SQLEXPRESS05'\n",
    "database_name = 'ECommerce_Logistics_DB'\n",
    "\n",
    "print(\"🔌 Establishing connection to SQL Server...\")\n",
    "\n",
    "params = urllib.parse.quote_plus(\n",
    "    f\"DRIVER={{ODBC Driver 18 for SQL Server}};\"\n",
    "    f\"SERVER={server_name};\"\n",
    "    f\"DATABASE={database_name};\"\n",
    "    f\"Trusted_Connection=yes;\"\n",
    "    f\"TrustServerCertificate=yes;\"\n",
    ")\n",
    "engine = create_engine(f\"mssql+pyodbc:///?odbc_connect={params}\")\n",
    "\n",
    "# We use a clean connection to drop constraints and clear existing tables first\n",
    "with engine.connect() as conn:\n",
    "    print(\"🧹 Dropping old tables to guarantee a clean slate...\")\n",
    "    conn.execute(text(\"DROP TABLE IF EXISTS Fact_Orders;\"))\n",
    "    conn.execute(text(\"DROP TABLE IF EXISTS Dim_Products;\"))\n",
    "    conn.execute(text(\"DROP TABLE IF EXISTS Dim_Customers;\"))\n",
    "    conn.execute(text(\"DROP TABLE IF EXISTS Dim_Carriers;\"))\n",
    "    conn.commit()\n",
    "\n",
    "# --- LOAD DATA (Using 'replace' mode creates clean new tables automatically) ---\n",
    "print(\"📥 Loading Dim_Products...\")\n",
    "df_p = pd.read_csv('dim_products.csv')\n",
    "# Dropping any accidental duplicate IDs in the CSV file just in case\n",
    "df_p = df_p.drop_duplicates(subset=['Product_ID'])\n",
    "df_p.to_sql(name='dim_products', con=engine, if_exists='replace', index=False)\n",
    "\n",
    "print(\"📥 Loading Dim_Customers...\")\n",
    "df_c = pd.read_csv('dim_customers.csv')\n",
    "df_c = df_c.drop_duplicates(subset=['Customer_ID'])\n",
    "df_c.to_sql(name='dim_customers', con=engine, if_exists='replace', index=False)\n",
    "\n",
    "print(\"📥 Loading Dim_Carriers...\")\n",
    "df_car = pd.read_csv('dim_carriers.csv')\n",
    "df_car = df_car.drop_duplicates(subset=['Carrier_ID'])\n",
    "df_car.to_sql(name='dim_carriers', con=engine, if_exists='replace', index=False)\n",
    "\n",
    "print(\"📊 Loading 1,000,000 row Fact_Orders table in chunks (Please wait)...\")\n",
    "# For the massive fact table, use 'replace' on the first chunk, then 'append'\n",
    "first_chunk = True\n",
    "for chunk in pd.read_csv('fact_orders.csv', chunksize=200000):\n",
    "    if first_chunk:\n",
    "        chunk.to_sql(name='fact_orders', con=engine, if_exists='replace', index=False)\n",
    "        first_chunk = False\n",
    "    else:\n",
    "        chunk.to_sql(name='fact_orders', con=engine, if_exists='append', index=False)\n",
    "\n",
    "# --- RE-ENFORCE PRODUCTION CONSTRAINTS ---\n",
    "print(\"🛠️ Re-applying Primary Keys, Foreign Keys, and Indexes...\")\n",
    "with engine.connect() as conn:\n",
    "    # 1. Add Primary Keys to Dimension Tables\n",
    "    conn.execute(text(\"ALTER TABLE dim_products ALTER COLUMN Product_ID INT NOT NULL;\"))\n",
    "    conn.execute(text(\"ALTER TABLE dim_products ADD CONSTRAINT PK_Products PRIMARY KEY (Product_ID);\"))\n",
    "    \n",
    "    conn.execute(text(\"ALTER TABLE dim_customers ALTER COLUMN Customer_ID INT NOT NULL;\"))\n",
    "    conn.execute(text(\"ALTER TABLE dim_customers ADD CONSTRAINT PK_Customers PRIMARY KEY (Customer_ID);\"))\n",
    "    \n",
    "    conn.execute(text(\"ALTER TABLE dim_carriers ALTER COLUMN Carrier_ID VARCHAR(10) NOT NULL;\"))\n",
    "    conn.execute(text(\"ALTER TABLE dim_carriers ADD CONSTRAINT PK_Carriers PRIMARY KEY (Carrier_ID);\"))\n",
    "    \n",
    "    # 2. Add Foreign Keys to the Fact Table\n",
    "    conn.execute(text(\"ALTER TABLE fact_orders ALTER COLUMN Customer_ID INT NOT NULL;\"))\n",
    "    conn.execute(text(\"ALTER TABLE fact_orders ALTER COLUMN Product_ID INT NOT NULL;\"))\n",
    "    conn.execute(text(\"ALTER TABLE fact_orders ALTER COLUMN Carrier_ID VARCHAR(10) NOT NULL;\"))\n",
    "    \n",
    "    conn.execute(text(\"ALTER TABLE fact_orders ADD CONSTRAINT FK_Fact_Customers FOREIGN KEY (Customer_ID) REFERENCES dim_customers(Customer_ID);\"))\n",
    "    conn.execute(text(\"ALTER TABLE fact_orders ADD CONSTRAINT FK_Fact_Products FOREIGN KEY (Product_ID) REFERENCES dim_products(Product_ID);\"))\n",
    "    conn.execute(text(\"ALTER TABLE fact_orders ADD CONSTRAINT FK_Fact_Carriers FOREIGN KEY (Carrier_ID) REFERENCES dim_carriers(Carrier_ID);\"))\n",
    "    \n",
    "    conn.commit()\n",
    "\n",
    "print(\"🎉 DATABASE PIPELINE COMPLETE! 1,000,000 rows fully loaded with proper constraints.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0db537f2-0f5c-41c7-bc78-e582b82e9e84",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7c606ff1-ff81-44e6-9d38-53c77d0fed55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['SQL Server']\n"
     ]
    }
   ],
   "source": [
    "import pyodbc\n",
    "print([x for x in pyodbc.drivers() if 'SQL Server' in x])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "10c99918-99c7-443e-825f-0c8f87c19617",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
