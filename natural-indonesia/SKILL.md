---
name: natural-indonesia
description: Dasar gaya tulisan bahasa Indonesia yang natural dan mengalir, dengan mode akademik untuk naskah. Antarkalimat disambung kata penghubung sesuai hubungannya, isi dinyatakan langsung tanpa kalimat negasi pembantah, istilah teknis dijabarkan untuk pembaca awam, letak keterangan bervariasi, dan tabel diantar kalimat yang membacanya. Ragam bawaannya agak formal (laporan, ringkasan, dokumen kerja, surel), lalu digeser menurut saluran, yaitu santai untuk grup WhatsApp, formal untuk surat dinas, dan mode akademik untuk tesis, skripsi, artikel jurnal, proposal hibah, abstrak, serta balasan reviewer. Pakai setiap kali menulis atau menyunting teks berbahasa Indonesia untuk dibaca orang lain, termasuk laporan, notulen, ringkasan untuk pimpinan, penjelasan teknis ke orang non-IT, dan paragraf naskah, juga ketika pengguna menyebut tulisan kaku, terputus-putus, AI banget, slop, atau tidak natural, walaupun nama skill ini tidak disebut.
---

# Natural Indonesia

Tulisan terasa natural ketika pembaca bisa mengikuti alurnya tanpa berhenti untuk menebak hubungan antarkalimat. Setiap kalimat membawa fakta, angka, atau keputusan, kemudian kalimat berikutnya jelas kedudukannya sebagai akibat, lanjutan, pertentangan, atau penjelasan dari kalimat sebelumnya. Tulisan mesin biasanya gagal di dua hal itu. Kalimatnya benar satu per satu, tetapi berdiri sendiri-sendiri, dan isinya sering berupa bantahan atau pembenaran yang tidak diminta.

Skill ini disusun dari koreksi nyata pada laporan teknis dan naskah akademik. Contoh sebelum dan sesudahnya ada di `references/contoh-perbaikan.md`, dan semua contoh ditulis ulang dari data publik. Baca berkas itu saat ragu bagaimana sebuah aturan diterapkan.

## Ragam

**Bawaan: agak formal.** Bahasa baku menurut EYD, tetapi tidak kaku. Kalimat aktif bila pelakunya penting, kalimat pasif bila prosedurnya yang penting. Kata ganti orang dipakai seperlunya. Ragam ini cocok untuk laporan ke mitra atau atasan, ringkasan hasil, dokumen kerja tim, dan surel resmi ringan.

Ragam bergeser dari bawaan bila pengguna memintanya, atau bila saluran dan pembacanya jelas berbeda:

- **Ke arah formal** untuk surat dinas dan nota resmi. Pakai penghubung baku, ragam impersonal, dan kalimat yang lebih padat.
- **Ke mode akademik** untuk naskah ilmiah. Lihat bagian "Mode akademik".
- **Ke arah santai** untuk pesan ke rekan kerja, catatan pribadi, atau unggahan internal. Pakai penghubung lisan, kalimat lebih pendek, dan sapaan langsung bila wajar.

Saluran sering menentukan ragam lebih kuat daripada pembacanya. Pesan grup WhatsApp untuk atasan tetap ditulis santai dan sopan, walaupun pembacanya senior, karena kalimat resmi seperti "izin menyampaikan" terasa janggal di grup percakapan.

| Saluran | Ragam |
|---|---|
| Tesis, skripsi, artikel jurnal, proposal hibah, balasan reviewer | Mode akademik |
| Surat dinas, nota resmi | Formal |
| Laporan ke mitra atau atasan, surel resmi, dokumen kerja | Agak formal (bawaan) |
| Pesan grup WhatsApp atau Telegram, obrolan tim, catatan pribadi | Santai dan sopan |

Tabel penghubung per ragam ada di bagian "Kata penghubung". Kalau pengguna mengoreksi tulisan pada ragam tertentu, catat koreksinya sebagai aturan atau contoh baru di ragam itu, sehingga skill ini makin tersetel.

## Mode akademik

Untuk tesis, skripsi, disertasi, artikel jurnal, makalah prosiding, proposal hibah, abstrak, dan balasan untuk pembimbing atau reviewer, baca `references/ragam-akademik.md` sebelum menulis. Berkas itu menyesuaikan aturan dasar di bawah untuk naskah (misalnya istilah teknis dipertahankan dan perumpamaan tidak dipakai), menambah aturan khusus naskah seperti larangan kalimat pembantah dan klaim yang melampaui bukti, serta memuat preferensi bawaan untuk sitasi dan pembuka latar belakang. Preferensi bawaan itu boleh diganti penulis lewat `~/.claude/gaya-penulisan.md`.

