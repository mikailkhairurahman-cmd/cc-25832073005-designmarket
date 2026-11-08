# ADR-0001: Initial Architecture DesignMarket

- Status: Accepted
- Date: 2026-11-08
- Project: DesignMarket — Marketplace Jasa Desain

## Context
DesignMarket merupakan proyek marketplace jasa desain berbasis web yang bertujuan menghubungkan pelanggan dengan desainer independen.

Pada tahap M03, diperlukan arsitektur sederhana yang dapat dijalankan pada VPS dengan sumber daya terbatas, mudah dipahami, dan mendukung deployment yang dapat direproduksi.

## Decision
Arsitektur awal DesignMarket menggunakan:

1. Ubuntu Server 24.04 LTS sebagai sistem operasi VPS.
2. Python dan Flask sebagai framework aplikasi web.
3. Gunicorn sebagai WSGI application server.
4. systemd untuk mengelola proses aplikasi.
5. Caddy sebagai reverse proxy untuk akses HTTP publik.
6. UFW sebagai firewall dasar VPS.
7. GitHub sebagai repository kode sumber dan dokumentasi.

Alur akses publik:

Browser → Caddy (port 80) → Gunicorn (127.0.0.1:8000) → Flask.

## Alternatives Considered
- **Django:** menyediakan fitur bawaan yang lebih lengkap, tetapi menambah kompleksitas untuk baseline M03.
- **Node.js dan Express:** dapat digunakan untuk aplikasi web, tetapi memerlukan penyesuaian dari stack referensi modul.
- **Nginx:** alternatif reverse proxy yang umum, tetapi Caddy dipilih untuk mengikuti stack referensi modul.
- **Docker:** mendukung isolasi aplikasi, tetapi containerization belum termasuk cakupan M03.

## Consequences

### Positive
- Arsitektur relatif sederhana dan sesuai kebutuhan baseline M03.
- Proses aplikasi dapat dikelola menggunakan systemd.
- Backend tidak perlu diekspos langsung ke internet.
- Repository dapat digunakan sebagai sumber deployment dan dokumentasi.

### Negative
- Fitur marketplace belum lengkap pada tahap M03.
- Belum menggunakan database produksi.
- Deployment awal masih memerlukan konfigurasi server manual.
- Akses publik M03 masih menggunakan HTTP, sehingga belum sesuai untuk transaksi dan data sensitif nyata.

## Future Development
Pada pertemuan berikutnya, sistem direncanakan menambahkan domain dan HTTPS, database, autentikasi pengguna, fitur pemesanan, pembayaran, komisi marketplace, serta otomatisasi deployment sesuai cakupan modul.
  
