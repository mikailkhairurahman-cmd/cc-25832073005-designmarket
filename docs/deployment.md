# Deployment Plan — DesignMarket

## 1. Informasi Proyek

- Nama proyek: DesignMarket
- Jenis aplikasi: Marketplace Jasa Desain
- Mata kuliah: Cloud Computing
- Pertemuan: M03 — Project Inception
- Nama: Mikail Khairu Rahman
- NIM: 25832073005
- Kelas: PTI 2A
- Status: Perencanaan deployment (belum diuji pada VPS)

## 2. Tujuan Deployment

Melakukan deployment awal aplikasi DesignMarket pada
VPS Ubuntu Server 24.04 LTS agar dapat diakses melalui
alamat IP publik menggunakan protokol HTTP.

Pada tahap M03, aplikasi menyediakan halaman utama,
contoh katalog jasa desain, endpoint /health, dan
endpoint /api/info.

Fitur marketplace seperti autentikasi, transaksi,
pembayaran, dan database persisten belum menjadi
bagian implementasi M03.

## 3. Spesifikasi Lingkungan

Spesifikasi VPS referensi:
- Sistem operasi: Ubuntu Server 24.04 LTS
- CPU: 1 vCPU
- RAM: 1 GB
- Penyimpanan: 20 GB
- Jaringan: Public IPv4

Komponen aplikasi:
- Python 3
- Flask
- Gunicorn
- systemd
- Caddy
- UFW
- Git dan GitHub

Spesifikasi aktual VPS akan dicatat setelah
infrastruktur berhasil disiapkan.

## 4. Arsitektur Deployment

Pengguna / Browser
        |
        | HTTP Port 80
        v
    Public IP VPS
        |
        v
       Caddy
  (Reverse Proxy)
        |
        | 127.0.0.1:8000
        v
      Gunicorn
        |
        v
    Flask App
    (DesignMarket)

Gunicorn hanya menerima koneksi melalui loopback.
Caddy menjadi pintu masuk HTTP dari jaringan publik.

## 5. Persiapan VPS

Langkah yang direncanakan:

1. Menyediakan VPS Ubuntu Server 24.04 LTS.
2. Melakukan login SSH awal.
3. Memverifikasi sistem operasi dan sumber daya.
4. Memperbarui paket sistem.
5. Mengatur hostname dan zona waktu.
6. Membuat pengguna non-root dengan akses sudo.
7. Mengonfigurasi autentikasi SSH menggunakan key.
8. Mengamankan konfigurasi SSH setelah akses
   pengguna non-root berhasil diverifikasi.
9. Mengaktifkan UFW untuk SSH dan HTTP.
10. Memasang Git, Python, dan dependensi aplikasi.

Pengaturan SSH harus diuji sebelum menonaktifkan
login root atau autentikasi password untuk
menghindari kehilangan akses ke VPS.

## 6. Repository Aplikasi

Repository GitHub:

https://github.com/mikailkhairurrahman-cmd/cc-25832073005-designmarket

Rencana direktori deployment:

/srv/cc-m03

Repository akan di-clone ke VPS menggunakan metode
autentikasi GitHub yang sesuai.

File rahasia dan private key tidak boleh disimpan
di repository publik.

## 7. Instalasi Aplikasi

Langkah yang direncanakan:

1. Clone repository ke /srv/cc-m03.
2. Membuat virtual environment Python.
3. Menginstal dependensi dari requirements.txt.
4. Memeriksa konfigurasi aplikasi.
5. Menguji halaman utama dan endpoint internal.

Perintah instalasi Python yang direncanakan:

    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt

Pengujian aplikasi dilakukan sebelum layanan
dikonfigurasi untuk berjalan otomatis.

## 8. Konfigurasi Gunicorn dan systemd

Gunicorn direncanakan berjalan pada:

127.0.0.1:8000

Aplikasi Flask akan dijalankan melalui Gunicorn.

systemd digunakan untuk:
- Menjalankan aplikasi sebagai layanan.
- Mengelola proses aplikasi.
- Menjalankan ulang layanan saat diperlukan.
- Menyediakan log melalui journalctl.
- Mendukung startup otomatis setelah reboot.

Nama layanan yang direncanakan:

designmarket.service

## 9. Konfigurasi Caddy

Caddy digunakan sebagai reverse proxy yang menerima
permintaan HTTP pada port 80 dan meneruskannya
ke Gunicorn.

Rencana konfigurasi Caddyfile:

    :80 {
        encode zstd gzip
        reverse_proxy 127.0.0.1:8000
    }

HTTPS dan domain akan dikonfigurasi pada tahap M04,
bukan sebagai target utama M03.

## 10. Konfigurasi Firewall

Aturan firewall yang direncanakan:

- SSH: diizinkan untuk administrasi VPS.
- HTTP port 80: diizinkan untuk akses publik.
- Port 8000: tidak dibuka ke jaringan publik.

Aturan aktual akan diverifikasi menggunakan UFW.

## 11. Rencana Pengujian

Pengujian yang akan dilakukan:

1. Memastikan service systemd aktif.
2. Memastikan Gunicorn berjalan pada loopback.
3. Memastikan Caddy aktif pada port 80.
4. Memastikan firewall sesuai kebutuhan.
5. Mengakses halaman utama melalui IP publik.
6. Menguji endpoint /health.
7. Menguji endpoint /api/info.
8. Memastikan /health mengembalikan HTTP 200.
9. Memeriksa log apabila terjadi kegagalan.

Semua hasil pengujian harus dicatat berdasarkan
output nyata dari VPS.

## 12. Evidence M03

Bukti yang direncanakan disimpan di:

docs/evidence/m03/

Daftar evidence:

- os.txt
- resources.txt
- ufw.txt
- ports.txt
- service.txt
- health-internal.txt
- health-public.txt
- notes.md

Evidence hanya akan dibuat berdasarkan hasil
pemeriksaan aktual setelah deployment.

## 13. Risiko dan Mitigasi

Risiko: Kehilangan akses SSH.
Mitigasi: Uji login pengguna non-root sebelum
menonaktifkan metode login awal.

Risiko: Aplikasi tidak dapat diakses.
Mitigasi: Periksa systemd, Gunicorn, Caddy,
firewall, dan alamat IP publik.

Risiko: VPS kehabisan sumber daya.
Mitigasi: Pantau RAM, CPU, dan penyimpanan.

Risiko: Informasi rahasia masuk GitHub.
Mitigasi: Gunakan .gitignore dan hindari
menyimpan credential pada repository.

## 14. Status Deployment

Status saat dokumen dibuat:

- Repository GitHub: sudah dibuat.
- Dokumentasi requirements: sudah dibuat.
- Dokumentasi architecture: sudah dibuat.
- ADR-0001: sudah dibuat.
- Aplikasi Flask awal: sudah dibuat di repository.
- Deployment VPS: belum dilakukan.
- Pengujian HTTP publik: belum dilakukan.
- Evidence VPS: belum tersedia.
- Tag/release m03: belum dibuat.

Status akan diperbarui setelah setiap tahap
implementasi dan pengujian selesai.
