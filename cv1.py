from tools import *

import numpy as np
import random
from scipy.misc import derivative

"""
Zadání:
V tomto kurzu jste se učili s některými vybranými knihovnami.
Některé sloužily pro rychlé vektorové operace, jako numpy, některé mají naprogramovány symbolické manipulace,
které lze převést na numerické reprezentace (sympy), některé mají v sobě funkce pro numerickou integraci (scipy).
Některé slouží i pro rychlé základní operace s čísly (numba).

Vaším úkolem je změřit potřebný čas pro vyřešení nějakého problému (např.: provést skalární součin, vypočítat určitý integrál)
pomocí standardního pythonu a pomocí specializované knihovny.Toto měření proveďte alespoň pro 5 různých úloh (ne pouze jiná čísla, ale úplně jiné téma)
a minimálně porovnejte rychlost jednoho modulu se standardním pythonem.
Ideálně proveďte porovnání ještě s dalším modulem a snažte se, ať je kód ve standardním pythonu napsán efektivně.  
"""

@benchmark_it
def scalar_multi_python(v1, v2):
    out = 0
    for i in range(len(v1)): 
        out = out + v1[i] * v2[i]
    return out

@benchmark_it
def scalar_multi_numpy(v1, v2):
    return np.dot(v1, v2)

@benchmark_it
def integral_python(p1, p2, step):
    inv_step = int(1/step)
    x1 = [x * step for x in range(inv_step*p1, inv_step*p2+1)]    
    out = 0
    for i in x1:    
        out = out + (3*i+2)*step
    return out

@benchmark_it
def integral_numpy(p1, p2, step):
    numpy_array = np.arange(p1, p2, step)
    x = np.append(numpy_array, p2)
    y = 3*x+2
    return np.trapz(y,x)

@benchmark_it
def determinant_python(mtx):
    size = len(mtx)

    det = 1.0
    row_swaps = 0

    for col in range(size):
        pivot_row = col
        for i in range(col + 1, size):
            if abs(mtx[i][col]) > abs(mtx[pivot_row][col]):
                pivot_row = i

        if pivot_row != col:
            mtx[col], mtx[pivot_row] = mtx[pivot_row], mtx[col]
            row_swaps += 1

        pivot_value = mtx[col][col]
        if pivot_value == 0:
            return 0

        det *= pivot_value

        for i in range(col + 1, size):
            factor = mtx[i][col] / pivot_value
            for j in range(col, size):
                mtx[i][j] -= factor * mtx[col][j]
    
    if row_swaps % 2 == 1:
        det *= -1

    return det


@benchmark_it
def determinant_numpy(mtx):
    return np.linalg.det(mtx)

@benchmark_it
def matrix_multi_python(mtx1, mtx2):
    rowsA = len(mtx1)
    colsA = len(mtx1[0])
    rowsB = len(mtx2)
    colsB = len(mtx2[0])
   
    mtxOut = []
    while len(mtxOut) < rowsA:
        mtxOut.append([])
        while len(mtxOut[-1]) < colsB:
            mtxOut[-1].append(0.0)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += mtx1[i][ii] * mtx2[ii][j]
            mtxOut[i][j] = total
    return mtxOut

@benchmark_it
def matrix_multi_numpy(mtx1, mtx2):
    return np.dot(mtx1, mtx2)

@benchmark_it
def derivative_python(point, dx, func):
    f = lambda x: eval(func) 
    dy = f(point + dx) - f(point)
    return dy/dx

@benchmark_it
def derivative_special(point, dx, func):
    f = lambda x: eval(func)
    return derivative(f, point, dx)

vector1 = [random.randrange(-100, 100) for _ in range(1_000_000)]
vector2 = [random.randrange(-100, 100) for _ in range(1_000_000)]
time_smp, val_smp = scalar_multi_python(vector1, vector2)
time_smn, val_smn = scalar_multi_numpy(np.array(vector1), np.array(vector2))

point1 = 0
point2 = 10
step = 0.000_000_1
time_ip, val_ip = integral_python(point1, point2, step)
time_in, val_in = integral_numpy(point1, point2, step)


matrix = [[2, 6, 4, 8],
        [1, -3, 2, 5],
        [2, 2, 4, 6],
        [9, -2, -4, 8]]
np_matrix = np.array(matrix)
time_det_p, val_det_p = determinant_python(matrix)
time_det_n, val_det_n = determinant_numpy(np_matrix)

mat1 = [[3, 6],
        [-2, 8]]
mat2 = [[9, 3],
        [5, -4]]
time_mmp, val_mmp = matrix_multi_python(mat1, mat2)
time_mmn, val_mmn = matrix_multi_numpy(mat1, mat2)

pointX = 5
dx = 0.000_000_1
func = "5**x+3*x"
time_dp, val_dp = derivative_python(pointX, dx, func)
time_ds, val_ds = derivative_special(pointX, dx, func)

"""
Čas potřebný k provedení funkce 'scalar_multi_python' byl 0.060652971267700195s. Výstup: -215098
Čas potřebný k provedení funkce 'scalar_multi_numpy' byl 0.0009989738464355469s. Výstup: -215098
Čas potřebný k provedení funkce 'integral_python' byl 15.285130500793457s. Výstup: 170.00000170000013
Čas potřebný k provedení funkce 'integral_numpy' byl 1.34114670753479s. Výstup: 169.99999999999997
Čas potřebný k provedení funkce 'determinant_python' byl 0.0s. Výstup: 703.9999999999999
Čas potřebný k provedení funkce 'determinant_numpy' byl 0.0s. Výstup: 704.0000000000005
Čas potřebný k provedení funkce 'matrix_multi_python' byl 0.0s. Výstup: [[57, -15], [22, -38]]
Čas potřebný k provedení funkce 'matrix_multi_numpy' byl 0.0009908676147460938s. Výstup: [[ 57 -15]
                                                                                          [ 22 -38]]
Čas potřebný k provedení funkce 'derivative_python' byl 0.0s. Výstup: 5032.493895669177
Čas potřebný k provedení funkce 'derivative_special' byl 0.0010039806365966797s. Výstup: 5032.493490944034
"""