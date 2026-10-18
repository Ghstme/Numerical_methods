import sympy as sp

print("Задание 1 а)")
x = 12 / 11
x_star = 1.091
delta = abs(x - x_star)
print(f"x = 12/11 = {x:.10f}")
print(f"x_star = {x_star}")
print(f"Абсолютная погрешность = {delta:.10f}")
print('-' * 20)

print("Задание 1 б)")
x_star = 0.000000935
delta_x_star = 10 ** (-10)
delta_otn = delta_x_star / abs(x_star)
print(f"x_star = {x_star:.10f}")
print(f"delta_x_star = {delta_x_star:.10f}")
print(f"Относительная погрешность = {delta_otn:.10f}")
print('-' * 20)
print("Задание 2")

x_star = 0.00230003500
delta_x_star = 10 ** (-13)

print(f"x* ={x_star}")
print(f"delta_x_star = {delta_x_star:.13f}")
print("0.002300035")
print("0.0000000000001")
print("Значащие цифры: 2 3 0 0 0 3 5 0 0 - 9 штук")
print("Верные цифры:  2 3 0 0 0 3 5 0 0   - 9 штук")

print('-' * 20)
print("Задание 3а")
print("V = (pi^2)/4 * D * d^2")

pi, D, d = sp.symbols("pi D d", positive=True)
V = (pi ** 2) / 4 * D * d ** 2

dV_dpi = sp.diff(V, pi)
dV_dD = sp.diff(V, D)
dV_dd = sp.diff(V, d)

print("dV/dpi =", dV_dpi)
print("dV/dD  =", dV_dD)
print("dV/dd  =", dV_dd)

pi_star, D_star, d_star = 3.149, 54.9, 8.235
d_pi, d_D, d_d = 10 ** (-3), 10 ** (-1), 10 ** (-2)
podst = {pi: pi_star, D: D_star, d: d_star}

V_star = float(V.subs(podst))

delta_V = (abs(float(dV_dpi.subs(podst))) * d_pi +
           abs(float(dV_dD.subs(podst))) * d_D +
           abs(float(dV_dd.subs(podst))) * d_d)

delta_V_otnos = delta_V / abs(V_star)

print(f"\npi* = {pi_star},  Δ(pi*) = {d_pi}")
print(f"D*  = {D_star},   Δ(D*)  = {d_D}")
print(f"d*  = {d_star},   Δ(d*)  = {d_d}")
print(f"Приближённое значение = {V_star}")
print(f"Абсолютная погрешность = {delta_V}")
print(f"Относительная погрешность = {delta_V_otnos}")

print('-' * 20)
print("Задание 3б")
print("y = x1^2 + x2^2 * ln(x2^2 + x3^2)")

x1, x2, x3 = sp.symbols("x1 x2 x3", positive=True)
y = x1 ** 2 + x2 ** 2 * sp.log(x2 ** 2 + x3 ** 2)

dy_dx1 = sp.diff(y, x1)
dy_dx2 = sp.diff(y, x2)
dy_dx3 = sp.diff(y, x3)

print("dy/dx1 =", dy_dx1)
print("dy/dx2 =", dy_dx2)
print("dy/dx3 =", dy_dx3)

x1_star, x2_star, x3_star = 25.3687, 0.000635, 0.0000054
d_x1, d_x2, d_x3 = 10 ** (-4), 10 ** (-6), 10 ** (-7)

podst = {x1: x1_star, x2: x2_star, x3: x3_star}

y_star = float(y.subs(podst))

delta_y = (abs(float(dy_dx1.subs(podst))) * d_x1
           + abs(float(dy_dx2.subs(podst))) * d_x2
           + abs(float(dy_dx3.subs(podst))) * d_x3)

delta_y_otnos = delta_y / abs(y_star)

print(f"\nx1* = {x1_star} +- {d_x1:.4f}")
print(f"x2* = {x2_star} +- {d_x2:.6f}")
print(f"x3* = {x3_star:.7f} +- {d_x3:.7f}")
print(f"Приближённое значение = {y_star}")
print(f"Абсолютная погрешность = {delta_y}")
print(f"Относительная погрешность = {delta_y_otnos:.15f}")
