import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SRC  = os.path.join(BASE_DIR, "hvac_simulated_week2.csv")
OUT1 = os.path.join(BASE_DIR, "hvac_with_outlier.csv")
OUT2 = os.path.join(BASE_DIR, "hvac_cleaned.csv")

df = pd.read_csv(SRC)

# Tạo outlier
df.loc[5, "T_in"] = 99
df.loc[10, "T_in"] = -5
df.loc[20, "humidity"] = 0
df.loc[25, "humidity"] = 150

df.to_csv(OUT1, index=False)

def bad_T(x): return x < 15 or x > 45
def bad_H(x): return x < 10 or x > 100

for i in df[df["T_in"].apply(bad_T)].index:
    df.loc[i, "T_in"] = df["T_in"].median()

for i in df[df["humidity"].apply(bad_H)].index:
    df.loc[i, "humidity"] = df["humidity"].median()

df.to_csv(OUT2, index=False)

print(" Đã tạo hvac_with_outlier.csv và hvac_cleaned.csv trong week_2")
