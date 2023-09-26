from tools import *

import numpy as np
import matplotlib.pyplot as plt

"""
Důležitou částí studia na přírodovědecké fakultě je podobor matematiky zvaný lineární algebra.
Poznatky tohoto oboru jsou základem pro oblasti jako zpracování obrazu, strojové učení nebo návrh mechanických soustav s definovanou stabilitou.
Základní úlohou v lineární algebře je nalezení neznámých v soustavě lineárních rovnic.
Na hodinách jste byli obeznámeni s přímou a iterační metodou pro řešení soustav lineárních rovnic.
Vaším úkolem je vytvořit graf, kde na ose x bude velikost čtvercové matice a na ose y průměrný čas potřebný k nalezení uspokojivého řešení.
Cílem je nalézt takovou velikost matice, od které je výhodnější využít iterační metodu.
"""

@benchmark_it
def jacobi(A, b, niteraci, x0):
    x = x0
    D = np.diag(A)
    L = np.tril(A, k = -1)
    U = np.triu(A, k = 1)
    for i in range(niteraci):
        x = (b - np.matmul((L + U),x))/D
        #print("iterace:",i, "x=",x)
    return x

@benchmark_it
def solve_linear_system_direct(A, b):
    return np.linalg.solve(A, b)


mtx_sizes = range(10, 5001, 100)
average_times_iter = []
average_times_direct = []

for size in mtx_sizes:
    times_iter = []
    times_direct = []

    rand_mtx = np.random.rand(size, size)
    rand_vect = np.random.rand(size)

    for i in range(10):
        elapsed_time_iter, _ = jacobi(rand_mtx, rand_vect, 20, np.ones(len(rand_mtx)))
        times_iter.append(elapsed_time_iter)
        elapsed_time_direct, _ = solve_linear_system_direct(rand_mtx, rand_vect)
        times_direct.append(elapsed_time_direct)

    average_time_iter = np.mean(times_iter)
    average_times_iter.append(average_time_iter)
    average_time_direct = np.mean(times_direct)
    average_times_direct.append(average_time_direct)

plt.plot(mtx_sizes, average_times_iter, marker='o', label="Iterační metoda (jacobi)")
plt.plot(mtx_sizes, average_times_direct, marker='x', label="Přímé řešení")
plt.xlabel('Velikost matice')
plt.ylabel('Průměrný čas (s)')
plt.title('Průměrný čas pro řešení lineární soustavy')
plt.legend()
plt.grid(True)
plt.show()