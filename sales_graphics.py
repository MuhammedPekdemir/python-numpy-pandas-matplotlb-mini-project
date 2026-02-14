import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Gunler = np.arange(1, 31)
AylikSatis = np.random.randint(1200, 3600, 30)
Kategoriler = np.random.choice(['Elektronik', 'Gıda', 'Giyim'], 30)

df = pd.DataFrame({ 'Gun': Gunler,'SatisFiyat': AylikSatis,'Kategori': Kategoriler})
print(df)

KategoriSatis = df.groupby('Kategori')['SatisFiyat'].sum()

def Performans(SatisFiyat):
    if SatisFiyat > 2500:
        return "Yüksek Kalite"
    elif 2000 < SatisFiyat <= 2500:
        return "Orta Kalite"
    else:
        return "Dusuk Kalite"

df["Urun Kategorisi"] = df["SatisFiyat"].apply(Performans)

df_performans = pd.DataFrame(df["Urun Kategorisi"])
print("")
print(df_performans)

df["7 Gunluk Ortalama"] = df["SatisFiyat"].rolling(window=7).mean()

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
plt.plot(Gunler, AylikSatis, linestyle="--", linewidth=1.5)
plt.xlabel("Günler")
plt.ylabel("Satış Fiyatı")
plt.title("Günlük Satışlar")
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.bar(KategoriSatis.index, KategoriSatis.values, width=0.4)
plt.xlabel("Kategori")
plt.ylabel("Toplam Satış Fiyatı")
plt.title("Kategorilere Göre Toplam Satış")
plt.ylim(0, 37500)

plt.tight_layout()
plt.show()
