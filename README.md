# Natural Indonesia

Skill untuk Claude dan agen AI lain yang membuat tulisan bahasa Indonesia terasa natural, mengalir, dan tidak terbaca seperti tulisan mesin. Tulisan mesin biasanya benar kalimat per kalimat, tetapi kalimatnya berdiri sendiri-sendiri dan isinya sering berupa bantahan atau pembenaran yang tidak diminta. Skill ini mengarahkan agen untuk menyambung setiap kalimat dengan kalimat sebelumnya, menyatakan isi secara langsung, dan memilih ragam bahasa yang cocok dengan saluran tulisannya.

Aturannya disusun dari koreksi nyata pada laporan teknis dan naskah akademik. Semua contoh di repositori ini memakai data publik yang ditulis ulang, dan sumbernya tercantum di bagian akhir.

## Isi repositori

| Berkas | Isi |
|---|---|
| `natural-indonesia/SKILL.md` | Ragam per saluran, 11 aturan inti, tabel kata penghubung, tanda baca, dan daftar periksa |
| `natural-indonesia/references/contoh-perbaikan.md` | Contoh sebelum dan sesudah untuk setiap aturan |
| `natural-indonesia/references/ragam-akademik.md` | Mode akademik untuk tesis, skripsi, artikel jurnal, dan proposal hibah |
| `natural-indonesia/scripts/cek_slop.py` | Pemeriksa otomatis yang memberi skor 0 sampai 100 |
| `gaya-penulisan.contoh.md` | Templat preferensi pribadi |

## Cara pasang

Untuk Claude Code, salin folder skill ke folder skills milikmu.

```bash
git clone https://github.com/gikirima/natural-indonesia.git
cp -r natural-indonesia/natural-indonesia ~/.claude/skills/
```

Untuk aplikasi Claude, unduh berkas `natural-indonesia.skill` dari halaman Releases, lalu unggah lewat menu Skills di pengaturan. Setelah terpasang, skill ini terpicu sendiri setiap kali agen menulis atau menyunting teks bahasa Indonesia untuk dibaca orang lain. Kamu juga bisa memanggilnya langsung, misalnya dengan "pakai natural-indonesia, mode akademik".

## Ragam dan mode

Ragam bawaannya agak formal, yaitu bahasa baku yang tidak kaku untuk laporan, ringkasan, dan dokumen kerja. Ragam itu kemudian digeser menurut saluran tulisan, karena saluran sering lebih menentukan daripada pembacanya. Pesan grup WhatsApp untuk atasan tetap ditulis santai dan sopan, sedangkan naskah tesis memakai mode akademik.

| Ragam | Dipakai untuk | Ciri utama |
|---|---|---|
| Santai | Grup WhatsApp atau Telegram, obrolan tim, catatan pribadi | Penghubung lisan (*jadi, tapi, terus*), kalimat pendek, sapaan langsung |
| Agak formal (bawaan) | Laporan ke mitra atau atasan, ringkasan hasil, surel, dokumen kerja | Baku tetapi luwes, istilah teknis dijabarkan untuk pembaca awam |
| Formal | Surat dinas, nota resmi | Penghubung baku, impersonal, kalimat lebih padat |
| Mode akademik | Tesis, skripsi, artikel jurnal, proposal hibah, balasan reviewer | Istilah teknis dipertahankan dan didefinisikan, tanpa kalimat pembantah, klaim sesuai bukti |

Agen memilih ragam dari salurannya, tetapi kamu bisa menentukannya sendiri dengan menyebut ragam atau mode yang diinginkan. Mode akademik membaca berkas `ragam-akademik.md`, yang menyesuaikan aturan dasar untuk naskah. Misalnya, istilah teknis tetap dipakai, perumpamaan ditinggalkan, dan kata penghubung lisan seperti *jadi* dan *padahal* tidak dipakai di awal kalimat.

## Contoh gaya

### Sebelum dan sesudah

Pasangan berikut menunjukkan pola yang paling sering diperbaiki skill ini.

**Kalimat yang berdiri sendiri-sendiri**

