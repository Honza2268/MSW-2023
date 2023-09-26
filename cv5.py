from tools import *
from math import *
import time
from scipy import optimize
import matplotlib.pyplot as plt

"""
Zadání:
Vyhledávání hodnot, při kterých dosáhne zkoumaný signál vybrané hodnoty je důležitou součástí analýzy časových řad. 
Pro tento účel existuje spousta zajímavých metod. Jeden typ metod se nazývá ohraničené (například metoda půlení intervalu),
při kterých je zaručeno nalezení kořenu, avšak metody typicky konvergují pomalu. Druhý typ metod se nazývá neohraničené,
které konvergují rychle, avšak svojí povahou nemusí nalézt řešení (metody využívající derivace). 
Vaším úkolem je vybrat tři různorodé funkce (například polynomiální, exponenciální/logaritmickou, harmonickou se směrnicí, aj.), 
které mají alespoň jeden kořen a nalézt ho jednou uzavřenou a jednou otevřenou metodou. 
Porovnejte časovou náročnost nalezení kořene a přesnost nalezení.
"""

funcs = [lambda x: x**3-x**2+x/4-5, lambda x: e**(x**2+x/9)-4, lambda x: sin(5*x)]

@benchmark_it
def bisect(min, max, max_iters, func):
  for _ in range(max_iters):  
    middle = (min + max) / 2  
    if (func(min) * func(middle)) < 0:
      max = middle
    else:
      min = middle
  return middle

@benchmark_it
def newton(func, x0):
   return optimize.newton(func, x0)

min=0     
max=10
steps=[50, 100, 150, 200, 250, 2000]
times = []

for s in steps:
    time = 0
    for i, func in enumerate(funcs):
        t, root = bisect(min, max, s, func)
        time += t*1000
        print(f"f{i} = {root} (biskce, krok {s})")
    print(f"Čas výpočtů: {time}ms")
    times.append(time)

time = 0
for i, func in enumerate(funcs):
    t, root = newton(func, min+max/2)
    time += t*1000
    print(f"f{i} = {root} (Newton)")
print(f"Čas výpočtů: {time}ms")

plt.plot(steps, times, marker='x', label="metoda bisekce")
plt.axhline(time, color="r", label="Newtonova metoda")
plt.ylabel("Čas")
plt.xlabel("Počet kroků bisekce")
plt.legend()
plt.grid(True)
plt.show()

"""
f0 = 2.058507184419609 (biskce, krok 50)
f1 = 1.1231644200421176 (biskce, krok 50)
f2 = 8.796459430051415 (biskce, krok 50)
Čas výpočtů: 0.0ms
f0 = 2.0585071844196063 (biskce, krok 100)
f1 = 1.1231644200421167 (biskce, krok 100)
f2 = 8.79645943005142 (biskce, krok 100)
Čas výpočtů: 0.0ms
f0 = 2.0585071844196063 (biskce, krok 150)
f1 = 1.1231644200421167 (biskce, krok 150)
f2 = 8.79645943005142 (biskce, krok 150)
Čas výpočtů: 0.0ms
f0 = 2.0585071844196063 (biskce, krok 200)
f1 = 1.1231644200421167 (biskce, krok 200)
f2 = 8.79645943005142 (biskce, krok 200)
Čas výpočtů: 0.0ms
f0 = 2.0585071844196063 (biskce, krok 250)
f1 = 1.1231644200421167 (biskce, krok 250)
f2 = 8.79645943005142 (biskce, krok 250)
Čas výpočtů: 1.0006427764892578ms
f0 = 2.0585071844196063 (biskce, krok 2000)
f1 = 1.1231644200421167 (biskce, krok 2000)
f2 = 8.79645943005142 (biskce, krok 2000)
Čas výpočtů: 3.998994827270508ms
f0 = 2.0585071844196063 (Newton)
f1 = 1.1231644200423638 (Newton)
f2 = 5.026548245743668 (Newton)
Čas výpočtů: 1.5077590942382812ms
"""





