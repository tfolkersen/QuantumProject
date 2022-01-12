import dimod
import minorminer
import dwave_networkx as dnx
from dwave.system import DWaveSampler

from dimod import ExactSolver
from neal.sampler import SimulatedAnnealingSampler


import dwavebinarycsp as dbc


csp = dbc.factories.multiplication_circuit(8)

bqm = dbc.stitch(csp, min_classical_gap=0.1)


number = "1110101001010101"

for i in range(0, len(number)):
    bqm.fix_variable("p" + str(i), int(number[len(number) - 1 - i]))


network = dnx.chimera_graph(m=16, n=16, t=4)

embedding = minorminer.find_embedding(bqm.quadratic, network)


logicalVariables = 0
for x in bqm.iter_variables():
    logicalVariables += 1

physicalVariables = 0
for x in embedding:
    physicalVariables += len(embedding[x])

print("Logical variables: " + str(logicalVariables))
print("Physical variables: " + str(physicalVariables))

solver = SimulatedAnnealingSampler()
sampleset = solver.sample(bqm, num_reads = 10000).lowest()




print(sampleset.record.energy)

print("Samples: " + str(len(sampleset.samples())))
for s in sampleset.samples():
    a = ""
    b = ""
    i = 0
    while True:
        aName = "a" + str(i)
        bName = "b" + str(i)

        exceptions = 0

        try:
            a = str(s[aName]) + a
        except:
            exceptions += 1

        try:
            b = str(s[bName]) + b
        except:
            exceptions += 1

        if exceptions == 2:
            break

        i += 1

    print(a + " " + b)





