# %% [markdown]
# 1. import data from datasheet csv with pandas

# %%
import pandas as pd

df = pd.read_csv('XAUUSD_H4.csv')
print(df.head())

# %% [markdown]
# 2. predict next candle close, if next price bigger than current price add 1 label, if lower than add label 0

# %%
# prediksi arah harga selanjutnya
# label: 1 jika harga berikutnya naik, 0 jika turun
df['next_close'] = df['close'].shift(-1)
df['target'] = (df['next_close'] > df['close']).astype(int)

# baris terakhir karena targetnya NaN
df = df.dropna()
print(df[['close', 'next_close', 'target']].head())

# %% [markdown]
# 3. technical code use methode moving average 20

# %%
df['ma20'] = df['close'].rolling(window=20).mean()
df['return_1'] = df['close'].pct_change()
df = df.dropna()

print(df[['close', 'ma20', 'return_1', 'target']].head())

# %% [markdown]
# 4. split fitur

# %%
X = df[['close', 'ma20', 'return_1']]
y = df['target']
print(X)

# %% [markdown]
# 4. Train_Test Split

# %%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# %%
from sklearn.ensemble import RandomForestClassifier as rfc

model = rfc(n_estimators=100, random_state=42, max_depth=10, min_samples_leaf=10, min_samples_split=2, class_weight='balanced')
model.fit(X_train,y_train)

# %%
from sklearn.metrics import accuracy_score, classification_report
y_pred = model.predict(X_test)
print("Akuarasi : ", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(df['target'].value_counts())

# %%
# Prediksi arah dari data terakhir
latest_data = df.iloc[-1]
fitur_terakhir = [[latest_data['close'], latest_data['ma20'], latest_data['return_1']]]
prediksi = model.predict(fitur_terakhir)

print("Prediksi arah selanjutnya:", "Naik" if prediksi[0] == 1 else "Turun")



