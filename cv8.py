import sympy as sp

"""
Zadání:
Numerická derivace je velice krátké téma.
V hodinách jste se dozvěděli o nejvyužívanějších typech numerické derivace (dopředná, zpětná, centrální).
Jedno z neřešených témat na hodinách byl problém volby kroku. V praxi je vhodné mít krok dynamicky nastavitelný.
Algoritmům tohoto typu se říká derivace s adaptabilním krokem. Cílem tohoto zadání je napsat program,
který provede numerickou derivaci s adaptabilním krokem pro vámi vybranou funkci.
Proveďte srovnání se statickým krokem a analytickým řešením.
"""

function = "x**3-3*x+8*x**2"
f = lambda x: eval(function)

def analytical_derivative(func_str, x):
    eq = sp.sympify(func_str)
    xs = sp.symbols("x")
    eq_d = sp.diff(eq, xs)
    return eq_d.subs(xs, x)

def adaptive_derivative(func, x, step = 1e-5, tolerance = 1e-7):
    previous_derivative = None
    while True:
        forward_point = x + step
        backward_point = x - step
        
        forward_difference = (func(forward_point) - func(x)) / step
        backward_difference = (func(x) - func(backward_point)) / step
        
        derivative = (forward_difference + backward_difference) / 2
        
        if previous_derivative is not None:
            if abs(derivative - previous_derivative) < tolerance:
                break
        
        step /= 2
        previous_derivative = derivative
    
    return derivative

x = 2.0

numerical_result = adaptive_derivative(f, x)
analytical_result = analytical_derivative(function, x)

print(f"Numerická derivace: {numerical_result}")
print(f"Analytická derivace: {analytical_result}")

"""
Numerická derivace: 40.99999999951365
Analytická derivace: 41.0000000000000
"""