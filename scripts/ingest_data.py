# import duckdb
# import os
# import glob

# # Membuat atau terhubung ke database DuckDB lokal
# db_path = 'olist_warehouse.duckdb'
# con = duckdb.connect(db_path)

# # Mencari semua file CSV di folder data/raw/
# csv_files = glob.glob('../data/raw/*.csv')

# print("Memulai proses pemuatan data ke DuckDB...")

# for file in csv_files:
#     # Mengambil nama file tanpa ekstensi untuk dijadikan nama tabel
#     table_name = os.path.basename(file).replace('.csv', '').replace('olist_', '').replace('_dataset', '')
    
#     try:
#         # Memuat CSV langsung ke DuckDB (sangat efisien memori)
#         con.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM read_csv_auto('{file}')")
#         print(f"✅ Tabel '{table_name}' berhasil dimuat.")
#     except Exception as e:
#         print(f"❌ Gagal memuat {table_name}: {e}")

# print("Proses selesai! Database siap digunakan.")
# con.close()

# New Solution

import duckdb
import os
import glob

# Memastikan jalur selalu mengarah ke folder utama proyek
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Membuat atau terhubung ke database DuckDB lokal
db_path = os.path.join(BASE_DIR, 'olist_warehouse.duckdb')
con = duckdb.connect(db_path)

# Mencari file CSV menggunakan jalur absolut
csv_path = os.path.join(BASE_DIR, 'data', 'raw', '*.csv')
csv_files = glob.glob(csv_path)

print(f"Menemukan {len(csv_files)} file CSV. Memulai pemuatan...")

for file in csv_files:
    table_name = os.path.basename(file).replace('.csv', '').replace('olist_', '').replace('_dataset', '')
    
    try:
        # Hapus tabel jika sudah ada (agar bersih), lalu muat ulang
        con.execute(f"DROP TABLE IF EXISTS {table_name}")
        con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{file}')")
        print(f"✅ Tabel '{table_name}' berhasil dimuat.")
    except Exception as e:
        print(f"❌ Gagal memuat {table_name}: {e}")

print("Proses selesai! Database siap digunakan.")
con.close()