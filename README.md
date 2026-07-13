# Dashboard Customer Analytics with RFM Analytics Pipeline

<img width="1435" height="786" alt="Screenshot 2026-07-13 at 14 39 05" src="https://github.com/user-attachments/assets/bb05eaca-9926-48d7-bbcc-68e460570b7d" />


**Live Dashboard: (tableau public still maintenance, stay tune for links)**

## Deskripsi :
Di industri ecommerce healthcare, mencari pelanggan baru mengeluarkan biaya yang lebih mahal dibandingkan mempertahankan pelanggan lama. Pelanggan pada ecommerce healthcare merupakan Rumah Sakit atau Klinik, sehingga diperlukan analisa untuk menentukan segmentasi pelanggan agar perlakuan yang akan diberikan tepat sasaran. Dalam proyek ini menggunakan pemodelan RFM, dalam menentukan segmen pelanggan.

Sistem ini dibangun menggunakan arsitektur **Local Modern Data Stack**, memastikan data mentah ditransformasikan menjadi metrik bisnis dengan pengujian kualitas data.

## Tech Stack & Arsitektur
Proyek ini mengimplementasikan alur kerja *Extract, Load, Transform* (ELT) :
* **Data Warehouse:** DuckDB (Lokal database)
* **Data Transformation:** dbt-core (Staging & Data Marts)
* **Data Ingestion & Scripting:** Python (Pandas, DuckDB API)
* **Data Visualization:** Tableau Public
* **Version Control:** Git & GitHub

**Data Lineage:**
`FTP .csv file` -> `Python Ingestion` -> `DuckDB (Raw)` -> `dbt (Staging)` -> `dbt (RFM Data Mart)` -> `Tableau (Dashboard)`

## Rekomendasi Bisnis
Berdasarkan analisis segmentasi RFM pada dataset, ditemukan beberapa *insight* utama:
1. **Pelanggan Prioritas:** Kelompok ini menyumbang margin pendapatan terbesar dan sering melakukan transaksi dalam waktu dekat. **Aksi:** Pemberian akses eksklusif ke produk baru serta program *Loyalty Customer*.
2. **Potensi Pelanggan Hilang (Calon Pelanggan Prioritas):** Pelanggan dengan nilai *Monetary* tertinggi namun jarang melakukan transaksi. **Aksi:** Melakukan strategi kampanye yang terpersonalisasi dengan diskon agresif dan menarik sehingga tidak beralih ke kompetitor.
3. **Pelanggan Hilang:** Merupakan pelanggan sekali beli dan tidak melakukan transaksi kembali dalam jangka waktu yang sangat lama. **Aksi:** Hentikan alokasi anggaran untuk menargetkan iklan yang terpersonalisasi, hanya gunakan iklan umum seperti penawaran pada produk-produk umum melalui channel Whatsapp guna mengoptimalkan anggaran.
