#Make BQM and make it quadratic
#Get embedding on graph

#Get embedding on machine
#Run problem in actual solver

import dimod
import minorminer
import dwave_networkx as dnx
from dwave.system import DWaveSampler

problem = {('c1', 'c2'): 68, ('c1', 'c3'): -8, ('c1', 'c4'): -16, ('c1', 'p1', 'q1'): -16, ('c1', 'p1', 'q2'): 2, ('c1', 'p1'): -4, ('c1', 'p2', 'q1'): 2, ('c1', 'p2', 'q2'): 4, ('c1', 'p2'): -16, ('c1', 'q1'): -4, ('c1', 'q2'): -16, ('c1',): 43, ('c2', 'c3'): -16, ('c2', 'c4'): -32, ('c2', 'p1', 'q1'): -32, ('c2', 'p1', 'q2'): 4, ('c2', 'p1'): -8, ('c2', 'p2', 'q1'): 4, ('c2', 'p2', 'q2'): 8, ('c2', 'p2'): -32, ('c2', 'q1'): -8, ('c2', 'q2'): -32, ('c2',): 120, ('c3', 'c4'): 68, ('c3', 'p1', 'q2'): -8, ('c3', 'p1'): -16, ('c3', 'p2', 'q1'): -8, ('c3', 'p2', 'q2'): -16, ('c3', 'p2'): 2, ('c3', 'q1'): -16, ('c3', 'q2'): 2, ('c3',): 5, ('c4', 'p1', 'q2'): -16, ('c4', 'p1'): -32, ('c4', 'p2', 'q1'): -16, ('c4', 'p2', 'q2'): -32, ('c4', 'p2'): 4, ('c4', 'q1'): -32, ('c4', 'q2'): 4, ('c4',): 44, ('p1', 'p2', 'q1', 'q2'): 2, ('p1', 'p2', 'q1'): 12, ('p1', 'p2', 'q2'): 12, ('p1', 'p2'): 4, ('p1', 'q1', 'q2'): 12, ('p1', 'q1'): 10, ('p1', 'q2'): 11, ('p1',): 3, ('p2', 'q1', 'q2'): 12, ('p2', 'q1'): 11, ('p2', 'q2'): 18, ('p2',): -11, ('q1', 'q2'): 4, ('q1',): 3, ('q2',): -11}

quadraticProblem = dimod.make_quadratic(problem, 5, dimod.BINARY)


#qpu_2000q = DWaveSampler(solver={"topology__type": "chimera"})
#network = qpu_2000q.to_networkx_graph()

#qpu_advantage = DWaveSampler(solver={"topology__type": "pegasus"})
#network = qpu_advantage.to_networkx_graph()

network = dnx.chimera_graph(m=16,n=16,t=4)


embedding = minorminer.find_embedding(quadraticProblem.quadratic, network)


print(embedding)

logicalVariables = 0
for x in quadraticProblem.iter_variables():
    logicalVariables += 1

physicalVariables = 0
for x in embedding:
    physicalVariables += len(embedding[x])

print("")
print("Logical variables: " + str(logicalVariables))
print("Physical variables: " + str(physicalVariables))
