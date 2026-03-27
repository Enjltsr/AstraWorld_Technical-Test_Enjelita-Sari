SELECT
    DATE_FORMAT(a.service_date, '%Y') AS periode,
    a.vin,
    c.name AS customer_name,
    ca.address,
    COUNT(a.service_ticket) AS count_service,
    CASE
        WHEN COUNT(a.service_ticket) > 10 THEN 'HIGH'
        WHEN COUNT(a.service_ticket) BETWEEN 5 AND 10 THEN 'MED'
        ELSE 'LOW'
    END AS priority
FROM after_sales_clean a
LEFT JOIN customers_clean c
    ON a.customer_id = c.customer_id
LEFT JOIN customer_addresses ca
    ON a.customer_id = ca.customer_id
GROUP BY a.vin, c.name, ca.address, periode;
