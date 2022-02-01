from sympy import Symbol
from sympy import Poly
from sympy.solvers.inequalities import solve_rational_inequalities, solve_poly_inequalities


x = Symbol('x', real=True)
y = Symbol('y', real=True)
z = Symbol('z', real=True)
w = solve_poly_inequalities((
    (Poly(x+y+z-8), "="),
    (Poly(x-1), ">="),
    (Poly(y), ">="),
    (Poly(z-1), ">=")
    ))

print(w)