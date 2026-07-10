WITH customers AS (
    SELECT * FROM {{ ref('stg_customers') }}
),

orders AS (
    SELECT * FROM {{ ref('stg_orders') }}
),

payments AS (
    SELECT 
        order_id,
        SUM(payment_amount) AS total_order_amount
    FROM {{ ref('stg_payments') }}
    GROUP BY order_id
),

-- 1. Menggabungkan data transaksi pelanggan
customer_transactions AS (
    SELECT
        c.customer_unique_id,
        o.order_id,
        o.order_date,
        p.total_order_amount
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    LEFT JOIN payments p ON o.order_id = p.order_id
),

-- 2. Menghitung Nilai Agregat RFM per Pelanggan
customer_rfm_raw AS (
    SELECT
        customer_unique_id,
        -- Recency: Jumlah hari sejak pembelian terakhir dari tanggal maksimal di dataset
        DATEDIFF('day', MAX(order_date), (SELECT MAX(order_date) FROM orders)) AS recency,
        -- Frequency: Total jumlah pesanan unik
        COUNT(DISTINCT order_id) AS frequency,
        -- Monetary: Total uang yang dibelanjakan (CLV awal)
        SUM(total_order_amount) AS monetary
    FROM customer_transactions
    GROUP BY customer_unique_id
)

-- 3. Final Query untuk menyajikan data ke Dashboard
SELECT
    customer_unique_id,
    recency,
    frequency,
    COALESCE(monetary, 0) AS monetary,
    
    -- Memberikan skor otomatis 1-5 menggunakan fungsi NTILE (Statistik Industri)
    -- Skor 5 adalah yang terbaik (paling baru belanja, paling sering, paling banyak belanja)
    NTILE(5) OVER (ORDER BY recency DESC) AS r_score, -- Semakin kecil recency, skor semakin tinggi
    NTILE(5) OVER (ORDER BY frequency ASC) AS f_score,
    NTILE(5) OVER (ORDER BY monetary ASC) AS m_score
FROM customer_rfm_raw