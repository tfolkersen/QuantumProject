import dimod
import minorminer
import dwave_networkx as dnx
from dwave.system import DWaveSampler

import time
from dimod import ExactSolver
from neal.sampler import SimulatedAnnealingSampler


import dwavebinarycsp as dbc


csp = dbc.factories.multiplication_circuit(9)
bqm = dbc.stitch(csp, min_classical_gap=0.3)



number = "111000011001111101"
number = "1110101001010101"
number = "10001010110001"
number = "110000110111"
number = "0110000111"
number = "10001111"

number = "01011011110111100001"

number = "10001111"

number = "0110000111"

number = "110000110111"

number = "10001010110001"



number = "1110101001010101"

number = "111000011001111101"


for i in range(0, len(number)):
    bqm.fix_variable("p" + str(i), int(number[len(number) - 1 - i]))

bqm.fix_variable("a0", 1)
bqm.fix_variable("b0", 1)



#network = dnx.chimera_graph(m=16, n=16, t=4)

#embedding = minorminer.find_embedding(bqm.quadratic, network)


logicalVariables = 0
for x in bqm.iter_variables():
    logicalVariables += 1

#physicalVariables = 0
#for x in embedding:
#    physicalVariables += len(embedding[x])

print("Logical variables: " + str(logicalVariables))
#print("Physical variables: " + str(physicalVariables))

solver = SimulatedAnnealingSampler()


startTime = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
sampleset = solver.sample(bqm, num_reads = 100000)
endTime = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
totalSamples = len(sampleset.record)
sampleset = sampleset.lowest()




print(sampleset.record.energy)

print("Samples: " + str(len(sampleset.samples())))


results = set()
for s in sampleset.samples():
    a = "1"
    b = "1"
    i = 1
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

    results.add(a + " " + b)

for x in results:
    print(x)

print("Time: " + str(endTime - startTime) + " " + str((endTime - startTime) / float(10**9)))