> **Sebelum:** Pengguna KRL Jabodetabek pada Juni 2024 berjumlah 26,7 juta orang. Pada Juli jumlahnya 29,2 juta orang. Rekor harian tercatat 1,15 juta pengguna.
>
> **Sesudah:** Pengguna KRL Jabodetabek pada Juni 2024 berjumlah 26,7 juta orang. Sebulan kemudian, jumlahnya naik 9% menjadi 29,2 juta orang, dan rekor harian 1,15 juta pengguna juga tercatat pada bulan itu.

**Kalimat negasi yang membantah**

> **Sebelum:** Kenaikan pengguna QRIS bukan sekadar tren sesaat dan tidak hanya terjadi di kota besar.
>
> **Sesudah:** Pengguna QRIS bertambah dari 46,37 juta orang pada Januari 2024 menjadi 55,02 juta orang pada November 2024.

**Penghubung yang salah hubungan**

> **Sebelum:** Prevalensi stunting tertinggi tercatat di Nusa Tenggara Timur, yaitu 37%. Akibatnya, prevalensi terendah tercatat di Bali, yaitu 8,7%.
>
> **Sesudah:** Prevalensi stunting tertinggi tercatat di Nusa Tenggara Timur, yaitu 37%. Sebaliknya, prevalensi terendah tercatat di Bali, yaitu 8,7%.

**Keterangan waktu yang selalu di depan**

> **Sebelum:** Pada Januari 2024, nilai transaksi QRIS mencapai Rp31,65 triliun. Pada triwulan III, nilainya Rp188,36 triliun. Pada November, penggunanya berjumlah 55,02 juta orang.
>
> **Sesudah:** Nilai transaksi QRIS mencapai Rp31,65 triliun pada Januari 2024, lalu Rp188,36 triliun sepanjang triwulan III. Pada November, penggunanya sudah berjumlah 55,02 juta orang.

**Ketetapan yang ditulis seperti catatan**

> **Sebelum:** Target stunting 2025 ditetapkan 18,8.
>
> **Sesudah:** Target prevalensi stunting yang ditetapkan untuk 2025 adalah 18,8%.

### Satu informasi dalam empat ragam

Informasinya sama, yaitu jumlah pengguna QRIS pada November 2024 dan target Bank Indonesia untuk tahun itu.

| Ragam | Kalimat |
|---|---|
| Santai | Pengguna QRIS sampai November 2024 udah 55,02 juta orang, jadi target BI tahun ini tembus. |
| Agak formal | Pengguna QRIS berjumlah 55,02 juta orang pada November 2024, jadi target Bank Indonesia sebanyak 55 juta pengguna untuk tahun itu sudah tercapai. |
| Formal | Jumlah pengguna QRIS pada November 2024 mencapai 55,02 juta orang, sehingga target Bank Indonesia sebanyak 55 juta pengguna pada tahun tersebut telah tercapai. |
| Akademik | Jumlah pengguna QRIS mencapai 55,02 juta orang pada November 2024, sehingga target 55 juta pengguna yang ditetapkan Bank Indonesia untuk tahun tersebut terlampaui. |

### Pesan grup WhatsApp

> Pagi, Bapak/Ibu. Sekadar info, pengguna KRL Jabodetabek bulan Juli 2024 tembus 29,2 juta orang, naik 9% dari Juni. Rekor hariannya juga pecah di 1,15 juta pengguna, pas tanggal 1 Juli.

### Paragraf laporan (ragam bawaan)

> Pengguna QRIS, yaitu kode QR standar yang bisa dibaca semua aplikasi pembayaran, berjumlah 55,02 juta orang pada November 2024. Angka itu sudah melampaui target Bank Indonesia sebanyak 55 juta pengguna untuk tahun yang sama. Sementara itu, penjual yang menerima pembayaran QRIS bertambah dari 30,88 juta pada Januari menjadi 35,1 juta pada November. Artinya, jumlah penjual juga ikut tumbuh, walaupun lebih lambat daripada jumlah pengguna.

### Paragraf naskah (mode akademik)

