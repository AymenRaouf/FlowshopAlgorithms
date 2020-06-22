import numpy as np
import matplotlib.pyplot as plt

import data as dataReader
from makespan import makespan


def plotGantt(jobMatrix,jobOrder,nom,nb=7):
    fig, ax = plt.subplots()

    nb_machine, nb_jobs = jobMatrix.shape
    ganttTable = _calc_makespan(jobMatrix,jobOrder,True)

    colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000',"#ff0000", "#7f0000", "#400000", "#ff8080", "#7f4040", "#403030", "#bf8f00", "#7f7040", "#7fff00", "#508020", "#dfffbf", "#10401c", "#7fff9f", "#208080", "#80ffff", "#204040", "#002080", "#101c40", "#809fff", "#bfcfff", "#9f40ff", "#604080", "#dfbfff", "#383040", "#400030", "#bf309b", "#806078"]
    for i in range(nb_jobs):
        ax.broken_barh([(ganttTable[i,2*j], ganttTable[i,2*j+1]-ganttTable[i,2*j]) for j in range(nb_machine)], (10*i, 10),facecolors=colors[:nb_machine])
    
    ax.set_xlabel('Temps')
    ax.set_yticks([i*10 for i in range(nb)])
    tasklist= ["Task"+str(x) for x in jobOrder]
    ax.set_yticklabels(tasklist)
    ax.grid(True)
    plt.title('Makespan = {}'.format(makespan(jobOrder, jobMatrix)))
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