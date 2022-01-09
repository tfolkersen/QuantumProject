from sympy import *
import re

#143 = 11 * 13

# 13 = 1101

# 11 = 1011

p2, p1, q2, q1, c4, c3, c2, c1 = symbols("p2 p1 q2 q1 c4 c3 c2 c1")
n7, n6, n5, n4, n3, n2, n1, n0 = [1,0,0,0,1,1,1,1]

o1 = ((p1 + q1) + 2*(p2 + q1*p1 + q2) - n1 - 2*n2 - 4*c1 - 8*c2)**2
o2 = ((2 + q1*p2 + q2*p1 + c1) + 2*(q1 + q2*p2 + p1 + c2) - n3 - 2*n4 - 4*c3 - 8*c4)**2
o3 = ((q2 + p2 + c3) + 2*(1 + c4) - n5 - 2*n6 - 4*n7)**2

o = o1 + o2 + o3



o = expand(o)

o = o.subs(p2**2, p2)
o = o.subs(p1**2, p1)
o = o.subs(q2**2, q2)
o = o.subs(q1**2, q1)
o = o.subs(c4**2, c4)
o = o.subs(c3**2, c3)
o = o.subs(c2**2, c2)
o = o.subs(c1**2, c1)

o = expand(o)

expr = str(o)
print(expr)



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