## Preferensi pribadi

Beberapa pilihan gaya bergantung pada selera penulis, misalnya letak keterangan waktu dan tempat atau pemakaian perumpamaan. Bila ada `~/.claude/gaya-penulisan.md`, baca bagian `## Natural Indonesia` di sana dan ikuti isinya, karena preferensi penulis lebih kuat daripada bawaan skill ini. Ketika pengguna mengoreksi pilihan yang sifatnya selera, tawarkan untuk mencatatnya di bagian itu, sehingga koreksi yang sama tidak perlu diulang.

## Aturan inti

**1. Tinggalkan kalimat yang berdiri sendiri-sendiri. Sambungkan dengan penghubung yang menunjukkan hubungannya.**
Sebelum menulis kalimat kedua dan seterusnya, tanyakan apa hubungannya dengan kalimat sebelumnya, lalu pilih penghubung untuk hubungan itu. Hubungan yang paling sering muncul adalah sebab-akibat, urutan waktu, pertentangan, tambahan, dan penjelasan. Penghubung dipilih karena hubungannya memang ada, sehingga tidak setiap kalimat perlu penghubung. Kalimat pertama paragraf, kalimat yang membuka topik baru, dan perincian yang sudah jelas urutannya boleh tanpa penghubung. Variasikan penghubungnya, sebab penghubung yang sama di awal tiga kalimat berturut-turut juga terbaca sebagai tulisan mesin.

> Terputus: Pengguna KRL Jabodetabek pada Juni 2024 berjumlah 26,7 juta orang. Pada Juli jumlahnya 29,2 juta orang. Rekor harian tercatat 1,15 juta pengguna.
> Tersambung: Pengguna KRL Jabodetabek pada Juni 2024 berjumlah 26,7 juta orang. Sebulan kemudian, jumlahnya naik 9% menjadi 29,2 juta orang, dan rekor harian 1,15 juta pengguna juga tercatat pada bulan itu.

Penghubung yang salah hubungan lebih buruk daripada tanpa penghubung, karena pembaca dibawa ke logika yang keliru. *Dengan begitu* dan *akibatnya* hanya dipakai bila kalimat kedua memang akibat dari kalimat pertama. Untuk penjumlahan atau rangkuman, pakai *jadi* atau *totalnya*. Pada ragam yang lebih formal, *sehingga* di dalam kalimat yang sama sering lebih tepat.

> Salah hubungan: KRL melayani 156,8 juta pengguna pada semester I 2024 dan 29,2 juta pengguna pada Juli. Dengan begitu, sampai akhir Juli KRL melayani sekitar 186,1 juta pengguna.
> Tepat: KRL melayani 156,8 juta pengguna pada semester I 2024 dan 29,2 juta pengguna pada Juli, jadi totalnya sampai akhir Juli sekitar 186,1 juta pengguna.
> Tepat, lebih formal: KRL melayani 156,8 juta pengguna pada semester I 2024 dan 29,2 juta pengguna pada Juli, sehingga jumlah pengguna sampai akhir Juli mencapai sekitar 186,1 juta orang.

**2. Tinggalkan kalimat negasi yang membantah sesuatu. Nyatakan apa yang ada atau yang terjadi.**
Kalimat seperti "Penurunan ini tidak terjadi secara kebetulan" atau "Data tidak hilang" membuat pembaca membayangkan hal yang tidak pernah dibahas. Tulis keadaan yang sebenarnya, misalnya angka apa yang berubah atau data apa yang dipakai. Negasi tetap dipakai bila memang informasinya, misalnya "Fitur ini belum tersedia di aplikasi versi lama".

> Negasi: Penurunan prevalensi stunting tahun ini tidak terjadi secara kebetulan.
> Langsung: Prevalensi stunting nasional turun dari 21,5% pada 2023 menjadi 19,8% pada 2024.

**3. Tinggalkan justifikasi yang tidak ditanyakan. Tulis alasan hanya ketika pembaca membutuhkannya untuk bertindak atau memahami keputusan.**
Klausa "karena ...", "supaya ...", atau "agar ..." yang tidak mengubah tindakan pembaca hanya memperpanjang kalimat. Sebaliknya, bila pengguna meminta alasan, atau bila keputusan akan dipertanyakan (misalnya memakai data Juli, bukan Agustus), alasannya ditulis lengkap.

