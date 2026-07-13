WITH raw_payments AS (
    SELECT * FROM {{ source('olist', 'order_payments') }}
)

SELECT
    order_id,
    payment_sequential,
    payment_type,
    payment_installments,
    CAST(payment_value AS FLOAT) AS payment_amount
FROM raw_payments