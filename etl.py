import pandas as pd
import glob
import os
import time
import shutil
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

print("Starting ETL...")

for i in range(10):
    try:
        engine = create_engine("mysql+pymysql://root:root@mysql:3306/maju_jaya")
        conn = engine.connect()
        conn.close()
        print("MySQL ready")
        break
    except OperationalError:
        print("waiting MySQL...")
        time.sleep(5)

files = glob.glob("data/*.csv")

for file in files:
    try:
        print(f"Processing: {file}")
        df = pd.read_csv(file)

        table_name = os.path.basename(file).replace(".csv", "")

        #cleaning database
        if table_name == "customers_raw":
            df["dob"] = pd.to_datetime(df["dob"], errors="coerce", dayfirst=True)

        elif table_name == "sales_raw":
            df["price"] = df["price"].str.replace(".", "", regex=False)
            df["price"] = pd.to_numeric(df["price"], errors="coerce")

        elif table_name == "after_sales_raw":
            df = df[df["vin"].notna()]

        elif table_name == "customer_addresses":
            df["city"] = df["city"].str.title()
            df["province"] = df["province"].str.title()

        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded into {table_name}")

        print(f"inserting into table: {table_name}")
        print(f"columns: {list(df.columns)}")

        shutil.move(file, f"archive/{os.path.basename(file)}")

    except Exception as e:
        print(f"Error {file}: {e}")