> Berlebih: Angka yang dipakai adalah hasil SSGI 2024, karena angka itu yang terbaru dan berasal dari pemerintah.
> Cukup: Angka yang dipakai berasal dari Survei Status Gizi Indonesia (SSGI) 2024.

**4. Jabarkan istilah teknis untuk pembaca awam.**
Sebut sesuatu menurut fungsinya ("kode QR standar yang bisa dibaca semua aplikasi pembayaran", "penjual yang menerima pembayaran QRIS"), bukan singkatan, nama berkas, kode, atau istilah alat. Ukuran statistik ditulis sebagai maknanya, misalnya "sekitar 20 dari 100 balita mengalami stunting", dan perbandingan tahunan ditulis "dibandingkan bulan yang sama tahun lalu", bukan "YoY". Nama berkas, kode, dan perintah hanya dipakai bila pembacanya tim teknis yang memang akan membukanya.

**5. Definisikan satuan sekali, lalu pakai terus.**
Satuan atau istilah buatan sendiri didefinisikan saat pertama muncul, kemudian dipakai dengan bentuk yang sama sampai akhir. Satu konsep memakai satu istilah. Mengganti istilah demi variasi, misalnya berganti-ganti antara "pengguna", "penumpang", dan "volume" untuk hal yang sama, membuat pembaca mengira ada tiga hal yang berbeda.

**6. Tulis angka konkret dan tandai perkiraan.**
Angka hasil ditulis apa adanya. Perkiraan atau hasil hitungan sendiri ditandai dengan "sekitar" atau "±", dan asumsinya disebut sekali di tempat angka itu dihitung. Persentase disertai jumlah aslinya bila jumlah itu penting ("29,2 juta orang, naik 9%").

**7. Antar dan baca setiap tabel.**
Sebelum tabel, satu kalimat menyebut isi tabel atau keadaan saat angkanya diambil. Sesudah tabel, satu atau dua kalimat membaca angka yang penting bagi kesimpulan. Kolom yang namanya tidak lazim dijelaskan sebelum tabel. Tabel yang muncul tanpa kalimat pengantar terasa seperti tempelan.

**8. Kesimpulan menyatakan posisi.**
Kesimpulan berisi temuan dan keputusan yang bisa dipegang pembaca, lengkap dengan angkanya. Hindari kalimat rekap yang hanya mengulang isi paragraf sebelumnya.

**9. Variasikan letak keterangan waktu dan tempat.**
Pola "Pada X, ...", "Selama X, ...", "Setelah X, ..." wajar dipakai, tetapi bila hampir setiap kalimat dibuka dengan keterangan lalu koma, irama tulisan terasa seragam. Pindahkan sebagian keterangan ke akhir kalimat. Keterangan diletakkan di depan bila menjadi penanda peralihan atau pembanding ("Pada musim mudik, ..."), dan di belakang bila hanya melengkapi. Pembagian depan dan belakang adalah selera, jadi ikuti preferensi penulis bila sudah tercatat.

> Seragam: Pada Januari 2024, nilai transaksi QRIS mencapai Rp31,65 triliun. Pada triwulan III, nilainya Rp188,36 triliun. Pada November, penggunanya berjumlah 55,02 juta orang.
> Bervariasi: Nilai transaksi QRIS mencapai Rp31,65 triliun pada Januari 2024, lalu Rp188,36 triliun sepanjang triwulan III. Pada November, penggunanya sudah berjumlah 55,02 juta orang.

**10. Tulis ketetapan dan nilai dalam kalimat utuh.**
Kalimat pasif pendek yang diakhiri angka tanpa satuan terasa seperti catatan rapat, bukan prosa. Sebut pokoknya, lalu nilainya beserta satuan dengan bentuk "... yang ... adalah ...", atau pakai kalimat aktif.

> Seperti catatan: Target stunting 2025 ditetapkan 18,8.
> Utuh: Target prevalensi stunting yang ditetapkan untuk 2025 adalah 18,8%.

**11. Perumpamaan sesuai keinginan penulis.**
Perumpamaan sehari-hari (misalnya "QRIS seperti satu colokan listrik yang cocok untuk semua merek charger") bisa membantu pembaca awam memahami hal teknis. Namun, ada penulis yang memakainya dan ada yang tidak. Ikuti preferensi penulis bila sudah tercatat atau disebut. Bila belum ada keterangan, tulis tanpa perumpamaan dan jelaskan hal teknisnya secara langsung.

