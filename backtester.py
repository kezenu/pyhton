import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

# === Load Data ===
df = pd.read_csv('EURUSD_M5.csv')
df['time'] = pd.to_datetime(df['time'])
df.set_index('time', inplace=True)

# === Init State ===
start = 100  # jumlah candle awal
fig, ax = plt.subplots(figsize=(10, 4))


def plot_candles(data):
    ax.clear()
    ax.set_title('Replay Chart (Tekan ENTER di Chart)')
    ax.set_xlabel('Waktu')
    ax.set_ylabel('Harga')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M\n%d-%b'))
    ax.xaxis.set_major_locator(mticker.MaxNLocator(10))

    for i in range(len(data)):
        o = data['open'].iloc[i]
        h = data['high'].iloc[i]
        l = data['low'].iloc[i]
        c = data['close'].iloc[i]
        t = data.index[i]

        color = 'green' if c >= o else 'red'
        ax.plot([t, t], [l, h], color=color)
        ax.plot([t, t], [o, c], color=color, linewidth=6)

    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.canvas.draw()


# === Event Handler ===
def on_key(event):
    global start
    if event.key == 'enter':
        if start < len(df):
            window = df.iloc[start-100:start]
            plot_candles(window)
            start += 1
        else:
            print("Sudah selesai semua candle.")
    elif event.key == 'q':
        print("Keluar.")
        plt.close()


# === Bind Keyboard Event ===
fig.canvas.mpl_connect('key_press_event', on_key)

# === Tampilkan Awal ===
plot_candles(df.iloc[start-100:start])
plt.show()
