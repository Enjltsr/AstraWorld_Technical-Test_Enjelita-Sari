CREATE TABLE after_sales_clean AS
SELECT *
FROM after_sales_raw
WHERE vin IS NOT NULL;
