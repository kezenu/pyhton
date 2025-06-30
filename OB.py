import pandas as pd
import matplotlib.pyplot as plt

# Load data (pastikan ada kolom: datetime, open, high, low, close)
df = pd.read_csv("data/EURUSD_H4.csv", parse_dates=["time"])

# Hitung body candle
df['body'] = abs(df['close'] - df['open'])
df['bullish'] = df['close'] > df['open']

# Threshold (tweak sesuai karakter data, ini contoh konservatif)
body_threshold = df['body'].rolling(50).mean() * 1.5

rbr_zones = []

# Loop candle untuk cari pola RBR
for i in range(1, len(df)-1):
    c1 = df.iloc[i-1]
    c2 = df.iloc[i]
    c3 = df.iloc[i+1]

    if (
        c1['bullish'] and c1['body'] > body_threshold[i-1] and
        not c2['bullish'] and c2['body'] < body_threshold[i] and
        c3['bullish'] and c3['body'] > body_threshold[i+1]
    ):
        # Simpan zona base (low-high dari candle ke-2)
        rbr_zones.append((df.iloc[i]['time'], df.iloc[i]['low'], df.iloc[i]['high']))

# Plot hasilnya
plt.figure(figsize=(15, 6))
plt.plot(df['time'], df['close'], label='Close')

# Tandai zona base RBR
for time, zl, zh in rbr_zones:
    plt.axhspan(zl, zh, color='skyblue', alpha=0.3)
    plt.axvline(time, color='blue', linestyle='--', alpha=0.4)

plt.title("Deteksi Zona RBR (Rally–Base–Rally)")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()
