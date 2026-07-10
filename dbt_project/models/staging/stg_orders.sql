WITH raw_orders AS (
    SELECT * FROM {{ source('olist', 'orders') }}
)

SELECT
    order_id,
    customer_id,
    order_status,
    -- Mengubah tipe data string/text menjadi TIMESTAMP agar bisa dianalisis berdasarkan waktu
    CAST(order_purchase_timestamp AS TIMESTAMP) AS order_date,
    CAST(order_approved_at AS TIMESTAMP) AS approved_at,
    CAST(order_delivered_customer_date AS TIMESTAMP) AS delivered_at
FROM raw_orders
-- Di dunia nyata, analisis retensi biasanya hanya berfokus pada pesanan yang berhasil dikirim
WHERE order_status = 'delivered'