from sympy import *
import re


p8, p7, p6, p5, p4, p3, p2, p1 = symbols("p8 p7 p6 p5 p4 p3 p2 p1")
q8, q7, q6, q5, q4, q3, q2, q1 = symbols("q8 q7 q6 q5 q4 q3 q2 q1")
c15, c14, c13, c12, c11, c10, c9, c8, c7, c6, c5, c4, c3, c2, c1 = symbols("c15 c14 c13 c12 c11 c10 c9 c8 c7 c6 c5 c4 c3 c2 c1")

"""
# N = 8
# 143 = 10001111
# 13 = 1101
# 11 = 1011
n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "10001111"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) - n1 - 2*n2 - 4*c1 - 8*c2)**2
o2 = ((1 + p2*q1 + p1*q1 + 1 + c1) + 2*(q1 + p2*q2 + p1 + c2) - n3 - 2*n4 - 4*c3 - 8*c4)**2
o3 = ((q2 + p2 + c3) + 2*(1 + c4) - n5 - 2*n6 - 4*n7)**2

o = o1 + o2 + o3
"""

"""
# N = 10
# 391 = 0110000111
# 23 = 10111
# 17 = 10001

n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "0110000111"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) - n1 - 2*n2 - 4*n3 - 8*c1 - 16*c2)**2
o2 = ((1 + p3*q1 + p2*q2 + p1*q3 + 1 + c1) + 2*(q1 + p3*q2 + p2*q3 + p1 + c2) + 4*(q2 + p3*q3 + p2) - n4 - 2*n5 - 4*n6 - 8*c3 - 16*c4)**2
o3 = ((q3 + p3 + c3) + 2*(1 + c4) - n7 - 2*n8 - 4*n9)**2

o = o1 + o2 + o3
"""

"""
# N = 12
# 3127 = 110000110111
# 59 = 111011
# 53 = 110101
n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "110000110111"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) - n1 - 2*n2 - 4*n3 - 8*c1 - 16*c2)**2
o2 = ((p4 + p3*q1 + p2*q2 + p1*q3 + q4 + c1) + 2*(1 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + 1 + c2) + 4*(q1 + p4*q2 + p3*q3 + p2*q4 + p1) - n4 - 2*n5 - 8*n6 - 16*c3 - 32*c4 - 64*c5)**2
o3 = ((q2 + p4*q3 + p3*q4 + p2 + c3) + 2*(q3 + p4*q4 + p3 + c4) + 4*(q4 + p4 + c5) - n7 - 2*n8 - 4*n9 - 8*c6 - 16*c7)**2
o4 = ((1 + c6) + 2*c7 - n10 - 2*n11)**2

o = o1 + o2 + o3 + o4
"""

"""
# N = 14
# 8881 = 10001010110001
# 107 = 1101011
# 83 = 1010011
n13, n12, n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "10001010110001"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) + 8*(p4 + p3*q1 + p2*q2 + p1*q3 + q4) - n1 - 2*n2 - 4*n3 - 8*n4 - 16*c1 - 32*c2 - 64*c3)**2
o2 = ((p5 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + q5 + c1) + 2*(1 + p5*q1 + p4*q2 + p3*q3 + p2*q4 + p1*q5 + 1 + c2) + 4*(q1 + p5*q2 + p4*q3 + p3*q4 + p2*q5 + p1 + c3) - n5 - 2*n6 - 4*n7 - 8*c4 - 16*c5 - 32*c6)**2
o3 = ((q2 + p5*q3 + p4*q4 + p3*q5 + p2 + c4) + 2*(q3 + p5*q4 + p4*q5 + p3 + c5) + 4*(q4 + p5*q5 + p4 + c6) - n8 - 2*n9 - 4*n10 - 8*c7 - 16*c8 - 32*c9)**2
o4 = ((q5 + p5 + c7) + 2*(1 + c8) + 4*c9 - n11 - 2*n12 - 4*n13)**2

o = o1 + o2 + o3 + o4
"""

"""
# N = 16
# 59989 = 1110101001010101
# 251 = 11111011
# 239 = 11101111
n15, n14, n13, n12, n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "1110101001010101"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) + 8*(p4 + p3*q1 + p2*q2 + p1*q3 + q4) - n1 - 2*n2 - 4*n3 - 8*n4 - 16*c1 - 32*c2 - 64*c3)**2
o2 = ((p5 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + q5 + c1) + 2*(p6 + p5*q1 + p4*q2 + p3*q3 + p2*q4 + p1*q5 + q6 + c2) + 4*(1 + p6*q1 + p5*q2 + p4*q3 + p3*q4 + p2*q5 + p1*q6 + 1 + c3) - n5 - 2*n6 - 4*n7 - 8*c4 - 16*c5 - 32*c6)**2
o3 = ((q1 + p6*q2 + p5*q3 + p4*q4 + p3*q5 + p2*q6 + p1 + c4) + 2*(q2 + p6*q3 + p5*q4 + p4*q5 + p3*q6 + p2 + c5) + 4*(q3 + p6*q4 + p5*q5 + p4*q6 + p3 + c6) - n8 - 2*n9 - 4*n10 - 8*c7 - 16*c8 - 32*c9)**2
o4 = ((q4 + p6*q5 + p5*q6 + p4 + c7) + 2*(q5 + p6*q6 + p5 + c8) + 4*(q6 + p6 + c9) - n11 - 2*n12 - 4*n13 - 8*c10 - 16*c11)**2
o5 = ((1 + c10) + 2*c11 - n14 - 2*n15)**2

o = o1 + o2 + o3 + o4 + o5
"""

