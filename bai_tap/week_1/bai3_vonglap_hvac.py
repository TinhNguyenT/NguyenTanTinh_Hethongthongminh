

count_off = 0
count_medium = 0
count_high = 0

for step in range(1, 6):
    print(f"\n--- Buoc {step} ---")
    T_in = float(input("Nhap nhiet do trong phong (do C): "))
    n_people = int(input("Nhap so nguoi trong phong: "))

    if T_in < 24 and n_people < 20:
        decision = "AC OFF"
        count_off += 1
    elif T_in < 28:
        decision = "AC MEDIUM"
        count_medium += 1
    else:
        decision = "AC HIGH"
        count_high += 1

    print(f"Buoc {step}: T_in={T_in}, n_people={n_people}, Quyet dinh={decision}")

print("\n=== TONG KET ===")
print(f"So lan AC OFF: {count_off}")
print(f"So lan AC MEDIUM: {count_medium}")
print(f"So lan AC HIGH: {count_high}")
