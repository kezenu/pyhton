class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def tampilkan(self):
        print(f"Mobil       : {self.merk}")
        print(f"Warna       : {self.warna}")
        print(f"tahun       : {self.tahun}")


mobil1 = Mobil("Totoya", "Merah", 2020)
mobil2 = Mobil("Honda", "Hitam", 2019)

mobil1.tampilkan()
