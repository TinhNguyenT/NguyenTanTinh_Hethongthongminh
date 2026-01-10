

T_in = float(input("Nhap nhiet do trong phong (do C): "))
T_out = float(input("Nhap nhiet do ngoai troi (do C): "))
n_people = int(input("Nhap so nguoi trong phong: "))

cong_suat = 30  

if T_out > 35:
    cong_suat += 20

if n_people > 30:
    cong_suat += 20

if T_in > 28:
    cong_suat += 20


if cong_suat > 100:
    cong_suat = 100

print("\n--- THONG TIN HE THONG ---")
print(f"Nhiet do trong phong: {T_in} °C")
print(f"Nhiet do ngoai troi: {T_out} °C")
print(f"So nguoi: {n_people}")
print(f"Cong suat dieu hoa de nghi: {cong_suat}%")
