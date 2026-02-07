import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "hvac_cleaned.csv")

df = pd.read_csv(CSV_PATH)
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.set_index("timestamp", inplace=True)

print("T_in trung bình cả ngày:", round(df["T_in"].mean(), 2))
print("Buổi sáng:", round(df.between_time("07:00","11:00")["T_in"].mean(), 2))
print("Buổi trưa:", round(df.between_time("11:00","13:00")["T_in"].mean(), 2))
print("Buổi chiều:", round(df.between_time("13:00","17:00")["T_in"].mean(), 2))
