## Cara Menjalankan Program

Ikuti langkah-langkah berikut untuk menjalankan program implementasi RSA ini.

### 1. Pastikan Python sudah terinstall

### 2. Download atau clone repository

### 3. Jalankan program

### 4. Masukkan input yang diminta

Program akan meminta beberapa input:

* bilangan prima p
* bilangan prima q
* nilai e
* pesan (angka)

Contoh input:

```
Masukkan bilangan prima p: 11
Masukkan bilangan prima q: 13
Masukkan nilai e: 7
Masukkan pesan (angka): 9
```

---

### 5. Hasil program

Program akan menampilkan:

* nilai n
* nilai phi(n)
* public key
* private key
* ciphertext
* hasil dekripsi

Contoh output:

```
Public Key (e,n) = (7,143)
Private Key (d,n) = (103,143)

Ciphertext = 48
Pesan setelah didekripsi = 9
```

Jika hasil dekripsi sama dengan pesan awal, maka algoritma RSA berhasil dijalankan dengan benar.

