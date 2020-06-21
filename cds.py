import numpy as np
import matplotlib.pyplot as plt

import data as dataReader
from makespan import makespan


def plotGantt(jobMatrix,jobOrder,nom):
    fig, ax = plt.subplots()

    nb_machine, nb_jobs = jobMatrix.shape
    ganttTable = _calc_makespan(jobMatrix,jobOrder,True)
    for i in range(nb_jobs):
        ax.broken_barh([(ganttTable[i,0], ganttTable[i,1]-ganttTable[i,0]), (ganttTable[i,2], ganttTable[i,3]-ganttTable[i,2])], (10*i, 10), facecolors=('red', 'yellow'))

    ax.set_ylim(-10, 75)
    ax.set_xlim(0,600)
    ax.set_xlabel('Temps')
    ax.set_yticks([0,10,20, 30,40,50,60,70])
    tasklist= ["Task"+str(x) for x in jobOrder]
    ax.set_yticklabels(tasklist)
    ax.grid(True)
    plt.show()

def _calc_makespan(jobMatrix,jobOrder,full=False):
    nb_machine, _ = jobMatrix.shape
    nb_jobs = len(jobOrder)
    ganttTable = np.zeros((nb_jobs,nb_machine*2))

    for i in range(0,nb_jobs):
        for j in range(0,nb_machine):
            ganttTable[i,2*j] = max(ganttTable[i-1,2*j+1],ganttTable[i,2*j-1])# Start of the job "i" in machine "j"
            ganttTable[i,2*j+1] = ganttTable[i,2*j] + jobMatrix[j,jobOrder[i]] # End of the job "i" in machine "j"
            
    if full==False:
        return ganttTable[-1,-1]
    return ganttTable
def Johnson(jobMatrix):
    nb_machine, nb_jobs = jobMatrix.shape
    jobMatrix = np.vstack((jobMatrix,list(range(nb_jobs))))

    jobOrder = [0] * nb_jobs
    idxJob1 = 0
    idxJob2 = nb_jobs-1

    for _ in range(nb_jobs):
        idx = jobMatrix.argmin(axis=1)

        if (jobMatrix[0,idx[0]]>=jobMatrix[1,idx[1]]):
            jobOrder[idxJob2] = int(jobMatrix[2,idx[1]])
            idxJob2 -= 1
            jobMatrix = np.delete(jobMatrix,idx[1],1)
        else:
            jobOrder[idxJob1] = int(jobMatrix[2,idx[0]])
            idxJob1 += 1
            jobMatrix = np.delete(jobMatrix,idx[0],1)
    return jobOrder

def CDS(jobMatrix):
    times=jobMatrix.T
    jobs_count = len(times)
    machine_count = len(times[0])
    
    merged_times = [[0, sum(j)] for j in times]
    perms = []
    for i in range(0, machine_count-1):
        for j in range(0, jobs_count):
            merged_times[j][0] += times[j][i]
            merged_times[j][1] -= times[j][i]
        perms.append(Johnson(np.array(merged_times).T))
        
    result = min(perms, key=lambda p: _calc_makespan(jobMatrix, np.array(p)))
    return (result, makespan(result, jobMatrix))