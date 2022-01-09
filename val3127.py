from sympy import *
import re

#   3127 = 59 * 53

# 0b110000110111

#59
#0b111011

#53
#0b110101

n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "110000110111"]




p4, p3, p2, p1 = symbols("p4 p3 p2 p1")
q4, q3, q2, q1 = symbols("q4 q3 q2 q1")

#p4, p3, p2, p1 = [1,1,0,1]
#q4, q3, q2, q1 = [1,0,1,0]

c7, c6, c5, c4, c3, c2, c1 = symbols("c7 c6 c5 c4 c3 c2 c1")

#o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) - n1 - 2*n2 - 4*n3 - 8*c1 - 16*c2)**2
#o2 = ((p4 + p3*q1 + p2*q2 + p1*q3 + q4 + c1) + 2*(1 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + 1 + c2) + 4*(q1 + p4*q2 + p3*q3 + p2*q4 + p1) - n4 - 2*n5 - 4*n6 - 8*c3 - 16*c4 - 32*c5)**2
#o3 = ((q2 + p4*q3 + p3*q4 + p2 + c3) + 2*(q3 + p4*q4 + p3 + c4) + 4*(q4 + p4 + c5) - n7 - 2*n8 - 4*n9 - 8*c6 - 16*c7) ** 2
#o4 = ((1 + c6) + 2*(c7) - n10 - 2*n11)**2

c7, c6 = [1, 0]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) - n1 - 2*n2 - 4*n3 - 8*c1 - 16*c2)**2
o2 = ((p4 + p3*q1 + p2*q2 + p1*q3 + q4 + c1) + 2*(1 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + 1 + c2) + 4*(q1 + p4*q2 + p3*q3 + p2*q4 + p1) - n4 - 2*n5 - 4*n6 - 8*c3 - 16*c4 - 32*c5)**2
o3 = ((q2 + p4*q3 + p3*q4 + p2 + c3) + 2*(q3 + p4*q4 + p3 + c4) + 4*(q4 + p4 + c5) - n7 - 2*n8 - 4*n9 - 8*c6 - 16*c7) ** 2
o4 = ((1 + c6) + 2*(c7) - n10 - 2*n11)**2



o = o1 + o2 + o3 + o4

o = expand(o)

o = o.subs(p4**2, p4)
o = o.subs(p3**2, p3)
o = o.subs(p2**2, p2)
o = o.subs(p1**2, p1)

o = o.subs(q4**2, q4)
o = o.subs(q3**2, q3)
o = o.subs(q2**2, q2)
o = o.subs(q1**2, q1)

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