## Kata penghubung

Pilih menurut hubungan, lalu sesuaikan dengan ragam.

| Hubungan | Agak formal (bawaan) | Formal atau akademik | Santai |
|---|---|---|---|
| Sebab-akibat | akibatnya, oleh karena itu, sehingga, karena itu | oleh karena itu, dengan demikian, sehingga | jadi, makanya, karena itu |
| Urutan | kemudian, lalu, setelah itu, sesudah itu | kemudian, selanjutnya, setelah itu | terus, habis itu, lalu |
| Pertentangan | namun, tetapi, padahal, meski begitu | namun, akan tetapi, meskipun demikian | tapi, padahal, cuma |
| Tambahan | selain itu, juga, pun | selain itu, di samping itu | juga, terus, sekalian |
| Penjelasan | artinya, jadi, dengan begitu | artinya, dengan kata lain | maksudnya, jadi |
| Jumlah atau rangkuman | jadi, sehingga | sehingga, dengan demikian | jadi, totalnya |
| Perbandingan | sementara itu, sebaliknya | sementara itu, sebaliknya | sedangkan, kalau |
| Syarat | jika, bila, kalau | jika, apabila | kalau, asal |

Catatan pemakaian:

- *Sehingga* dan *sedangkan* menyambung dua klausa dalam satu kalimat, jadi tidak dipakai di awal kalimat baru.
- *Jadi* dan *padahal* di awal kalimat terasa lisan untuk ragam formal. Di ragam bawaan keduanya wajar bila hanya sesekali.
- Hindari *di sisi lain* sebagai peralihan kosong. Pakai *namun* atau *sebaliknya* bila memang ada kebalikan.

## Tanda baca

Bila ada `~/.claude/gaya-penulisan.md`, ikuti preferensi di sana. Bila tidak ada, pakai bawaan ini:

- Tanpa tanda pisah (—) dan en dash (–), kecuali rentang nyata. Ganti dengan koma berpasangan, tanda kurung, atau kalimat baru.
- Tanpa titik koma sebagai pengganti kata sambung antarklausa. Pakai koma dengan kata sambung, atau titik.
- Tanpa titik dua pengantar daftar di tengah prosa. Gabungkan perincian ke dalam kalimat, misalnya "label positif, netral, dan negatif".

## Cara kerja

1. Tentukan pembaca dan ragam. Kalau pembacanya campuran, tulis untuk yang paling awam.
2. Kumpulkan isinya lebih dulu, yaitu fakta, angka, keputusan, dan alasan yang memang dibutuhkan.
3. Tulis paragraf, lalu periksa sambungan setiap kalimat dengan kalimat sebelumnya (aturan 1).
4. Periksa daftar di bawah, kemudian jalankan pemeriksa otomatis.

Daftar periksa manual:

- Apakah ragam sudah sesuai dengan saluran (surat, laporan, naskah, atau grup percakapan)?
- Adakah dua kalimat berurutan yang hubungannya harus ditebak pembaca, atau penghubung yang hubungannya keliru?
- Apakah sebagian besar kalimat dibuka dengan keterangan waktu atau tempat lalu koma?
- Adakah ketetapan atau nilai yang ditulis seperti catatan ("ditetapkan 18,8")?
- Adakah kalimat negasi yang membantah hal yang tidak pernah dibahas?
- Adakah klausa alasan yang tidak mengubah tindakan atau pemahaman pembaca?
- Adakah singkatan, nama berkas, kode, atau istilah alat yang belum dijabarkan untuk pembaca awam?
- Apakah setiap tabel punya kalimat pengantar dan kalimat yang membaca angkanya?
- Apakah istilah dan satuan sama dari awal sampai akhir?
- Apakah angka di ringkasan, isi, dan kesimpulan saling cocok?

Pemeriksa otomatis:

```bash
python3 scripts/cek_slop.py draf.md
```

Skrip memberi skor 0 sampai 100 dan menandai pola seperti pembuka generik, irama kalimat yang seragam, keterangan waktu atau tempat yang terlalu sering di depan, ketetapan yang ditulis seperti catatan, dan tanda baca yang ditolak. Targetnya 85 atau lebih. Skrip ini dikalibrasi untuk prosa formal, jadi temuan irama di antara sel tabel boleh diabaikan. Perbaiki temuan dengan menulis ulang kalimat dari isinya, bukan dengan mengganti sinonim.
