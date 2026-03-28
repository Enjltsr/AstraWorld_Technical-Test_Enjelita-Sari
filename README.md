# AstraWorld_Technical-Test_Enjelita-Sari

# Astra Tech Test — Data Engineering Project

## Overview

This project is built to solve a data engineering case involving daily data ingestion, data cleaning, and datamart creation.

The solution is designed using a simple yet scalable architecture that separates raw data, cleaned data, and analytical data layers to ensure maintainability and data quality.

---

## Architecture

The data pipeline is structured into three main layers:

### Raw Layer

Stores raw data ingested directly from source files without any transformation.

* `customers_raw`
* `sales_raw`
* `after_sales_raw`
* `customer_addresses`

### Staging / Clean Layer

Handles data cleaning and transformation such as:

* Standardizing date formats
* Cleaning numeric values
* Handling null or invalid data

Tables:

* `customers_clean`
* `sales_clean`
* `after_sales_clean`

### Datamart Layer

Prepared for reporting and analysis:

* `dm_sales`
* `dm_service`

---

## Data Pipeline Flow

```text
CSV Files → Python ETL (Docker) → MySQL (Raw)
          → Data Cleaning (SQL) → Clean Tables
          → Aggregation → Datamart
```

---

## Tech Stack

* Python (Pandas, SQLAlchemy)
* MySQL
* Docker & Docker Compose
* SQL

---

## Task 1 — Data Landing

A Python-based ETL pipeline is implemented to ingest daily CSV files into MySQL.

Key features:

* Automatically detects new files in `/data`
* Loads data into corresponding tables
* Moves processed files to `/archive`
* Prevents duplicate ingestion (idempotent process)
* Includes retry mechanism for database readiness

---

## Task 2 — Data Cleaning & Datamart

### Data Cleaning

Performed using SQL scripts:

* Standardize `dob` format
* Clean `price` column
* Filter invalid records
* Classify customer type

### Datamart

Two reports are generated:

1. **Sales Summary**

   * Aggregation by month, price class, and model

2. **Service Summary**

   * Count of services per vehicle
   * Customer priority classification

---

## Project Structure

```
astra_techtest/
│
├── data/                # Incoming CSV files
├── archive/             # Processed files
├── sql/                 # SQL scripts (cleaning & datamart)
├── etl.py               # ETL pipeline
├── docker-compose.yml
├── requirements.txt
```

---

## How to Run

### 1. Start Docker

```
docker-compose up --build
```

### 2. Run ETL

The ETL pipeline will:

* Detect CSV files
* Load into MySQL
* Move files to archive

### 3. Run SQL Scripts

Execute SQL scripts in order:

1. Cleaning scripts
2. Datamart scripts

(SQL can be executed using DBeaver or any SQL client)

---

## Key Highlights

* Implements idempotent data pipeline using file archiving
* Handles inconsistent data formats (e.g., multiple date formats)
* Separates data layers for better maintainability
* Designed with scalability in mind

---

## Future Improvements

* Add orchestration tool (Airflow)
* Automate SQL execution within pipeline
* Add data validation layer
* Connect to BI tools for visualization

---

## Author

Developed as part of a technical test submission.

---
