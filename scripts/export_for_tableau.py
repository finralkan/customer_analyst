import duckdb
import os

# Folder Utama
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, 'olist_warehouse.duckdb')
output_csv = os.path.join(BASE_DIR, 'data', 'processed', 'mart_customer_rfm.csv')

# Koneksi database Duckdb
con = duckdb.connect(db_path)

print("Mengekspor tabel ke CSV")

try:
    # Membaca data mart dari dbt dan menyimpannya langsung menjadi file CSV
    con.execute(f"COPY (SELECT * FROM mart_customer_rfm) TO '{output_csv}' (HEADER, DELIMITER ',')")
    print(f"Data berhasil diekspor ke: {output_csv}")
except Exception as e:
    print(f"Gagal mengekspor data: {e}")

con.close()