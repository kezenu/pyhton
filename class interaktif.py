class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def tampilkan(self):
        print(f"Mobil       : {self.merk}")
        print(f"Warna       : {self.warna}")
        print(f"tahun       : {self.tahun}")
        print("=============================")
        mobil1.nyalakan_mesin()
        mobil1.status_mesin()
        print("=============================")
        mobil2.nyalakan_mesin()
        mobil2.status_mesin()

    def nyalakan_mesin(self):
        self.mesin_nyala = True
        print(f"Mesin {self.merk} dinyalakan")

    def matikan_mesin(self):
        self.mesin_mati = False
        print(f"Mesin {self.merk} Dimatikan")

    def status_mesin(self):
        status = "Nyala" if self.mesin_nyala else "Mati"
        print(f"Status Mesin {status}")


mobil1 = Mobil("Totoya", "Merah", 2020)
mobil2 = Mobil("Honda", "Hitam", 2019)

mobil1.tampilkan()
mobil2.tampilkan()
