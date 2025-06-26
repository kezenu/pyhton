import MetaTrader5 as mt5
import pandas as pd

# Peta input user ke atribut MetaTrader5
TIMEFRAME_MAP = {
    "M1": "TIMEFRAME_M1",
    "M5": "TIMEFRAME_M5",
    "M15": "TIMEFRAME_M15",
    "M30": "TIMEFRAME_M30",
    "H1": "TIMEFRAME_H1",
    "H4": "TIMEFRAME_H4",
    "D1": "TIMEFRAME_D1",
    "W1": "TIMEFRAME_W1",
    "MN1": "TIMEFRAME_MN1",
}


def scrapper(s, tf_key, candle):
    if tf_key not in TIMEFRAME_MAP:
        print(f"Timeframe '{tf_key}' tidak valid.")
        return

    tf_str = TIMEFRAME_MAP[tf_key]

    if not mt5.initialize():
        print("Gagal menghubungkan ke MetaTrader5")
        return

    TF = getattr(mt5, tf_str)
    bar = candle

    rates = mt5.copy_rates_from_pos(s, TF, 0, bar)
    mt5.shutdown()

    if rates is None or len(rates) == 0:
        print("Data tidak ditemukan.")
        return

    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit='s')
    df["open"] = round(df["open"], 5)
    df["high"] = round(df["high"], 5)
    df["low"] = round(df["low"], 5)
    df["close"] = round(df["close"], 5)
    df = df[['time', 'open', 'high', 'low', 'close', 'tick_volume']]

    df.to_csv(f"{s}_{tf_key}.csv", index=False)
    print(f"✅ Data {s} ({tf_key}) berhasil disimpan ke CSV")


# -----------------------
# Input user
# -----------------------
s = input("Masukkan simbol (contoh: EURUSD): ").upper()
tf_key = input("Masukkan Timeframe (M1, M5, H1, D1, dll): ").upper()
candle = int(input("Masukkan jumlah candlestick: "))

scrapper(s, tf_key, candle)
