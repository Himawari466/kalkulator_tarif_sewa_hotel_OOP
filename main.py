#!/usr/bin/env python3
# Kalkulator Tarif Sewa Hotel OOP
# 2020 - Himawari466
# https://mit-license.org/

from konfigurasi import hotel, tipekamar, kelaskamar, errormsg
from tarif import TarifNonMember, TarifMember
from plumbum.cmd import clear
from termcolor import colored as wrn
from shutil import get_terminal_size
import locale, time

locale.setlocale(locale.LC_ALL, "id_ID.UTF-8")

def wiper():
  print(clear())

def separator(kolom):
  print("-" * kolom)

class Main:
  def App():
    kolomlayar = get_terminal_size().columns
    wiper()
    separator(kolomlayar)
    print(f"{wrn(hotel[0].center(kolomlayar), 'blue')}")
    print(f"{wrn(hotel[1].center(kolomlayar), 'blue')}")
    print(f"{wrn(hotel[2].center(kolomlayar), 'blue')}")
    separator(kolomlayar)
    print("\n" * 4)
    print(f"{wrn(time.strftime('%A, %d %b %Y').center(kolomlayar), 'blue')}")
    print(f"{wrn(time.strftime('%H:%M:%S').center(kolomlayar), 'blue')}")
    print("\n" * 4)
    print("Semangat bekerja!".center(kolomlayar))
    print("[enter] untuk memulai".center(kolomlayar))
    separator(kolomlayar)
    input("")
    __class__.Menu()

  def Menu():
    kolomlayar = get_terminal_size().columns
    if kolomlayar < 35:
      exit("Lebar layar terlalu kecil")
    while True:
      wiper()
      separator(kolomlayar)
      print(f"{wrn(hotel[0].center(kolomlayar), 'blue')}")
      print(f"{wrn(hotel[1].center(kolomlayar), 'blue')}")
      print(f"{wrn(hotel[2].center(kolomlayar), 'blue')}")
      separator(kolomlayar)
      print(f"{wrn('Menu Pembayaran:', 'blue')}")
      print("[1] Non Member")
      print("[2] Member")
      print("[e] Exit")
      pil = input(">> ").lower()
      if pil == "1":
        __class__.__tarif(1)
      elif pil == "2":
        __class__.__tarif(2)
      elif pil == "e":
        exit("Terima Kasih")
      else:
        input(f"{wrn(errormsg[0], 'red')}")

  def __tarif(_spil):
    kolomlayar = get_terminal_size().columns
    if _spil == 1:
      judul = "Pembayaran Non Member"
    elif _spil == 2:
      judul = "Pembayaran Member"
    else:
      exit()
    while True:
      wiper()
      separator(kolomlayar)
      print(f"{wrn(judul.center(kolomlayar), 'blue')}")
      separator(kolomlayar)
      print(f"{wrn(time.strftime('%H:%M:%S - %A, %d %b %Y'), 'blue')}")
      nama = input(f"{wrn('Nama pengunjung', 'blue')}\t{wrn(': ', 'blue')}")
      if nama == "":
        pil = input(f"{wrn(errormsg[1], 'red')}").lower()
        if pil == "m":
          __class__.Menu()
        else:
          continue
      index = 0
      for tipe in tipekamar:
        index += 1
        print(f"{index:>2}. {tipe[0]}\t\t{tipe[1]:>9,}")
      tipe = input(f"{wrn('Tipe Kamar', 'blue')}\t{wrn(': ', 'blue')}")
      if tipe == "":
        input(f"{wrn(errormsg[2], 'red')}")
        continue
      try:
        tipe = int(tipe)
      except ValueError:
        input(f"{wrn(errormsg[6], 'red')}")
        continue
      index = 0
      for kelas in kelaskamar:
        index += 1
        print(f"{index:>2}. {kelas[0]}\t{kelas[1]:>9,}")
      kelas = input(f"{wrn('Kelas Kamar', 'blue')}\t{wrn(': ', 'blue')}")
      if kelas == "":
        input(f"{wrn(errormsg[3], 'red')}")
        continue
      try:
        kelas = int(kelas)
      except ValueError:
        input(f"{wrn(errormsg[6], 'red')}")
        continue
      hari = input(f"{wrn('Lama inap (maks. 365 hari)', 'blue')}{wrn(': ', 'blue')}")
      if hari == "":
        input(f"{wrn(errormsg[4], 'red')}")
        continue
      try:
        hari = int(hari)
      except ValueError:
        input(f"{wrn(errormsg[6], 'red')}")
        continue
      if hari > 365:
        input(f"{wrn('Maksimal 365 hari, [enter]', 'red')}")
        continue
      pil = input("\nYakin input sudah benar?\nY / T >> ").lower()
      tanggal = time.strftime("[%H:%M:%S] %d/%m/%Y")
      if pil == "y":
        if _spil == 1:
          tarif = TarifNonMember(nama, tipe - 1, kelas - 1, hari)
        elif _spil == 2:
          tarif = TarifMember(nama, tipe - 1, kelas - 1, hari)
        else:
          exit()
        bayar = 0
        while True:
          wiper()
          separator(kolomlayar)
          print(f"{wrn(judul.center(kolomlayar), 'blue')}")
          separator(kolomlayar)
          __class__.total(tarif, bayar, tanggal)
          separator(10)
          bayar = input("Bayar: ")
          if bayar == "":
            input(f"{wrn('Jumlah belum diisi, [enter]', 'red')}")
            continue
          try:
            bayar = int(bayar)
          except ValueError:
            bayar = 0
            input(f"{wrn(errormsg[6], 'red')}")
            continue
          if bayar < tarif.grandtotal():
            input(f"{wrn(errormsg[5], 'red')}")
            continue
          elif bayar > tarif.grandtotal():
            pil = input("\nYakin input sudah benar?\nY / T >> ").lower()
            if pil == "y":
              kolomreceipt = 35
              while True:
                wiper()
                separator(kolomreceipt)
                print(f"{wrn('Receipt'.center(kolomreceipt), 'blue')}")
                separator(kolomreceipt)
                __class__.total(tarif, bayar, tanggal)
                separator(kolomreceipt)
                print(f"{wrn(hotel[0].center(kolomreceipt), 'blue')}")
                print(f"{wrn(hotel[1].center(kolomreceipt), 'blue')}")
                print(f"{wrn(hotel[2].center(kolomreceipt), 'blue')}")
                separator(kolomreceipt)
                pil = input("")
                if pil == "":
                  print("[enter] sembunyikan\n[k] kembali\n[m] menu")
                  pil = input(">> ").lower()
                  if pil == "":
                    continue
                  elif pil == "k":
                    del tarif
                    __class__.__tarif(_spil)
                  elif pil == "m":
                    del tarif
                    __class__.Menu()
                  else:
                    input(f"{wrn(errormsg[0], 'red')}")
                    continue
            else:
              continue
      else:
        continue

  def total(tarif, bayar, tanggal):
    if bayar == "":
      bayar = 0
    print(f"{wrn(tanggal, 'blue')}")
    print(f"{wrn('Nama', 'blue')}\t{wrn(': ', 'blue')}{tarif.nama()}")
    print(f"{wrn('Tipe', 'blue')}\t{wrn(': ', 'blue')}{tarif.tipe()[0]}")
    print(f"\t{wrn(': ', 'blue')}{tarif.tipe()[1]:,}")
    print(f"{wrn('Kelas', 'blue')}\t{wrn(': ', 'blue')}{tarif.kelas()[0]}")
    print(f"\t{wrn(': ', 'blue')}{tarif.kelas()[1]:,}")
    print(f"{wrn('Lama inap', 'blue')}\t{wrn(': ', 'blue')}{tarif.hari()} hari")
    print(f"{wrn('Tarif permalam', 'blue')}\t{wrn(': ', 'blue')}{tarif.tarifpermalam():,}")
    separator(10)
    print(f"{wrn('Tarif total', 'blue')}\t{wrn(': ', 'blue')}{tarif.tariftotal():>16,}")
    print(f"{wrn('Potongan', 'blue')}\t{wrn(': ', 'blue')}-{tarif.potongan(tarif.hari()):>15,}")
    print(f"{wrn('Sub total 1', 'blue')}\t{wrn(': ', 'blue')}{tarif.subtotal1():>16,}")
    print(f"{wrn('Diskon', 'blue')}\t\t{wrn(': ', 'blue')}-{tarif.diskon():>15,}")
    print(f"{wrn('Sub total 2', 'blue')}\t{wrn(': ', 'blue')}{tarif.subtotal2():>16,}")
    print(f"{wrn('PPN', 'blue')}\t\t{wrn(': ', 'blue')}+{tarif.ppn():>15,}")
    print(f"{wrn('Grand Total', 'green')}\t{wrn(': ', 'green')}{tarif.grandtotal():>16,}")
    print(f"{wrn('Bayar', 'blue')}\t\t{wrn(': ', 'blue')}{bayar:>16,}")
    kembali = bayar - tarif.grandtotal()
    print(f"{wrn('Kembalian', 'green')}\t{wrn(': ', 'green')}{kembali:>16,}")

if __name__ == "__main__":
  Main.App()
