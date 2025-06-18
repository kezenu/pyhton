import pandas as pd

data = {
    'Nama': ['Budi', 'Ani', 'Santi', 'Joko', 'Rina'],
    'Umur': [23, 21, 22, 25, 24],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Jakarta', 'Bandung'],
    'Nilai': [85, 90, 78, 88, 95]
}

df = pd.DataFrame(data)

print(df.head())