"""
# N = 18
# 231037 = 111000011001111101
# 499 = 111110011
# 463 = 111001111
n17, n16, n15, n14, n13, n12, n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "111000011001111101"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) + 8*(p4 + p3*q1 + p2*q2 + p1*q3 + q4) - n1 - 2*n2 - 4*n3 - 8*n4 - 16*c1 - 32*c2 - 64*c3)**2
o2 = ((p5 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + q5 + c1) + 2*(p6 + p5*q1 + p4*q2 + p3*q3 + p2*q4 + p1*q5 + q6 + c2) + 4*(p7 + p6*q1 + p5*q2 + p4*q3 + p3*q4 + p2*q5 + p1*q6 + q7 + c3) - n5 - 2*n6 - 4*n7 - 8*c4 - 16*c5 - 32*c6)**2
o3 = ((1 + p7*q1 + p6*q2 + p5*q3 + p4*q4 + p3*q5 + p2*q6 + p1*q7 + 1 + c4) + 2*(q1 + p7*q2 + p6*q3 + p5*q4 + p4*q5 + p3*q6 + p2*q7 + p1 + c5) + 4*(q2 + p7*q3 + p6*q4 + p5*q5 + p4*q6 + p3*q7 + p2 + c6) - n8 - 2*n9 - 4*n10 - 8*c7 - 16*c8 - 32*c9)**2
o4 = ((q3 + p7*q4 + p6*q5 + p5*q6 + p4*q7 + p3 + c7) + 2*(q4 + p7*q5 + p6*q6 + p5*q7 + p4 + c8) + 4*(q5 + p7*q6 + p6*q7 + p5 + c9) - n11 - 2*n12 - 4*n13 - 8*c10 - 16*c11 - 32*c12)**2
o5 = ((q6 + p7*q7 + p6 + c10) + 2*(q7 + p7 + c11) + 4*(1 + c12) - n14 - 2*n15 - 4*n16 - 8*n17)**2

o = o1 + o2 + o3 + o4 + o5
"""

"""
# N = 19
# 376289 = 1011011110111100001
# 659 = 1010010011
# 571 = 1000111011
n19, n18, n17, n16, n15, n14, n13, n12, n11, n10, n9, n8, n7, n6, n5, n4, n3, n2, n1, n0 = [int(i) for i in "01011011110111100001"]

o1 = ((p1 + q1) + 2*(p2 + p1*q1 + q2) + 4*(p3 + p2*q1 + p1*q2 + q3) + 8*(p4 + p3*q1 + p2*q2 + p1*q3 + q4) - n1 - 2*n2 - 4*n3 - 8*n4 - 16*c1 - 32*c2 - 64*c3)**2
o2 = ((p5 + p4*q1 + p3*q2 + p2*q3 + p1*q4 + q5 + c1) + 2*(p6 + p5*q1 + p4*q2 + p3*q3 + p2*q4 + p1*q5 + q6 + c2) + 4*(p7 + p6*q1 + p5*q2 + p4*q3 + p3*q4 + p2*q5 + p1*q6 + q7 + c3) - n5 - 2*n6 - 4*n7 - 8*c4 - 16*c5 - 32*c6)**2
o3 = ((p8 + p7*q1 + p6*q2 + p5*q3 + p4*q4 + p3*q5 + p2*q6 + p1*q7 + q8 + c4) + 2*(1 + p8*q1 + p7*q2 + p6*q3 + p5*q4 + p4*q5 + p3*q6 + p2*q7 + p1*q8 + 1 + c5) + 4*(q1 + p8*q2 + p7*q3 + p6*q4 + p5*q5 + p4*q6 + p3*q7 + p2*q8 + p1 + c6) - n8 - 2*n9 - 4*n10 - 8*c7 - 16*c8 - 32*c9 - 64*c10)**2
o4 = ((q2 + p8*q3 + p7*q4 + p6*q5 + p5*q6 + p5*q6 + p4*q7 + p3*q8 + p2 + c7) + 2*(q3 + p8*q4 + p7*q5 + p6*q6 + p5*q7 + p4*q8 + p3 + c8) + 4*(q4 + p8*q5 + p7*q6 + p6*q7 + p5*q8 + p4 + c9) - n11 - 2*n12 - 4*n13 - 8*c11 - 16*c12 - 32*c13)**2
o5 = ((q5 + p8*q6 + p7*q7 + p6*q8 + p5 + c10 + c11) + 2*(q6 + p8*q7 + p7*q8 + p6 + c12) + 4*(q7 + p8*q8 + p7 + c13) - n15 - 2*n16 - 4*n17 - 8*c14 - 16*c15)**2
o6 = ((q8 + p8 + c14) + 2*(1 + c15) - n18 - 2*n19)**2

o = o1 + o2 + o3 + o4 + o5 + o6
"""

o = expand(o)

o = o.subs(p8**2, p8)
o = o.subs(p7**2, p7)
o = o.subs(p6**2, p6)
o = o.subs(p5**2, p5)
o = o.subs(p4**2, p4)
o = o.subs(p3**2, p3)
o = o.subs(p2**2, p2)
o = o.subs(p1**2, p1)

o = o.subs(q8**2, q8)
o = o.subs(q7**2, q7)
o = o.subs(q6**2, q6)
o = o.subs(q5**2, q5)
o = o.subs(q4**2, q4)
o = o.subs(q3**2, q3)
o = o.subs(q2**2, q2)
o = o.subs(q1**2, q1)


o = o.subs(c15**2, c15)
o = o.subs(c14**2, c14)
o = o.subs(c13**2, c13)
o = o.subs(c12**2, c12)
o = o.subs(c11**2, c11)
o = o.subs(c10**2, c10)
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
