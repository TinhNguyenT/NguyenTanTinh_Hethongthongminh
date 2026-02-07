import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def rule_ac_power(T, occ):
    if T > 30 and occ >= 1:
        return 80
    elif T >= 27:
        return 50
    return 20

T_in = 29.0
T_out = 32.0
occ = 2

T_list = []
AC_list = []

for step in range(60):
    if step < 20:
        occ = 2
    elif step < 40:
        occ = 1
    else:
        occ = 0

    ac = rule_ac_power(T_in, occ)

    dT = -0.1 if ac == 80 else -0.05 if ac == 50 else -0.02
    if T_out > 30:
        dT += 0.1
    if occ == 2:
        dT += 0.08
    elif occ == 1:
        dT += 0.04

    T_in = min(max(T_in + dT, 20), 35)

    T_list.append(T_in)
    AC_list.append(ac)


plt.figure()
plt.plot(T_list)
plt.title("Mô phỏng T_in")
plt.tight_layout()

img1_path = os.path.join(BASE_DIR, "loop_temperature.png")
plt.savefig(img1_path)
plt.show()


plt.figure()
plt.step(range(len(AC_list)), AC_list, where="post")
plt.title("Công suất AC")
plt.tight_layout()

img2_path = os.path.join(BASE_DIR, "loop_ac_power.png")
plt.savefig(img2_path)
plt.show()

print(" Đã lưu ảnh mô phỏng vào:", BASE_DIR)
