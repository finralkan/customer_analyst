import duckdb
import os
import glob

# Folder utama
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Setting database DuckDB lokal
db_path = os.path.join(BASE_DIR, 'olist_warehouse.duckdb')
con = duckdb.connect(db_path)

# Folder file CSV
csv_path = os.path.join(BASE_DIR, 'data', 'raw', '*.csv')
csv_files = glob.glob(csv_path)

print(f"Menemukan file CSV sebesar {len(csv_files)}.")

for file in csv_files:
    table_name = os.path.basename(file).replace('.csv', '').replace('olist_', '').replace('_dataset', '')
    
    try:
        # Hapus tabel jika sudah ada, dan lakukan restart
        con.execute(f"DROP TABLE IF EXISTS {table_name}")
        con.execute(f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{file}')")
        print(f"Tabel '{table_name}' berhasil dimuat.")
    except Exception as e:
        print(f"Gagal memuat {table_name}: {e}")

print("Process telah selesai")
con.close()