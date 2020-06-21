from data import read
import numpy as np
from makespan import makespan
'''
def _calc_makespan(jobMatrix, jobOrder):
    nb_machine, _ = jobMatrix.shape
    nb_jobs = len(jobOrder)
    
    ganttTable = np.zeros((nb_jobs,nb_machine*2))

    for i in range(0,nb_jobs):
        for j in range(0,nb_machine):
            ganttTable[i,2*j] = max(ganttTable[i-1,2*j+1],ganttTable[i,2*j-1])# Start of the job "i" in machine "j"
            ganttTable[i,2*j+1] = ganttTable[i,2*j] + jobMatrix[j,jobOrder[i]] # End of the job "i" in machine "j"
    return ganttTable[-1,-1]
'''

def neh(jobMatrix):
    jobs_with_total_times = [(job_id, sum(job)) for job_id, job in enumerate(jobMatrix.T)]
    order = []
    for job in sorted(jobs_with_total_times, key=lambda x: x[1], reverse = True):
        candidates = []
        for i in range(0, len(order) + 1):
            candidate = order[:i] + [job[0]] + order[i:]
            candidates.append((candidate, makespan(candidate, jobMatrix)))
        order = min(candidates, key = lambda x: x[1])[0]
    #print(makespan(order, jobMatrix))
    return (order, makespan(order, jobMatrix))

'''
path = './data/ta20_20.txt'
M = read(path, 20)

nb_machines, nb_jobs = M.shape
print("we have "+str(nb_machines) + " machines each one must do " + str(nb_jobs) + " jobs")
res = neh(M)
print(res)
'''

