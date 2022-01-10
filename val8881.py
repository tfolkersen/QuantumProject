from sympy import *
import re


# 8881 = 10001010110001
# 107 = 1101011
# 83 = 1010011

p5, p4, p3, p2, p1 = symbols("p5 p4 p3 p2 p1")
q5, q4, q3, q2, q1 = symbols("q5 q4 q3 q2 q1")
c9, c8, c7, c6, c5, c4, c3, c2, c1 = symbols("c9 c8 c7 c6 c5 c4 c3 c2 c1")
n13, n12, n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "10001010110001"]


c9 = 0
c8 = 0

#p5, p4, p3, p2, p1 = [int(i) for i in "10101"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) + 8*(p4 + p3*q1 + p2*q2 + p1*q3 + q4) - n1 - 2*n2 - 4*n3 - 8*n4 - 16*c1 - 32*c2 - 64*c3)**2
o2 = ((p5 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + q5 + c1) + 2*(1 + p5*q1 + p4*q2 + p3*q3 + p2*q4 + p1*q5 + 1 + c2) + 4*(q1 + p5*q2 + p4*q3 + p3*q4 + p2*q5 + p1 + c3) - n5 - 2*n6 - 4*n7 - 8*c4 - 16*c5 - 32*c6)**2
o3 = ((q2 + p5*q3 + p4*q4 + p3*q5 + p2 + c4) + 2*(q3 + p5*q4 + p4*q5 + p3 + c5) + 4*(q4 + p5*q5 + p4 + c6) - n8 - 2*n9 - 4*n10 - 8*c7 - 16*c8 - 32*c9)**2
o4 = ((q5 + p5 + c7) + 2*(1 + c8) + 4*(c9) - n11 - 2*n12 - 4*n13)**2

o = o1 + o2 + o3 + o4

o = expand(o)

o = o.subs(p5**2, p5)
o = o.subs(p4**2, p4)
o = o.subs(p3**2, p3)
o = o.subs(p2**2, p2)
o = o.subs(p1**2, p1)

o = o.subs(q5**2, q5)
o = o.subs(q4**2, q4)
o = o.subs(q3**2, q3)
o = o.subs(q2**2, q2)
o = o.subs(q1**2, q1)

#o = o.subs(c10**2, c10)
o = o.subs(c9**2, c9)
o = o.subs(c8**2, c8)
o = o.subs(c7**2, c7)
o = o.subs(c6**2, c6)
o = o.subs(c5**2, c5)
o = o.subs(c4**2, c4)
o = o.subs(c3**2, c3)
o = o.subs(c2**2, c2)
o = o.subs(c1**2, c1)

o = expand(o)

expr = str(o)

problem = {}

termRe = re.compile("[\-\+]?(\ )?[0-9a-zA-Z\*]+")
numberRe = re.compile("[0-9]+")

term = termRe.search(expr)
while not term is None:
    text = term.group(0)
    
    sign = 1
    if text[0] == "-":
        sign = -1

    while text[0] in [" ", "-", "+"]:
        text = text[1:]

    numberMatch = numberRe.match(text)
    coefficient = sign
    if not numberMatch is None:
        coefficient = sign * int(numberMatch.group(0))
        text = text[numberMatch.span()[1]:]

    stripped = text.strip("*")
    if stripped != "":
        variables = stripped.split("*")

        problem[tuple(variables)] = coefficient

    term = termRe.search(expr, term.span()[1])

print(problem)
