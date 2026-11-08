# Requirements — DesignMarket

## Problem Statement
Pelanggan membutuhkan platform terpusat untuk menemukan desainer, membandingkan layanan, dan melakukan pemesanan desain. Desainer independen membutuhkan media untuk memasarkan keterampilan dan memperoleh pelanggan.

DesignMarket merupakan proyek marketplace jasa desain berbasis web yang direncanakan untuk menghubungkan pelanggan dan desainer melalui satu platform digital.

## Target Users
- Pelanggan: mencari layanan desain dan melakukan pemesanan.
- Desainer: menawarkan layanan dan mengelola pesanan.
- Admin: mengawasi pengguna, layanan, dan pesanan.
- Owner: memantau aktivitas marketplace dan transaksi.

## Functional Requirements
- FR-01: Menampilkan halaman utama marketplace.
- FR-02: Menyediakan endpoint /health.
- FR-03: Menampilkan metadata aplikasi.
- FR-04: Menampilkan katalog contoh layanan desain.
- FR-05: Registrasi dan login pelanggan/desainer (pengembangan lanjutan).
- FR-06: Pengelolaan profil dan portofolio desainer (pengembangan lanjutan).
- FR-07: Pemesanan layanan desain (pengembangan lanjutan).
- FR-08: Pengelolaan status pesanan (pengembangan lanjutan).
- FR-09: Pencatatan pembayaran dan komisi (pengembangan lanjutan).
- FR-10: Laporan transaksi untuk Owner (pengembangan lanjutan).

## Non-Functional Requirements
- NFR-01: Backend hanya diakses melalui loopback 127.0.0.1.
- NFR-02: Proses aplikasi dikelola oleh systemd.
- NFR-03: Caddy digunakan sebagai reverse proxy.
- NFR-04: Secret dan private key tidak disimpan dalam repository.
- NFR-05: Endpoint /health mengembalikan HTTP 200 saat aplikasi sehat.
- NFR-06: Deployment dapat direproduksi dari repository GitHub.
- NFR-07: Aplikasi dirancang untuk VPS baseline 1 vCPU, RAM 1 GB, dan disk 20 GB.

## In Scope M03
- Repository GitHub dan dokumentasi proyek.
- Arsitektur awal dan ADR.
- Aplikasi Flask sederhana dengan halaman utama dan katalog contoh.
- Endpoint health dan metadata aplikasi.
- Deployment melalui Gunicorn, systemd, dan Caddy pada VPS Ubuntu Server 24.04.
- Pengamanan SSH, firewall, dan pengumpulan evidence.

## Out of Scope M03
- Database produksi.
- Registrasi dan login pengguna secara penuh.
- Pemesanan dan pembayaran nyata.
- Sistem komisi otomatis.
- Docker, Infrastructure as Code, dan CI/CD.
- Domain dan HTTPS produksi.
  
