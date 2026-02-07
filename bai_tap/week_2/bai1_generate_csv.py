import csv
from datetime import datetime, timedelta
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "hvac_simulated_week2.csv")

start_time = datetime(2025, 1, 1, 7, 0)
end_time   = datetime(2025, 1, 1, 21, 0)
delta      = timedelta(minutes=5)

def get_occ_level(t):
    h = t.hour
    if 7 <= h < 11:
        return 2
    elif 11 <= h < 13:
        return 1
    elif 13 <= h < 17:
        return 2
    return 0

def get_T_out(t):
    h = t.hour
    if 11 <= h < 14:
        return 33.0
    elif 9 <= h < 11 or 14 <= h < 16:
        return 31.0
    elif 7 <= h < 9 or 16 <= h < 18:
        return 29.0
    return 27.0

def rule_ac_power(T, occ):
    if T > 30 and occ >= 1:
        return 80, 3
    elif 27 <= T <= 30:
        return 50, 2
    return 20, 1

rows = []
T_in = 28.0
humidity = 75.0

current_time = start_time
while current_time <= end_time:
    T_out = get_T_out(current_time)
    occ = get_occ_level(current_time)
    ac, fan = rule_ac_power(T_in, occ)

    dT = -0.15 if ac >= 70 else -0.08 if ac >= 40 else -0.02
    if T_out >= 31:
        dT += 0.10
    if occ == 2:
        dT += 0.08
    elif occ == 1:
        dT += 0.04

    T_in = min(max(T_in + dT, 20), 35)

    rows.append({
        "timestamp": current_time.strftime("%Y-%m-%d %H:%M"),
        "T_in": round(T_in, 2),
        "T_out": T_out,
        "humidity": humidity,
        "occ_level": occ,
        "ac_power": ac,
        "fan_level": fan
    })

    current_time += delta

with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(" Đã tạo file:", CSV_PATH)
