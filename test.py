#Make BQM and make it quadratic
#Get embedding on graph
#Get embedding on machine
#Run problem in actual solver

import dimod
import minorminer
import dwave_networkx as dnx
from dwave.system import DWaveSampler

from dimod import ExactSolver
from neal.sampler import SimulatedAnnealingSampler


problemFile = open("problemDict.txt", "r")
problem = eval(problemFile.read())
problemFile.close()

quadraticProblem = dimod.make_quadratic(problem, 50000000, dimod.BINARY)


#qpu_2000q = DWaveSampler(solver={"topology__type": "chimera"})
#network = qpu_2000q.to_networkx_graph()

#qpu_advantage = DWaveSampler(solver={"topology__type": "pegasus"})
#network = qpu_advantage.to_networkx_graph()

network = dnx.chimera_graph(m=16, n=16, t=4)


embedding = minorminer.find_embedding(quadraticProblem.quadratic, network)


logicalVariables = 0
for x in quadraticProblem.iter_variables():
    logicalVariables += 1

physicalVariables = 0
for x in embedding:
    physicalVariables += len(embedding[x])

print("Logical variables: " + str(logicalVariables))
print("Physical variables: " + str(physicalVariables))


"""
quadraticProblem.fix_variable("q1",1)
quadraticProblem.fix_variable("q2",0)
quadraticProblem.fix_variable("q3",0)
quadraticProblem.fix_variable("q4",1)
quadraticProblem.fix_variable("q5",0)
quadraticProblem.fix_variable("q6",0)
quadraticProblem.fix_variable("q7",1)
quadraticProblem.fix_variable("q8",0)

quadraticProblem.fix_variable("p1",1)
quadraticProblem.fix_variable("p2",0)
quadraticProblem.fix_variable("p3",1)
quadraticProblem.fix_variable("p4",1)
quadraticProblem.fix_variable("p5",1)
quadraticProblem.fix_variable("p6",0)
quadraticProblem.fix_variable("p7",0)
quadraticProblem.fix_variable("p8",0)
"""

#solver = ExactSolver()
solver = SimulatedAnnealingSampler()
sampleset = solver.sample(quadraticProblem, num_reads = 300000).lowest()
print(sampleset.record.energy)

print("Samples: " + str(len(sampleset.samples())))
for s in sampleset.samples():
    p = "1"
    q = "1"

    i = 1
    while True:
        pName = "p" + str(i)
        qName = "q" + str(i)

        exceptions = 0

        try:
            p = str(s[pName]) + p
        except:
            exceptions += 1

        try:
            q = str(s[qName]) + q
        except:
            exceptions += 1

        if exceptions == 2:
            break

        i += 1

    #p = "1" + p
    #q = "1" + q

    #p = "1" + str(s["p4"]) + str(s["p3"]) + str(s["p2"]) + str(s["p1"]) + "1"
    #q = "1" + str(s["q4"]) + str(s["q3"]) + str(s["q2"]) + str(s["q1"]) + "1"
    print(p + " " + q)

    #print(q)


