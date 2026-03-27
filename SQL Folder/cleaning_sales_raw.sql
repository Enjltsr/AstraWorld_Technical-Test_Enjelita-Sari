CREATE TABLE sales_clean AS
SELECT
    vin,
    customer_id,
    model,s
    invoice_date,
    CAST(REPLACE(price, '.', '') AS UNSIGNED) AS price,
    created_at
FROM sales_raw;
