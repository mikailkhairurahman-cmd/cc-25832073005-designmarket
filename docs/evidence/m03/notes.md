# Catatan Evidence M03 — DesignMarket

Nama: Mikail Khairu Rahman
NIM: 25832073005
Proyek: DesignMarket
Pertemuan: M03 — Project Inception dan First Deployment

## Lingkungan Deployment

- Cloud Provider: Microsoft Azure for Students
- Sistem Operasi: Ubuntu Server
- Aplikasi: DesignMarket
- Backend: Python Flask
- Application Server: Gunicorn
- Reverse Proxy: Caddy
- Service Manager: systemd
- Firewall: UFW
- Direktori aplikasi: /srv/cc-m03

## Hasil Pengujian

1. Aplikasi berhasil dijalankan menggunakan Gunicorn.
2. Gunicorn berjalan pada alamat 127.0.0.1:8000.
3. Caddy berhasil meneruskan permintaan HTTP ke Gunicorn.
4. Halaman utama DesignMarket berhasil diakses melalui browser.
5. Endpoint /health memberikan respons HTTP 200 OK.
6. Service designmarket berjalan dengan status active (running).
7. Firewall UFW aktif dan mengizinkan port SSH 22 serta HTTP 80.

## Evidence

- os.txt: Informasi sistem operasi.
- resources.txt: Informasi sumber daya VPS.
- ufw.txt: Status firewall.
- ports.txt: Informasi port jaringan.
- service.txt: Status service DesignMarket.
- health-internal.txt: Pengujian health endpoint lokal.
- health-public.txt: Pengujian health endpoint publik.

## Batasan M03

Aplikasi masih berupa prototipe awal marketplace jasa desain.
Data layanan masih berupa data demonstrasi.
Database produksi, transaksi nyata, domain, dan HTTPS
belum diimplementasikan pada tahap M03.

## Kesimpulan

Deployment awal DesignMarket berhasil dilakukan pada VPS
menggunakan Flask, Gunicorn, systemd, dan Caddy.
Aplikasi dapat diakses melalui HTTP publik dan endpoint
health berhasil memberikan respons HTTP 200 OK.
