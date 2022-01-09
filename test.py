import sympy
from sympy import *

x, y, z, l, m = symbols("x y z l m")

x = 2*x*y

print(type(x))
for i in x.args:
    print(type(i))
    i.subs(i,1)
print(expand(x))

def find(expr):
    for i in expr.args:
        if type(i) is sympy.core.mul.Mul:
            print(i)


    


p1, p2, q1, q2, c1, c2, c3, c4 = symbols("p1 p2 q1 q2 c1 c2 c3 c4")


n7, n6, n5, n4, n3, n2, n1, n0 = [1,0,0,0,1,1,1,1]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) - (8*c2 + 4*c1) - (n1 + 2*n2))**2
o2 = ((1 + p2*q1 + p1*q2 + 1 + c1) + 2*(q1 + p2*q2 + p1 + c2) - (8*c4 + 4*c3) - (n3 + 2*n4))**2
o3 = ((q2 + p2 + c3) + 2*(1 + c4) - (n5 + 2*n6 + 4*n7))**2

o = o1 + o2 + o3
o = expand(o)
print(expand(o))
print("")


o = o.subs(p1**2, p1)
o = o.subs(p2**2, p2)
o = o.subs(q1**2, q1)
o = o.subs(q2**2, q2)

o = o.subs(c1**2, c1)
o = o.subs(c2**2, c2)
o = o.subs(c3**2, c3)
o = o.subs(c4**2, c4)


print(expand(o))
print("")

find(o)