> Survei Status Gizi Indonesia (SSGI) 2024 mencatat prevalensi stunting nasional sebesar 19,8%, turun dari 21,5% pada 2023 (Kementerian Kesehatan, 2025). Angka tersebut berada di bawah target 2024 sebesar 20,1%. Meskipun demikian, kesenjangan antarprovinsi masih lebar, dengan prevalensi terendah 8,7% di Bali dan tertinggi 37% di Nusa Tenggara Timur. Selisih lebih dari empat kali lipat itu menunjukkan bahwa penurunan nasional belum merata di tingkat provinsi. Dengan target RPJMN sebesar 14,2% pada 2029, prevalensi nasional masih perlu turun 5,6 poin persentase dalam lima tahun.

## Preferensi pribadi

Beberapa pilihan gaya bergantung pada selera penulis, misalnya letak keterangan waktu, pemakaian perumpamaan, atau gaya sitasi. Pilihan itu dicatat di `~/.claude/gaya-penulisan.md`, dan skill akan mengikutinya bila berkas itu ada. Templatnya tersedia di `gaya-penulisan.contoh.md`, jadi cukup salin lalu ubah isinya.

```bash
cp gaya-penulisan.contoh.md ~/.claude/gaya-penulisan.md
```

Preferensi bawaan di templat berasal dari penyusun skill ini, antara lain sitasi APA dengan *et al.*, latar belakang naskah yang tidak dibuka dengan "Penelitian ini", dan perumpamaan yang hanya dipakai bila diminta. Setiap kali kamu mengoreksi pilihan yang sifatnya selera, agen akan menawarkan untuk mencatatnya di berkas itu.

## Pemeriksa otomatis

Pemeriksa ini memberi skor 0 sampai 100 dan menandai pola seperti pembuka generik, irama kalimat yang seragam, keterangan waktu yang terlalu sering di depan, ketetapan yang ditulis seperti catatan, serta tanda baca yang ditolak.

```bash
python3 natural-indonesia/scripts/cek_slop.py draf.md
```

Targetnya 85 atau lebih. Skrip hanya memakai pustaka standar Python 3, dan pengaturan tanda bacanya dibaca dari bagian `## Pengaturan pemeriksa` di berkas preferensi. Temuan di dalam sel tabel boleh diabaikan, karena sel tabel memang sering berbentuk serupa.

## Sumber data contoh

Angka dalam contoh diambil dari pemberitaan dan rilis berikut, lalu kalimatnya ditulis ulang untuk keperluan ilustrasi.

- Prevalensi stunting SSGI 2024: [Kementerian Kesehatan RI](https://www.kemkes.go.id/id/ssgi-2024-prevalensi-stunting-nasional-turun-menjadi-198)
- Pengguna dan penjual QRIS November 2024: [Bisnis.com](https://finansial.bisnis.com/read/20241218/90/1825348/warga-ri-makin-banyak-pakai-qris-transaksi-kartu-debit-terus-susut)
- Transaksi dan pengguna QRIS Januari 2024: [Infobank News](https://infobanknews.com/jos-transaksi-qris-tembus-rp3165-triliun-naik-14946-persen/)
- Transaksi QRIS triwulan III 2024: [Bisnis.com](https://ekonomi.bisnis.com/read/20241016/9/1808167/transaksi-qris-tembus-rp18836-trilliun-masyarakat-doyan-belanja-makan-dan-minum)
- Target pengguna QRIS 2024: [Investortrust](https://investortrust.id/macro/32362/bank-indonesia-bidik-55-juta-pengguna-qris-tahun-ini)
- Pengguna KRL Jabodetabek semester I 2024: [Okezone](https://economy.okezone.com/read/2024/07/16/320/3035075/penumpang-krl-jabodetabek-tembus-156-8-juta-orang-pada-semester-i-2024)
- Pengguna KRL Jabodetabek Juni dan Juli 2024 serta rekor harian: [Investortrust](https://investortrust.id/business/36343/catat-rekor-tertinggi-volume-harian-krl-capai-1-juta-penumpang)
- Pengguna KRL Jabodetabek selama libur Lebaran 2024: [Bisnis.com](https://ekonomi.bisnis.com/read/20240423/98/1759868/libur-lebaran-krl-jabodetabek-angkut-1789-juta-penumpang)

## Lisensi

Repositori ini memakai [lisensi MIT](LICENSE), sehingga skill ini boleh dipakai, diubah, dan dibagikan ulang dengan menyebut sumbernya.
