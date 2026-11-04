#!/usr/bin/env python3
"""Pemeriksa pola slop untuk prosa berbahasa Indonesia (salinan untuk skill natural-indonesia).

Skrip hanya membaca dan melaporkan. Temuan adalah petunjuk untuk dinilai,
bukan keputusan otomatis.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

WORD_RE = re.compile(r"[A-Za-zÀ-ÿ0-9]+(?:[-'’][A-Za-zÀ-ÿ0-9]+)*")
SENTENCE_RE = re.compile(r"[^.!?\n]+[.!?]?")
MONTHS_DAYS = {
    "senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu",
    "januari", "februari", "maret", "april", "mei", "juni", "juli",
    "agustus", "september", "oktober", "november", "desember",
}
PENALTY = {"P1": 6, "P2": 2, "P3": 1}


def baca_preferensi() -> dict:
    """Baca pengaturan pemeriksa dari berkas gaya penulisan personal.

    Berkas: $GAYA_PENULISAN atau ~/.claude/gaya-penulisan.md, bagian "## Pengaturan pemeriksa"
    berisi baris `kunci: tolak|boleh`. Tanpa berkas, semua pemeriksaan tanda baca aktif.
    """
    import os
    pref = {"tanda_pisah": "tolak", "titik_koma_antarklausa": "tolak", "titik_dua_prosa": "tolak"}
    path = Path(os.environ.get("GAYA_PENULISAN", Path.home() / ".claude" / "gaya-penulisan.md"))
    try:
        teks = path.read_text(encoding="utf-8")
    except OSError:
        return pref
    m = re.search(r"(?ms)^## Pengaturan pemeriksa\s*$(.*?)(?=^## |\Z)", teks)
    for k, v in re.findall(r"(?m)^\s*([a-z_]+)\s*:\s*(tolak|boleh)\b", m.group(1) if m else ""):
        if k in pref:
            pref[k] = v
    return pref


@dataclass(frozen=True)
class Temuan:
    tingkat: str
    kode: str
    baris: int
    cuplikan: str
    pesan: str


def pola(teks: str) -> re.Pattern[str]:
    return re.compile(teks, re.IGNORECASE)


FRASA = [
    ("P1", "PEMBUKA_GENERIK", pola(r"\b(di era (modern|digital|globalisasi) ini|seiring (dengan )?perkembangan zaman|tidak dapat di[mp]ungkiri|sebagaimana (kita )?ketahui)\b"),
     "Pembuka generik. Mulai dengan fakta, objek, atau masalah yang spesifik."),
    ("P1", "PENGANTAR_META", pola(r"\b(perlu (dicatat|diketahui|diingat|ditekankan) bahwa|penting untuk (dicatat|diingat|dipahami)|dapat (dilihat|dipahami) bahwa)\b"),
     "Pengantar meta tanpa isi. Nyatakan isinya langsung."),
    ("P1", "INFLASI_KEPENTINGAN", pola(r"\b(memainkan peran (yang )?(penting|krusial|kunci|sentral)|berperan (sangat )?(penting|krusial|kunci)|sangat (penting|krusial)|krusial|memberikan kontribusi (yang )?signifikan|menjadi (landasan|tonggak|fondasi) (yang )?penting|menunjukkan betapa pentingnya|merupakan salah satu \w+ (yang )?paling|tidak (bisa|dapat) dipandang sebelah mata)\b"),
     "Inflasi kepentingan. Sebut mekanisme, tindakan, atau ukurannya."),
    ("P1", "PENUTUP_FORMULAIK", pola(r"\b(dengan demikian,? dapat disimpulkan bahwa|pada akhirnya|satu hal yang (pasti|jelas)|intinya adalah)\b"),
     "Penutup formulaik. Akhiri pada fakta atau posisi."),
    ("P1", "KONTRAS_NEGASI", pola(r"\b(bukan (hanya|sekadar|semata(-mata)?)\b[^.!?]{0,120}\b(melainkan|tetapi|namun)|tidak hanya\b[^.!?]{0,120}\btetapi juga)\b"),
     "Kontras negasi. Nyatakan hal yang dimaksud secara langsung, kecuali kontras itu bagian dari argumen."),
    ("P1", "DIKSI_PUITIS", pola(r"\b(nan|laksana|tatkala|manakala|niscaya|permadani|cakrawala|lentera|mercusuar|menyelami|menapaki|merajut|menenun|menyibak|urat nadi|ujung tombak|angin segar)\b"),
     "Diksi puitis. Ganti dengan kata literal."),
    ("P1", "BUZZWORD", pola(r"\b(komprehensif|holistik|inovatif|sinergi|ekosistem|lanskap|transformasi digital|secara fundamental|pada intinya|pada dasarnya|multilingual generalis)\b"),
     "Kata abstrak yang sering menjadi hiasan. Sebut komponen atau mekanismenya."),
    ("P1", "ARTEFAK_ASISTEN", pola(r"\b(semoga membantu|jangan ragu untuk|tentu saja!|baik, berikut (adalah|ini)|apakah (anda|kamu) ingin saya|sebagai ai)\b"),
     "Frasa percakapan asisten. Hapus."),
    ("P2", "KLAUSA_TEMPELAN", pola(r",\s*(yang\s+)?(menunjukkan|menyoroti|menggarisbawahi|mencerminkan|menegaskan|menandakan|memastikan)\b"),
     "Klausa tempelan di akhir kalimat. Jadikan kalimat sendiri jika berisi informasi, hapus jika hanya penilaian."),
    ("P2", "SEHINGGA_MEMASTIKAN", pola(r"\bsehingga (dapat )?(memastikan|menjamin|mengoptimalkan)\b"),
     "Akibat yang diklaim tanpa bukti. Sebut tindakan pemeriksaannya."),
    ("P2", "VERBA_BANTALAN", pola(r"\b(menyoroti|menggarisbawahi|memfasilitasi|mengedepankan|mewujudkan|merealisasikan|berkontribusi (pada|terhadap))\b"),
     "Verba bantalan. Pakai verba yang menyatakan tindakan nyata."),
    ("P2", "PEMBANTAH", pola(r"\b(hal ini tidak berarti|bukan berarti bahwa|perlu ditegaskan bahwa|perlu dibedakan bahwa|meskipun demikian, (hal ini|penelitian ini) tidak)\b"),
     "Kemungkinan kalimat pembantah. Periksa apakah klaim yang dibantah pernah ditulis."),
    ("P2", "JUSTIFIKASI_NEGATIF", pola(r"\bpenelitian ini (tidak|bukan) (menggunakan|membahas|dimaksudkan|bertujuan|merupakan)\b"),
     "Justifikasi yang mungkin tidak ditanyakan. Hapus jika pembaca tidak akan salah paham."),
    ("P2", "ATRIBUSI_SAMAR", pola(r"\b(para ahli (menyatakan|berpendapat)|banyak (kalangan|pihak) berpendapat|menurut beberapa sumber|(berbagai )?(penelitian|studi) menunjukkan)\b"),
     "Atribusi samar. Sebut sumbernya."),
    ("P2", "PASANGAN_FORMULAIK", pola(r"\b(tantangan dan peluang|kelebihan dan kekurangan|di satu sisi)\b"),
     "Pasangan formulaik. Sebut masalah atau manfaat yang spesifik."),
    ("P2", "KALKE_RELATIF", pola(r"\b(yang mana|di mana(?= (setiap|masing-masing|data|model|nilai|peserta|pengguna|label|teks)))\b"),
     "Kalke relatif bahasa Inggris. Gunakan 'yang' atau susun ulang."),
    ("P2", "KALKE_FRASA", pola(r"\b(melakukan (analisis|pengukuran|evaluasi|perhitungan) terhadap|memiliki kemampuan untuk|mampu untuk|dalam rangka untuk|sebagai hasilnya|secara respektif|berfungsi sebagai|berperan sebagai)\b"),
     "Konstruksi terjemahan. Pakai verba langsung."),
    ("P3", "PENGUAT_TANPA_UKURAN", pola(r"\b(secara (signifikan|efektif|drastis)|semakin|sangat)\b"),
     "Penguat tanpa ukuran. Beri angka atau hapus. 'Signifikan' statistik tetap boleh jika ada ujinya."),
    ("P3", "PENGHUBUNG_KOSONG", pola(r"\b(menariknya|tak kalah penting(nya)?|lebih lanjut|dalam hal ini|berkaitan dengan hal (ini|tersebut))\b"),
     "Penghubung yang sering tidak membawa hubungan logis."),
]

PEMBUKA_BERULANG = re.compile(r"^(hal ini|ini|dalam|selain itu|dengan|penelitian ini|oleh karena itu)\b", re.IGNORECASE)
KETERANGAN_DEPAN = re.compile(
    r"^(pada|selama|setelah|sesudah|sebelum|saat|ketika|di|dalam|untuk|sampai|sejak|hingga|menjelang)\b[^,.!?]{0,60},",
    re.IGNORECASE,
)
KALIMAT_NILAI = re.compile(
    r"\b(di[a-z]+kan)\s+(\d+|satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh)\s*[.]",
    re.IGNORECASE,
)
HEDGE = re.compile(r"\b(mungkin|dapat|cenderung|berpotensi|relatif|umumnya|biasanya|kemungkinan)\b", re.IGNORECASE)


def nomor_baris(teks: str, posisi: int) -> int:
    return teks.count("\n", 0, posisi) + 1


def cuplik(teks: str, awal: int, akhir: int, radius: int = 50) -> str:
    potong = re.sub(r"\s+", " ", teks[max(0, awal - radius):min(len(teks), akhir + radius)]).strip()
    return potong if len(potong) <= 150 else potong[:147] + "..."


def buat(teks: str, awal: int, akhir: int, tingkat: str, kode: str, pesan: str) -> Temuan:
    return Temuan(tingkat, kode, nomor_baris(teks, awal), cuplik(teks, awal, akhir), pesan)


def token_sekitar(teks: str, i: int, arah: int) -> str:
    if arah < 0:
        m = re.search(r"([\wÀ-ÿ.,]+)\s*$", teks[:i])
    else:
        m = re.match(r"\s*([\wÀ-ÿ.,]+)", teks[i + 1:])
    return m.group(1).strip(".,") if m else ""


def cek_dash(teks: str):
    for m in re.finditer(r"[—–]|(?<![-\w])--(?![-\w])", teks):
        kiri, kanan = token_sekitar(teks, m.start(), -1), token_sekitar(teks, m.end() - 1, 1)
        angka = re.fullmatch(r"\d+(?:[.,]\d+)*", kiri or "") and re.fullmatch(r"\d+(?:[.,]\d+)*", kanan or "")
        kalender = kiri.casefold() in MONTHS_DAYS and kanan.casefold() in MONTHS_DAYS
        if angka or kalender:
            continue
        yield buat(teks, m.start(), m.end(), "P1", "TANDA_PISAH",
                   "Tanda pisah sebagai penyisip atau penghubung. Ganti dengan koma, kurung, titik, atau susun ulang.")


def cek_titik_koma(teks: str):
    for m in re.finditer(r";", teks):
        buka = teks.rfind("(", 0, m.start())
        tutup = teks.rfind(")", 0, m.start())
        # Titik koma di dalam kurung biasanya memisahkan sumber sitasi, yang dibolehkan.
        if buka > tutup:
            continue
        awal_baris = teks.rfind("\n", 0, m.start()) + 1
        baris = teks[awal_baris:m.start()].lstrip()
        # Perincian bernomor atau berhuruf juga boleh memakai titik koma.
        if re.match(r"(\(?\d+[.)]|\(?[a-z][.)]|[-*•])\s", baris):
            continue
        yield buat(teks, m.start(), m.end(), "P1", "TITIK_KOMA_KLAUSA",
                   "Titik koma antarklausa. Ganti dengan koma dan konjungsi, atau titik.")


def cek_frasa(teks: str):
    for tingkat, kode, rx, pesan in FRASA:
        for m in rx.finditer(teks):
            yield buat(teks, m.start(), m.end(), tingkat, kode, pesan)


def kalimat_per_paragraf(teks: str):
    posisi = 0
    for paragraf in re.split(r"\n\s*\n", teks):
        mulai = teks.find(paragraf, posisi)
        posisi = mulai + len(paragraf)
        daftar = []
        for m in SENTENCE_RE.finditer(paragraf):
            isi = m.group(0).strip()
            if WORD_RE.search(isi):
                daftar.append((mulai + m.start(), isi))
        yield mulai, daftar


def cek_irama(teks: str):
    for mulai_par, kalimat in kalimat_per_paragraf(teks):
        panjang = [len(WORD_RE.findall(k)) for _, k in kalimat]
        for i in range(len(panjang) - 2):
            jendela = panjang[i:i + 3]
            if all(17 <= n <= 23 for n in jendela) or (min(jendela) >= 12 and max(jendela) - min(jendela) <= 2):
                yield buat(teks, kalimat[i][0], kalimat[i + 2][0], "P2", "IRAMA_SERAGAM",
                           f"Tiga kalimat berurutan berpanjang serupa ({', '.join(map(str, jendela))} kata). Ubah struktur karena alasan isi.")
                break
        if len(kalimat) >= 3:
            berulang = [k for _, k in kalimat if PEMBUKA_BERULANG.match(k)]
            if len(berulang) * 2 > len(kalimat):
                yield buat(teks, mulai_par, mulai_par + 40, "P2", "PEMBUKA_SERAGAM",
                           f"{len(berulang)} dari {len(kalimat)} kalimat dibuka dengan penanda yang sama jenisnya.")
        if len(kalimat) >= 3:
            depan = [k for _, k in kalimat if KETERANGAN_DEPAN.match(k)]
            if len(depan) * 2 > len(kalimat):
                yield buat(teks, mulai_par, mulai_par + 40, "P2", "KETERANGAN_DEPAN",
                           f"{len(depan)} dari {len(kalimat)} kalimat dibuka dengan keterangan waktu atau tempat lalu koma. Pindahkan sebagian ke akhir kalimat.")
        for posisi, k in kalimat:
            m = KALIMAT_NILAI.search(k)
            if m:
                yield buat(teks, posisi + m.start(), posisi + m.end(), "P3", "KALIMAT_NILAI",
                           "Ketetapan ditulis seperti catatan. Tulis utuh, misalnya 'X yang ditetapkan adalah 3 proses'.")
            if len(HEDGE.findall(k)) >= 3:
                yield buat(teks, posisi, posisi + len(k), "P2", "HEDGING_BERTUMPUK",
                           "Tiga atau lebih penanda keraguan dalam satu kalimat. Pilih satu.")


def cek_titik_dua(teks: str, jumlah_kata: int):
    # Pengguna menolak titik dua yang mengantar daftar atau penjelasan di tengah prosa.
    for m in re.finditer(r"(?<=[A-Za-zÀ-ÿ*)])\s*:\s+(?=[a-zà-ÿ*])", teks):
        awal_baris = teks.rfind("\n", 0, m.start()) + 1
        baris = teks[awal_baris:m.start()]
        if re.match(r"\s*(#|\||[-*] \*\*|Tabel|Gambar|>)", baris):
            continue
        yield buat(teks, m.start(), m.end(), "P2", "TITIK_DUA_PROSA",
                   "Titik dua mengantar perincian di tengah kalimat. Gabungkan perincian ke dalam kalimat.")


PENGHUBUNG_AWAL = re.compile(
    r"^(kemudian|lalu|namun|selain itu|sementara itu|akibatnya|jadi|oleh karena itu|setelah itu),\s*",
    re.IGNORECASE,
)


def cek_keterangan_dokumen(teks: str):
    # Keterangan di depan yang tersebar di banyak paragraf juga membuat irama seragam.
    prosa = "\n".join(b for b in teks.splitlines() if not b.lstrip().startswith(("|", "#")))
    kalimat = [k for _, daftar in kalimat_per_paragraf(prosa) for _, k in daftar]
    depan = [k for k in kalimat if KETERANGAN_DEPAN.match(PENGHUBUNG_AWAL.sub("", k))]
    if len(depan) >= 6 and len(depan) * 100 >= 12 * len(kalimat):
        yield Temuan("P3", "KETERANGAN_DEPAN_DOKUMEN", 1, depan[0][:150],
                     f"{len(depan)} dari {len(kalimat)} kalimat prosa dibuka dengan keterangan waktu atau tempat. "
                     "Pindahkan sebagian ke akhir kalimat, kecuali keterangan yang menjadi peralihan atau pembanding.")


def audit(teks: str) -> tuple[list[Temuan], int, int]:
    jumlah_kata = len(WORD_RE.findall(teks))
    temuan: list[Temuan] = []
    pref = baca_preferensi()
    fungsi_aktif = [cek_frasa, cek_irama, cek_keterangan_dokumen]
    if pref["tanda_pisah"] == "tolak":
        fungsi_aktif.append(cek_dash)
    if pref["titik_koma_antarklausa"] == "tolak":
        fungsi_aktif.append(cek_titik_koma)
    for fungsi in fungsi_aktif:
        temuan.extend(fungsi(teks))
    if pref["titik_dua_prosa"] == "tolak":
        temuan.extend(cek_titik_dua(teks, jumlah_kata))
    unik = {(t.kode, t.baris, t.cuplikan): t for t in temuan}
    urut = sorted(unik.values(), key=lambda t: ({"P1": 0, "P2": 1, "P3": 2}[t.tingkat], t.baris, t.kode))
    # Penalti dinormalisasi per 250 kata agar teks panjang tidak otomatis bernilai rendah.
    beban = sum(PENALTY[t.tingkat] for t in urut) * 250 / max(jumlah_kata, 250)
    return urut, jumlah_kata, max(0, round(100 - beban))


def main() -> int:
    parser = argparse.ArgumentParser(description="Periksa pola slop pada prosa akademik Indonesia.")
    sumber = parser.add_mutually_exclusive_group(required=True)
    sumber.add_argument("path", nargs="?", type=Path)
    sumber.add_argument("--stdin", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    try:
        teks = sys.stdin.read() if args.stdin else args.path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"cek_slop.py: {exc}", file=sys.stderr)
        return 2

    temuan, jumlah_kata, skor = audit(teks)
    if args.json:
        print(json.dumps({"jumlah_kata": jumlah_kata, "skor": skor,
                          "temuan": [asdict(t) for t in temuan]}, ensure_ascii=False, indent=2))
    else:
        hitung = {k: sum(t.tingkat == k for t in temuan) for k in PENALTY}
        print(f"Kata: {jumlah_kata} | Skor: {skor}/100 | P1={hitung['P1']} P2={hitung['P2']} P3={hitung['P3']}")
        for t in temuan:
            print(f"\n[{t.tingkat}] {t.kode} baris {t.baris}\n  {t.pesan}\n  > {t.cuplikan}")
    return 1 if skor < 85 else 0


if __name__ == "__main__":
    raise SystemExit(main())
