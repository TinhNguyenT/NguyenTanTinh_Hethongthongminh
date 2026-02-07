import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "hvac_simulated_week2.csv")

df = pd.read_csv(CSV_PATH)
df["timestamp"] = pd.to_datetime(df["timestamp"])


plt.figure(figsize=(10,4))
plt.plot(df["timestamp"], df["T_in"], label="T_in")
plt.plot(df["timestamp"], df["T_out"], label="T_out")
plt.xlabel("Thời gian")
plt.ylabel("Nhiệt độ (°C)")
plt.title("Nhiệt độ trong / ngoài")
plt.legend()
plt.tight_layout()

img1_path = os.path.join(BASE_DIR, "plot_temperature.png")
plt.savefig(img1_path)
plt.show()


plt.figure(figsize=(10,3))
plt.step(df["timestamp"], df["occ_level"], where="post")
plt.xlabel("Thời gian")
plt.ylabel("Occupancy")
plt.title("Mức độ sử dụng phòng")
plt.tight_layout()

img2_path = os.path.join(BASE_DIR, "plot_occupancy.png")
plt.savefig(img2_path)
plt.show()

print(" Đã lưu ảnh vào:", BASE_DIR)
