#Make BQM and make it quadratic
#Get embedding on graph
#Get embedding on machine
#Run problem in actual solver

import time
import json

import dimod
import minorminer
import dwave_networkx as dnx
from dwave.system import DWaveSampler, EmbeddingComposite

from dimod import ExactSolver
from neal.sampler import SimulatedAnnealingSampler



problemFile = open("problemDict.txt", "r")
problem = eval(problemFile.read())
problemFile.close()

500
#500000000

#50,000
quadraticProblem = dimod.make_quadratic(problem, 50000, dimod.BINARY)
#500000000


print(type(quadraticProblem))

#qpu_2000q = DWaveSampler(solver={"topology__type": "chimera"})
#net2000q = qpu_2000q.to_networkx_graph()

qpu_advantage = DWaveSampler(solver={"topology__type": "pegasus"})
#netAdvantage = qpu_advantage.to_networkx_graph()





#from dwave.system import LeapHybridBQMSampler, LeapHybridCQMSampler


# Select a standard BQM solver

#bqm_solver_selection = LeapHybridBQMSampler.default_solver
#bqm_solver_selection.update(name__regex=".*(?<!bulk)$")
#sampler_bqm = LeapHybridBQMSampler(solver=bqm_solver_selection)  


#et2000Start = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
#embedding2000q = minorminer.find_embedding(quadraticProblem.quadratic, net2000q)
#et2000End = time.clock_gettime_ns(time.CLOCK_MONOTONIC)

#etAstart = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
#embeddingAdvantage = minorminer.find_embedding(quadraticProblem.quadratic, netAdvantage)
#etAEnd = time.clock_gettime_ns(time.CLOCK_MONOTONIC)

#embeddingTime2000 = et2000End - et2000Start
#embeddingTimeA = etAEnd - etAstart

logicalVariables = 0
for x in quadraticProblem.iter_variables():
    logicalVariables += 1

#logicalQuadratic = 0
#for x in quadraticProblem.quadratic:
#    logicalQuadratic += 1


#variables2000q = 0
#for x in embedding2000q:
#    variables2000q += len(embedding2000q[x])


#variablesAdvantage = 0
#for x in embeddingAdvantage:
#    variablesAdvantage += len(embeddingAdvantage[x])


# 659 = 1010010011
# 571 = 1000111011

#-123 energy
"""
quadraticProblem.fix_variable("q1",1)
quadraticProblem.fix_variable("q2",0)
quadraticProblem.fix_variable("q3",0)
quadraticProblem.fix_variable("q4",1)
quadraticProblem.fix_variable("q5",0)
quadraticProblem.fix_variable("q6",0)
quadraticProblem.fix_variable("q7",1)
quadraticProblem.fix_variable("q8",0)
quadraticProblem.fix_variable("q9",1)

quadraticProblem.fix_variable("p1",1)
quadraticProblem.fix_variable("p2",0)
quadraticProblem.fix_variable("p3",1)
quadraticProblem.fix_variable("p4",1)
quadraticProblem.fix_variable("p5",1)
quadraticProblem.fix_variable("p6",0)
quadraticProblem.fix_variable("p7",0)
quadraticProblem.fix_variable("p8",0)
quadraticProblem.fix_variable("p9",1)
"""


#solver = ExactSolver()
solver = SimulatedAnnealingSampler()
#solver = qpu_2000q

sampler = EmbeddingComposite(qpu_advantage) 

print("Logical variables: " + str(logicalVariables))

startTime = time.clock_gettime_ns(time.CLOCK_MONOTONIC)

#sampleset = sampler.sample(quadraticProblem, num_reads = 10000, annealing_time = 50)
sampleset = solver.sample(quadraticProblem, num_reads = 100000)

#sampleset = sampler_bqm.sample(quadraticProblem, num_reads=10000)
#print(sampleset.info)


endTime = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
totalSamples = len(sampleset.record)


serial = sampleset.to_serializable()
outfile = open("outSample.txt", "w")
outfile.write(json.dumps(serial))
outfile.close()


sampleset = sampleset.lowest()


print("Samples: " + str(len(sampleset.samples())))
results = set()
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
    results.add(p + " " + q)

    #print(q)

for x in results:
    print(x)


print(sampleset.record.energy)
#print("Logical variables: " + str(logicalVariables))
#print("2000q variables: " + str(variables2000q))
#print("Advantage variables: " + str(variablesAdvantage))

#print("Embedding time 2000Q: " + str(embeddingTime2000) + " " + str(embeddingTime2000 / float(10**9)))
#print("Embedding time Advantage: " + str(embeddingTimeA) + " " + str(embeddingTimeA / float(10**9)))


#print("")
#print("Logical quadratic: " + str(logicalQuadratic))

print("Samples: " + str(totalSamples) + " " + str(len(sampleset.record)))
print("Time: " + str(endTime - startTime) + " " + str((endTime - startTime) / float(10**9)))
