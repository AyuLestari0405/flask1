# Flask Project

Project ini berisi dua bagian utama yang berjalan dalam satu aplikasi Flask:

- Hello Flask: halaman dasar dan route latihan seperti home, about, users, profile, nilai, dan mahasiswa.
- Sleep Debt Calculator: fitur untuk menghitung utang tidur melalui halaman web dan endpoint API.

## Struktur Singkat

```text
flask/
|-- app.py
|-- requirements.txt
|-- templates/
|   |-- home.html
|   |-- about.html
|   |-- data.html
|   |-- mahasiswa.html
|   |-- nilai.html
|   |-- profile.html
|   |-- users.html
|   `-- sleep_debt/
|       |-- index.html
|       `-- info.html
|-- static/
|   `-- sleep_debt/
|       `-- style.css
`-- sleep_debt_calculator/
		|-- app.py
		|-- templates/
		`-- static/
```

## Persiapan

Pastikan Python sudah terpasang. Disarankan menggunakan virtual environment yang ada di project ini.

## Install Dependency

Jalankan perintah berikut dari folder project:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Jika PowerShell menolak menjalankan script, jalankan ini sekali pada terminal yang sama:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Menjalankan Aplikasi Hello Flask

Semua route utama dijalankan dari file berikut:

```powershell
python app.py
```

Jika berhasil, Flask biasanya berjalan di alamat berikut:

```text
http://127.0.0.1:5000/
```

Route yang bisa dibuka:

- Home: `http://127.0.0.1:5000/`
- About: `http://127.0.0.1:5000/about`
- Data: `http://127.0.0.1:5000/data`
- Users: `http://127.0.0.1:5000/users`
- Users dengan role: `http://127.0.0.1:5000/users-role`
- Profile dinamis: `http://127.0.0.1:5000/profile/NamaAnda`
- Nilai: `http://127.0.0.1:5000/nilai/85`
- Mahasiswa: `http://127.0.0.1:5000/mahasiswa`

## Menjalankan Sleep Debt Calculator

Fitur Sleep Debt juga dijalankan melalui file utama yang sama:

```powershell
python app.py
```

Setelah server aktif, buka halaman berikut di browser:

- Halaman utama Sleep Debt: `http://127.0.0.1:5000/sleep-debt`
- Halaman info Sleep Debt: `http://127.0.0.1:5000/sleep-debt/info`

Endpoint API untuk menghitung sleep debt:

- POST `http://127.0.0.1:5000/sleep-debt/calculate`

Contoh request dengan PowerShell:

```powershell
$body = '{"hours_needed":8,"hours_actual":5}'
Invoke-RestMethod -Uri "http://127.0.0.1:5000/sleep-debt/calculate" `
	-Method Post `
	-ContentType "application/json" `
	-Body $body
```

## Catatan Penting

- File `sleep_debt_calculator/app.py` saat ini bukan entry point utama untuk dijalankan langsung.
- Untuk membuka Hello Flask dan Sleep Debt, gunakan `app.py` yang ada di root project.
- Jika port 5000 sedang dipakai proses lain, hentikan proses tersebut atau jalankan ulang setelah port kosong.

## Troubleshooting

Jika muncul error `ModuleNotFoundError: No module named 'flask'`, pastikan:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Jika halaman tidak tampil, cek apakah server Flask sudah berjalan dan URL yang dibuka sudah benar.
