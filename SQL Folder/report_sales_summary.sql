SELECT
    DATE_FORMAT(invoice_date, '%Y-%m') AS periode,
    CASE
        WHEN price BETWEEN 100000000 AND 250000000 THEN 'LOW'
        WHEN price BETWEEN 250000001 AND 400000000 THEN 'MEDIUM'
        ELSE 'HIGH'
    END AS class,
    model,
    SUM(price) AS total
FROM sales_clean
GROUP BY periode, class, model
ORDER BY periode;
