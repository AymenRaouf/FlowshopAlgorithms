import numpy as np

def makespan(jobOrder, jobMatrix):
	nb_machine, _ = jobMatrix.shape
	nb_jobs = len(jobOrder)
	ganttTable = np.zeros((nb_jobs,nb_machine*2))
	for i in range(0,nb_jobs):
		for j in range(0,nb_machine):
			ganttTable[i,2*j] = max(ganttTable[i-1,2*j+1],ganttTable[i,2*j-1])# Start of the job "i" in machine "j"
			ganttTable[i,2*j+1] = ganttTable[i,2*j] + jobMatrix[j,jobOrder[i]] # End of the job "i" in machine "j"            
	return int(ganttTable[-1,-1])
'''
def makespan(jobOrder, jobMatrix):
    job_count = len(jobOrder)
    machine_count = len(jobMatrix)
    
    makespan = [[0] * (machine_count + 1) for _ in range(0, job_count + 1)]
    for i, job in enumerate(jobOrder):
        for machine in range(0, machine_count):
            makespan[i + 1][machine + 1] = max(makespan[i][machine + 1], makespan[i + 1][machine]) + data[machine][job - 1]
    
    return makespan[job_count][machine_count]

'''