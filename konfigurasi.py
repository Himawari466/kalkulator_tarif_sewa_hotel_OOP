#!/usr/bin/env python3
# Kalkulator Tarif Sewa Hotel OOP
# 2020 - Himawari466
# https://mit-license.org/

hotel = [
  "Selene Hotel",            # nama hotel
  "Jl. Kaguya no. 466",      # alamat hotel
  "0888 1234 1234 12"        # no telp hotel
]

tipekamar = [                # fill spasi untuk mempertahankan indent
  ["Single Room", 100000],
  ["Twin Room  ", 155000],
  ["Double Room", 170000],
  ["Family Room", 190000]
]

kelaskamar = [               # fill spasi untuk mempertahankan indent
  ["Regular (STD)", 90000],
  ["Deluxe (DLX) ", 150000],
  ["Suite (STE)  ", 220000],
  ["Presidental  ", 375000]
]

nonmember = [
  ["Potongan", 10000],       # potongan per hari
  ["Diskon 1", 5],           # diskon 4 - 7 hari, satuan persen
  ["Diskon 2", 10]           # diskon diatas 7 hari, satuan persen
]

member = [
  ["Potongan", 12000],       # potongan per hari
  ["Diskon 1", 20],          # diskon 4 - 7 hari, satuan persen
  ["Diskon 2", 30]           # diskon diatas 7 hari, satuan persen
]

errormsg = [
  "Input tidak valid, [enter]",
  "Nama pelanggan belum diisi, [enter]\n[m] Menu\n>> ",
  "Tipe kamar belum diisi, [enter]",
  "Kelas kamar belum diisi, [enter]",
  "Lama inap belum diisi, [enter]",
  "Pembayaran kurang, [enter]",
  "Input bukan bilangan bulat, [enter]"
 ]

if __name__ == "__main__":
  exit("File adalah konfigurasi")
