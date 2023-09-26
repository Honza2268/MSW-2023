import numpy as np
from scipy import integrate
import sympy as sp

"""
Zadání:
V oblasti přírodních a sociálních věd je velice důležitým pojmem integrál,
který představuje funkci součtů malých změn (počet nakažených covidem za čas, hustota monomerů daného typu při posouvání se v řetízku polymeru, aj.).
Integraci lze provádět pro velmi jednoduché funkce prostou Riemannovým součtem,
avšak pro složitější funkce je nutné využít pokročilé metody.
Vaším úkolem je vybrat si 3 různorodé funkce (polynom, harmonická funkce, logaritmus/exponenciála)
a vypočíst určitý integrál na dané funkci od nějakého počátku do nějakého konečného bodu.
Porovnejte, jak si každá z metod poradila s vámi vybranou funkcí na základě přesnosti vůči analytickému řešení.
"""

sx = sp.symbols('x')

# Polynom
polynomial = sx**2
f_polynomial = lambda x: x**2

# Harmonická funkce
harmonic = sp.sin(sx)
f_harmonic = lambda x: np.sin(x)

# Exponenciální funkce
log_exponential = sp.exp(sx)
f_log_exponential = lambda x: np.exp(x)

# Interval integrace
point_from = 0
point_to = np.pi

# Analytické řešení
analytical_solution_poly = sp.integrate(polynomial, (sx, point_from, point_to))
analytical_solution_harmonic = sp.integrate(harmonic, (sx, point_from, point_to))
analytical_solution_log_exponential = sp.integrate(log_exponential, (sx, point_from, point_to))

# Riemannův čtverec
riemann_solution_poly, _ = integrate.quad(f_polynomial, point_from, point_to)
riemann_solution_harmonic, _ = integrate.quad(f_harmonic, point_from, point_to)
riemann_solution_log_exponential, _ = integrate.quad(f_log_exponential, point_from, point_to)

# Simpsonova metoda
simpson_solution_poly = integrate.simps([polynomial.subs(sx, i) for i in np.linspace(point_from, point_to, 1000)], np.linspace(point_from, point_to, 1000))
simpson_solution_harmonic = integrate.simps([harmonic.subs(sx, i) for i in np.linspace(point_from, point_to, 1000)], np.linspace(point_from, point_to, 1000))
simpson_solution_log_exponential = integrate.simps([log_exponential.subs(sx, i) for i in np.linspace(point_from, point_to, 1000)], np.linspace(point_from, point_to, 1000))

# Rombergova metoda
def romberg_integration(func, a, b, n):
    integral, _ = integrate.quad(func, a, b)
    return integrate.romberg(func, a, b, tol=10**(-n))

romberg_solution_poly = romberg_integration(lambda x: x**2, point_from, point_to, 5)
romberg_solution_harmonic = romberg_integration(lambda x: np.sin(x), point_from, point_to, 5)
romberg_solution_log_exponential = romberg_integration(lambda x: np.exp(x), point_from, point_to, 5)

print("Polynom:")
print("Analytické řešení:", analytical_solution_poly)
print("Riemannův čtverec:", riemann_solution_poly)
print("Simpsonova metoda:", simpson_solution_poly)
print("Rombergova metoda:", romberg_solution_poly)

print("Harmonická funkce:")
print("Analytické řešení:", analytical_solution_harmonic)
print("Riemannův čtverec:", riemann_solution_harmonic)
print("Simpsonova metoda:", simpson_solution_harmonic)
print("Rombergova metoda:", romberg_solution_harmonic)

print("Exponenciální funkce:")
print("Analytické řešení:", analytical_solution_log_exponential)
print("Riemannův čtverec:", riemann_solution_log_exponential)
print("Simpsonova metoda:", simpson_solution_log_exponential)
print("Rombergova metoda:", romberg_solution_log_exponential)

"""
Polynom:
Analytické řešení: 10.3354255600999
Riemannův čtverec: 10.335425560099939
Simpsonova metoda: 10.3354255600999
Rombergova metoda: 10.33542556009994

Harmonická funkce:
Analytické řešení: 2.00000000000000
Riemannův čtverec: 2.0
Simpsonova metoda: 2.00000000000516
Rombergova metoda: 1.9999999945872906

Exponenciální funkce:
Analytické řešení: 22.1406926327793
Riemannův čtverec: 22.140692632779267
Simpsonova metoda: 22.1406926328853
Rombergova metoda: 22.1406926327867
"""