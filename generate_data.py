import pandas as pd
import random
from datetime import datetime, timedelta

def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

names = ["Antonio", "Brandon", "Charlie", "Dominikus", "Erik"]
companies = ["PT Maju Jaya", "PT Black Bird", "PT Sejahtera"]

models = ["RAIZA", "RANGGO", "INNAVO", "VELOS"]

cities = ["Bekasi", "Tangerang Selatan", "Jakarta Pusat", "Jakarta Utara"]
provinces = ["Jawa Barat", "DKI Jakarta"]

#Tabel Customer
customers = []

for i in range(1, 101):
    name = random.choice(names + companies)

    # DOB error variations
    dob_type = random.choice(["normal", "slash", "random", "null"])

    if dob_type == "normal":
        dob = random_date(datetime(1980,1,1), datetime(2005,1,1)).strftime("%Y-%m-%d")
    elif dob_type == "slash":
        dob = random_date(datetime(1980,1,1), datetime(2005,1,1)).strftime("%d/%m/%Y")
    elif dob_type == "random":
        dob = "1900-01-01"
    else:
        dob = None

    customers.append({
        "id": i,
        "name": name,
        "dob": dob,
        "created_at": datetime.now()
    })

df_customers = pd.DataFrame(customers)
df_customers.to_csv("data/customers_raw.csv", index=False)

#Tabel Sales
sales = []

for i in range(1, 101):
    price = random.randint(200, 700) * 1000000

    # format harga salah (pakai titik)
    price_str = f"{price:,}".replace(",", ".")

    sales.append({
        "vin": f"VIN{i:04}",
        "customer_id": random.randint(1, 100),
        "model": random.choice(models),
        "invoice_date": random_date(datetime(2025,1,1), datetime(2025,12,31)),
        "price": price_str,
        "created_at": datetime.now()
    })

df_sales = pd.DataFrame(sales)
df_sales.to_csv("data/sales_raw.csv", index=False)

#Tabel after sales
after_sales = []

for i in range(1, 101):
    # kadang VIN ga ada di sales
    vin = random.choice([f"VIN{random.randint(1,100):04}", f"UNKNOWN{i}"])

    after_sales.append({
        "service_ticket": f"T{i:04}",
        "vin": vin,
        "customer_id": random.randint(1, 100),
        "model": random.choice(models),
        "service_date": random_date(datetime(2025,1,1), datetime(2026,12,31)),
        "service_type": random.choice(["BP", "PM", "GR"]),
        "created_at": datetime.now()
    })

df_after = pd.DataFrame(after_sales)
df_after.to_csv("data/after_sales_raw.csv", index=False)

#Customer addresses
addresses = []

for i in range(1, 101):
    addresses.append({
        "id": i,
        "customer_id": random.randint(1, 100),
        "address": f"Jalan No {random.randint(1,100)}",
        "city": random.choice(cities),
        "province": random.choice(provinces),
        "created_at": datetime.now()
    })

df_addr = pd.DataFrame(addresses)
df_addr.to_csv("data/customer_addresses.csv", index=False)

print("RAW DATA GENERATED (100 rows each)")