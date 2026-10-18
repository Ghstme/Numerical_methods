import numpy as np
import sympy as sp


def f(x):
    return x * np.exp(x) + np.sin(x)


x_sym = sp.Symbol('x', real=True)
f_sym = x_sym * sp.exp(x_sym) + sp.sin(x_sym)
f_deriv3_sym = sp.diff(f_sym, x_sym, 3)
f_deriv3_func = sp.lambdify(x_sym, f_deriv3_sym, 'numpy')


def gauss_n2(x0, h):
    j = int(round(x0 / h))
    xj = j * h
    t = (x0 - xj) / h

    x_left = (j - 1) * h
    x_right = (j + 1) * h

    y_left = f(x_left)
    y_mid = f(xj)
    y_right = f(x_right)

    d1_right = y_right - y_mid
    d1_left = y_mid - y_left
    d2 = d1_right - d1_left

    L2 = y_mid + d1_right * t + d2 * t * (t - 1) / 2.0

    xs = np.linspace(x_left, x_right, 200)
    M3 = np.max(np.abs(f_deriv3_func(xs)))
    R_est = M3 * h ** 3 * abs(t * (t * t - 1)) / 6.0

    return L2, R_est, t


a = 0.0
b = 2.0
x0 = 1.55
eps = 0.000001

print(f"Отрезок [{a}, {b}], x0 = {x0}, eps = {eps}")
h = 0.5
log = []

for i in range(60):
    L2, R_est, t = gauss_n2(x0, h)
    log.append((h, L2, R_est, t))
    if R_est <= eps:
        break
    h /= 2.0

exact = f(x0)
L2_final = log[-1][1]
h_final = log[-1][0]
n_iter = len(log)

print("Узлы (шаг, t, L2, |R2|):")
print(f"{'#':>3} | {'h':>10} | {'t':>7} | {'L2(x0)':>16} | {'|R2|':>14}")

for i in range(len(log)):
    hi, Li, Ri, ti = log[i]
    print(f"{i + 1:>3} | {hi:>10.6f} | {ti:>+7.3f} | {Li:>16.10f} | {Ri:>14.3e}")

print()
print(f"Точное f({x0})   = {exact:.10f}")
print(f"Гаусс L2({x0})   = {L2_final:.10f}")
print(f"Погрешность      = {abs(exact - L2_final):.3e}")
print(f"Финальный h      = {h_final}")
print(f"Итераций         = {n_iter}")
