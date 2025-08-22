# Vuln_Uploader

## Deskripsi

Vuln_Uploader adalah script sederhana untuk menguji endpoint upload pada sebuah server. Script ini mengirimkan file (misalnya .shtml) ke target yang ditentukan menggunakan request POST.
Script ini tidak menyediakan payload berbahaya, pengguna wajib membuat atau mengedit file sendiri sesuai kebutuhan.

---

## Dependensi

Sebelum menjalankan, pastikan sudah menyiapkan:

- Python 3.7+
- Modul requests (install dengan pip install requests)

---

## Cara Menyiapkan File .shtml

Anda perlu membuat file .shtml sendiri.
Berikut cara membuat dan mengedit file di berbagai terminal:

### Termux
```
nano example.shtml
```
### Linux
```
nano example.shtml
```
atau gunakan editor lain seperti vim atau gedit.

### Windows PowerShell
```
notepad.exe example.shtml
```
(Bisa juga menggunakan editor lain seperti VS Code atau Sublime Text, nama file juga boleh diganti sesuai keinginan.)

---

## Cara Penggunaan

### 1. Di Termux (Android)
```
pkg update && pkg upgrade -y
pkg install python -y
pip install requests
cd Vuln_Uploader
python vuln_uploader.py --target https://example.com/upload.php --file example.shtml
```
### 2. Di Linux
```
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
pip3 install requests
cd Vuln_Uploader
python3 vuln_uploader.py --target https://example.com/upload.php --file example.shtml
```
### 3. Di Windows PowerShell

*Pastikan Python sudah terinstall*
```
pip install requests
cd Vuln_Uploader
python vuln_uploader.py --target https://example.com/upload.php --file example.shtml
```
(Untuk nama file `.shtml` nya bisa disesuaikan dengan nama file yang ada di directory yang sama dengan `up_vuln.py`.)

---

## Catatan Penting

Gunakan script ini hanya untuk pembelajaran atau pengujian legal pada server milik Anda sendiri.

File .shtml wajib dibuat/diedit oleh pengguna sesuai tujuan masing-masing.

Segala bentuk penyalahgunaan berada di luar tanggung jawab pembuat script.



---

## Lisensi & Hak Cipta

*© 2025 Peju3ncer*
Dibuat oleh *Peju3ncer* untuk tujuan edukasi dan riset keamanan.
Dilarang memperjualbelikan atau menyalahgunakan tanpa izin.
