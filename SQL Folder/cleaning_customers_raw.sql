CREATE TABLE customers_clean AS
SELECT 
    id AS customer_id,
    name,                      
    CASE 
        WHEN CAST(dob AS CHAR) LIKE '%/%/%' 
            THEN STR_TO_DATE(CAST(dob AS CHAR), '%d/%m/%Y')
        WHEN CAST(dob AS CHAR) LIKE '%-%-%' 
            THEN STR_TO_DATE(CAST(dob AS CHAR), '%Y-%m-%d')
        ELSE NULL 
    END AS dob,                
    created_at,               
    CASE 
        WHEN name LIKE 'PT%' THEN 'Corporate'
        ELSE 'Individual' 
    END AS customer_type   
FROM customers_raw;
