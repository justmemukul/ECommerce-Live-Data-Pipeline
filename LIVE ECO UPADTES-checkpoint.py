{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "cb68e5b1-2012-4711-9500-ccdb56ffccfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyodbc in c:\\users\\monkey\\anaconda3\\lib\\site-packages (5.3.0)\n",
      "Requirement already satisfied: pandas in c:\\users\\monkey\\anaconda3\\lib\\site-packages (2.3.3)\n",
      "Requirement already satisfied: numpy>=1.26.0 in c:\\users\\monkey\\anaconda3\\lib\\site-packages (from pandas) (2.3.5)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\monkey\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\monkey\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\monkey\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\monkey\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
      "✅ Libraries imported successfully!\n"
     ]
    }
   ],
   "source": [
    "# Cell 1: Prerequisites\n",
    "!pip install pyodbc pandas\n",
    "import pyodbc\n",
    "import pandas as pd\n",
    "import random\n",
    "import time\n",
    "from datetime import datetime\n",
    "print(\"✅ Libraries imported successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "61e8575c-d4a7-439e-9f49-0ba4f56982c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🔗 Connection path configured.\n"
     ]
    }
   ],
   "source": [
    "# Cell 2: Database Connection Parameters\n",
    "CONN_STR = (\n",
    "    \"DRIVER={SQL Server};\"\n",
    "    \"SERVER=SHIVE\\\\SQLEXPRESS05;\"  \n",
    "    \"DATABASE=ECommerce_Logistics_DB;\"  # Adjust to your exact database name if needed\n",
    "    \"Trusted_Connection=yes;\"\n",
    ")\n",
    "\n",
    "print(\"🔗 Connection path configured.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4c8961f3-736b-476d-9fe5-82b707b82961",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\monkey\\AppData\\Local\\Temp\\ipykernel_3716\\3638637784.py:5: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.\n",
      "  df_orders = pd.read_sql(query, conn)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ SQL Server Connection Successful!\n",
      "📊 Previewing the latest 5 transactions:\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order_ID</th>\n",
       "      <th>Order_Date</th>\n",
       "      <th>Customer_ID</th>\n",
       "      <th>Product_ID</th>\n",
       "      <th>Carrier_ID</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Shipping_Cost</th>\n",
       "      <th>Order_Status</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>82201678</td>\n",
       "      <td>2025-12-31</td>\n",
       "      <td>12691</td>\n",
       "      <td>573</td>\n",
       "      <td>CR-01</td>\n",
       "      <td>1</td>\n",
       "      <td>19.31</td>\n",
       "      <td>Delivered</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>85416632</td>\n",
       "      <td>2025-12-31</td>\n",
       "      <td>48995</td>\n",
       "      <td>552</td>\n",
       "      <td>CR-02</td>\n",
       "      <td>1</td>\n",
       "      <td>8.01</td>\n",
       "      <td>Delayed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>13440711</td>\n",
       "      <td>2025-12-31</td>\n",
       "      <td>26642</td>\n",
       "      <td>926</td>\n",
       "      <td>CR-04</td>\n",
       "      <td>5</td>\n",
       "      <td>24.04</td>\n",
       "      <td>Delivered</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>12890084</td>\n",
       "      <td>2025-12-31</td>\n",
       "      <td>8795</td>\n",
       "      <td>93</td>\n",
       "      <td>CR-03</td>\n",
       "      <td>4</td>\n",
       "      <td>12.80</td>\n",
       "      <td>Delivered</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>73384001</td>\n",
       "      <td>2025-12-31</td>\n",
       "      <td>21091</td>\n",
       "      <td>700</td>\n",
       "      <td>CR-02</td>\n",
       "      <td>5</td>\n",
       "      <td>4.83</td>\n",
       "      <td>Delivered</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Order_ID  Order_Date  Customer_ID  Product_ID Carrier_ID  Quantity  \\\n",
       "0  82201678  2025-12-31        12691         573      CR-01         1   \n",
       "1  85416632  2025-12-31        48995         552      CR-02         1   \n",
       "2  13440711  2025-12-31        26642         926      CR-04         5   \n",
       "3  12890084  2025-12-31         8795          93      CR-03         4   \n",
       "4  73384001  2025-12-31        21091         700      CR-02         5   \n",
       "\n",
       "   Shipping_Cost Order_Status  \n",
       "0          19.31    Delivered  \n",
       "1           8.01      Delayed  \n",
       "2          24.04    Delivered  \n",
       "3          12.80    Delivered  \n",
       "4           4.83    Delivered  "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Cell 3: Pipeline Handshake & Verification Test\n",
    "try:\n",
    "    conn = pyodbc.connect(CONN_STR)\n",
    "    query = \"SELECT TOP 5 * FROM v_Fact_Orders ORDER BY Order_Date DESC\"\n",
    "    df_orders = pd.read_sql(query, conn)\n",
    "    \n",
    "    print(\"✅ SQL Server Connection Successful!\")\n",
    "    print(f\"📊 Previewing the latest {len(df_orders)} transactions:\")\n",
    "    display(df_orders.head()) # Using display() looks beautiful in Jupyter\n",
    "    conn.close()\n",
    "except Exception as e:\n",
    "    print(f\"❌ Extraction Error: {str(e)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7db1fde-989c-44d7-a410-6333274bed4d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🚀 Starting Live Transaction Simulator... Click 'Stop' ◼️ in Jupyter to pause.\n",
      "\n",
      "📦 [Sale #1] 2026-05-30 | Order ID: 92543109 | Product ID: 599 | Status: Delayed -> Pushed to SQL Server!\n",
      "📦 [Sale #2] 2026-05-30 | Order ID: 59526434 | Product ID: 790 | Status: Returned -> Pushed to SQL Server!\n",
      "📦 [Sale #3] 2026-05-30 | Order ID: 79769113 | Product ID: 987 | Status: Delivered -> Pushed to SQL Server!\n",
      "📦 [Sale #4] 2026-05-30 | Order ID: 96072042 | Product ID: 544 | Status: Delayed -> Pushed to SQL Server!\n",
      "📦 [Sale #5] 2026-05-30 | Order ID: 85465700 | Product ID: 568 | Status: Returned -> Pushed to SQL Server!\n",
      "📦 [Sale #6] 2026-05-30 | Order ID: 79590340 | Product ID: 375 | Status: Delayed -> Pushed to SQL Server!\n",
      "📦 [Sale #7] 2026-05-30 | Order ID: 84103996 | Product ID: 714 | Status: Delivered -> Pushed to SQL Server!\n",
      "📦 [Sale #8] 2026-05-30 | Order ID: 76838994 | Product ID: 277 | Status: Returned -> Pushed to SQL Server!\n",
      "📦 [Sale #9] 2026-05-30 | Order ID: 94186426 | Product ID: 224 | Status: Shipped -> Pushed to SQL Server!\n",
      "📦 [Sale #10] 2026-05-30 | Order ID: 70706961 | Product ID: 952 | Status: Delayed -> Pushed to SQL Server!\n"
     ]
    }
   ],
   "source": [
    "# Cell 4: Background Real-Time E-Commerce Stream Engine\n",
    "def simulate_live_orders(iterations=50, delay_seconds=3):\n",
    "    # Valid pools based strictly on your real dimension tables shown in the screenshot\n",
    "    statuses = [\"Delivered\", \"Shipped\", \"Delayed\", \"Returned\"]\n",
    "    \n",
    "    # We will pick from existing IDs in your database to maintain star-schema data integrity\n",
    "    carrier_ids = [\"CR-01\", \"CR-02\", \"CR-03\", \"CR-04\"]\n",
    "\n",
    "    # 1. DATABASE CONNECTION SETUP (Updated to your exact database name!)\n",
    "    CONN_STR = (\n",
    "        \"DRIVER={SQL Server};\"\n",
    "        \"SERVER=localhost\\\\SQLEXPRESS05;\" # Target your exact local instance\n",
    "        \"DATABASE=ECommerce_Logistics_DB;\" # Fixed from your screenshot!\n",
    "        \"Trusted_Connection=yes;\"\n",
    "    )\n",
    "\n",
    "    conn = pyodbc.connect(CONN_STR)\n",
    "    cursor = conn.cursor()\n",
    "    print(\"🚀 Starting Live Transaction Simulator... Click 'Stop' ◼️ in Jupyter to pause.\\n\")\n",
    "\n",
    "    for i in range(1, iterations + 1):\n",
    "        # Generate data points matching your exact table constraints\n",
    "        order_id = random.randint(50000000, 99999999) # 8-digit format matching your data\n",
    "        customer_id = random.randint(1000, 49999)    # Random valid customer key range\n",
    "        product_id = random.randint(1, 999)           # Random valid product key range\n",
    "        selected_carrier = random.choice(carrier_ids)  # CR-01 to CR-04\n",
    "        quantity = random.randint(1, 5)\n",
    "        shipping_cost = round(random.uniform(5.00, 30.00), 2)\n",
    "        selected_status = random.choice(statuses)\n",
    "        \n",
    "        # Capture current live timestamp\n",
    "        current_date = datetime.now().strftime('%Y-%m-%d')\n",
    "\n",
    "        # 2. EXACT MATCHING INSERT QUERY (Only the 8 real database columns!)\n",
    "        insert_query = \"\"\"\n",
    "            INSERT INTO fact_orders \n",
    "            (Order_ID, Order_Date, Customer_ID, Product_ID, Carrier_ID, Quantity, Shipping_Cost, Order_Status)\n",
    "            VALUES (?, ?, ?, ?, ?, ?, ?, ?)\n",
    "        \"\"\"\n",
    "\n",
    "        try:\n",
    "            cursor.execute(\n",
    "                insert_query, \n",
    "                order_id, current_date, customer_id, product_id, selected_carrier, \n",
    "                quantity, shipping_cost, selected_status\n",
    "            )\n",
    "            conn.commit() # Save row permanently to your hard drive\n",
    "            print(f\"📦 [Sale #{i}] {current_date} | Order ID: {order_id} | Product ID: {product_id} | Status: {selected_status} -> Pushed to SQL Server!\")\n",
    "        except Exception as e:\n",
    "            print(f\"❌ Table Mapping Error: {str(e)}\")\n",
    "            break\n",
    "            \n",
    "        time.sleep(delay_seconds)\n",
    "\n",
    "    cursor.close()\n",
    "    conn.close()\n",
    "    print(\"\\n✅ Simulation batch complete.\")\n",
    "\n",
    "# Run the live pipeline simulation\n",
    "simulate_live_orders(iterations=50, delay_seconds=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c934ef6-9fcd-4c46-af2d-6246e027ca45",
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
