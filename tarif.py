#!/usr/bin/env python3
# Kalkulator Tarif Sewa Hotel OOP
# 2020 - Himawari466
# https://mit-license.org/

from konfigurasi import tipekamar, kelaskamar, nonmember, member

class Tarif(object):
  def __init__(self, nama, tipe, kelas, hari):
    self.__nama = nama
    self.__tipe = tipe
    self.__kelas = kelas
    self.__hari = hari
    self.__tariftipe = tipekamar
    self.__tarifkelas = kelaskamar

  def __del__(self):
    print("Data dibersihkan")

  def nama(self):
    return self.__nama

  def tipe(self):
    return self.__tariftipe[self.__tipe]

  def kelas(self):
    return self.__tarifkelas[self.__kelas]

  def hari(self):
    return self.__hari

  def tarifpermalam(self):
    return self.tipe()[1] + self.kelas()[1]

  def tariftotal(self):
    return (self.tipe()[1] + self.kelas()[1]) * self.hari()


class TarifNonMember(Tarif):
  def __init__(self, nama, tipe, kelas, hari):
    super().__init__(nama, tipe, kelas, hari)
    self.NonMember__tariftotal = None

  def potongan(self, hari):
    if hari == 1: # hari pertama tidak termasuk
      return 0
    return nonmember[0][1] + __class__.potongan(self, hari - 1)

  def diskon(self):
    if 4 <= super().hari() <= 7:
      diskon = nonmember[1][1] / 100
    else:
      if super().hari() > 7:
        diskon = nonmember[2][1] / 100
      else:
        diskon = 0
    return round(super().tariftotal() * diskon)

  def subtotal1(self):
    return round(super().tariftotal() - __class__.potongan(self, super().hari()))

  def subtotal2(self):
    return round(__class__.subtotal1(self) - __class__.diskon(self))

  def ppn(self):
    return round(__class__.subtotal2(self) * 10 / 100)

  def grandtotal(self):
    return __class__.subtotal2(self) + __class__.ppn(self)

class TarifMember(Tarif):
  def __init__(self, nama, tipe, kelas, hari):
    super().__init__(nama, tipe, kelas, hari)
    self._TarifMember__tariftotal = None

  def potongan(self, hari):
    if hari == 1: # hari pertama tidak termasuk
      return 0
    return member[0][1] + __class__.potongan(self, hari - 1)

  def diskon(self):
    if 4 <= super().hari() <= 7:
      diskon = member[1][1] / 100
    else:
      if super().hari() > 7:
        diskon = member[2][1] / 100
      else:
        diskon = 0
    return round(super().tariftotal() * diskon)

  def subtotal1(self):
    return round(super().tariftotal() - __class__.potongan(self, super().hari()))

  def subtotal2(self):
    return round(__class__.subtotal1(self) - __class__.diskon(self))

  def ppn(self):
    return round(__class__.subtotal2(self) * 10 / 100)

  def grandtotal(self):
    return __class__.subtotal2(self) + __class__.ppn(self)

if __name__ == "__main__":
    exit("File adalah module")
