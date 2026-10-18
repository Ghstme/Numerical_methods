import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import factorial


def f(x):
    return x * np.exp(x) + np.sin(x)


a = 0.0
b = 2.0
n_poly = 12
n_nodes = n_poly + 1

print(f"Отрезок [{a}, {b}], n = {n_poly}, узлов = {n_nodes}")

x_nodes = np.linspace(a, b, n_nodes)
y_nodes = f(x_nodes)
print("Узлы интерполяции и значения функции:")
print(f"{'i':>3} | {'x_i':>8} | {'f(x_i)':>16}")

for i in range(len(x_nodes)):
    xi = x_nodes[i]
    yi = y_nodes[i]
    print(f"{i:>3} | {xi:>8.4f} | {yi:>16.10f}")

x_dense = np.linspace(a, b, 500)
y_exact = f(x_dense)


def lagrange(x_nodes, y_nodes, x_array):
    results = []
    for x_eval in x_array:
        total = 0.0
        for i in range(len(x_nodes)):
            Li = 1.0
            for j in range(len(x_nodes)):
                if i != j:
                    Li *= (x_eval - x_nodes[j]) / (x_nodes[i] - x_nodes[j])
            total += y_nodes[i] * Li
        results.append(total)
    return np.array(results)


def composition(x, x_nodes):
    p = 1.0
    for xi in x_nodes:
        p *= (x - xi)
    return p


y_lag = lagrange(x_nodes, y_nodes, x_dense)

prac_err = np.abs(y_exact - y_lag)
eps_prac = np.max(prac_err)

x_sym = sp.Symbol('x', real=True)
f_sym = x_sym * sp.exp(x_sym) + sp.sin(x_sym)
f_deriv_sym = sp.diff(f_sym, x_sym, n_poly + 1)
print(f"Производная функции: {f_deriv_sym}")
f_deriv_func = sp.lambdify(x_sym, f_deriv_sym, 'numpy')
M_n1 = np.max(np.abs(f_deriv_func(x_dense)))
factor = M_n1 / factorial(n_poly + 1)

theo_err = np.zeros(len(x_dense))
for i in range(len(x_dense)):
    theo_err[i] = factor * abs(composition(x_dense[i], x_nodes))

eps_theo = np.max(theo_err)

print(f"f^({n_poly + 1})(x) = {f_deriv_sym}")
print(f"M_n+1= {M_n1:.6f}")
print(f"({n_poly + 1})! = {factorial(n_poly + 1):,}")
print(f"Практическая погрешность  ε_практ = {eps_prac:.6e}")
print(f"Теоретическая погрешность ε_теор  = {eps_theo:.6e}")
print()

fig1, ax1 = plt.subplots(figsize=(11, 6))

ax1.plot(x_dense, y_exact, 'b-', lw=2.5, label='f(x) = x·eˣ + sin x')
ax1.plot(x_dense, y_lag, 'r--', lw=2.5, label='Полином Лагранжа')
ax1.plot(x_nodes, y_nodes, 'ko', ms=7, zorder=5, label=f'Узлы интерполяции')

ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('Функция f(x) и полином Лагранжа', fontsize=13)
ax1.legend(fontsize=11)
ax1.grid(alpha=0.3)
plt.tight_layout()
plt.show()

fig2, ax2 = plt.subplots(figsize=(11, 6))

ax2.semilogy(x_dense, prac_err, 'g-', lw=2)
ax2.axhline(eps_prac, color='r', ls='--', lw=1.5, label=f'ε_практ = {eps_prac:.3e}')

for xi in x_nodes:
    ax2.axvline(xi, color='gray', ls=':', alpha=0.3)

ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('|f(x) − L12(x)|', fontsize=12)
ax2.set_title('Практическая погрешность', fontsize=13)
ax2.legend(fontsize=11)
ax2.grid(alpha=0.3, which='both')
plt.tight_layout()
plt.show()

fig3, ax3 = plt.subplots(figsize=(11, 6))

ax3.semilogy(x_dense, theo_err, 'm-', lw=2)
ax3.axhline(eps_theo, color='r', ls='--', lw=1.5, label=f'ε_теор = {eps_theo:.3e}')

for xi in x_nodes:
    ax3.axvline(xi, color='gray', ls=':', alpha=0.3)

ax3.set_xlabel('x', fontsize=12)
ax3.set_ylabel('|R12(x)|', fontsize=12)
ax3.set_title('Теоретическая', fontsize=13)
ax3.legend(fontsize=11)
ax3.grid(alpha=0.3, which='both')
plt.tight_layout()
plt.show()

fig4, ax4 = plt.subplots(figsize=(11, 6))

ax4.semilogy(x_dense, prac_err, 'g-', lw=2,
             label='практическая |f − L12|')
ax4.semilogy(x_dense, theo_err, 'm--', lw=2,
             label='теоретическая |R12|')

for xi in x_nodes:
    ax4.axvline(xi, color='gray', ls=':', alpha=0.3)

ax4.set_xlabel('x', fontsize=12)
ax4.set_ylabel('Погрешности', fontsize=12)
ax4.set_title('Сравнение теоретической и практической погрешностей',
              fontsize=13)
ax4.legend(fontsize=11)
ax4.grid(alpha=0.3, which='both')
plt.tight_layout()
plt.show()
