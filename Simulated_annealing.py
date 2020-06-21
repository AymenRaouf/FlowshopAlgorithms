import data as dataReader
from random import randint
from makespan import makespan
import time
import numpy as np
from neh import neh
import sys


#population_size = 100
#job_count = 20
#nb_machines = len(matrice[0])


def simulated_annealing(matrice, Ti = 790,Tf = 3 ,alpha = 0.93):
    #Number of jobs given
    nb_machines, job_count = matrice.shape
    n = job_count;

    default_timer = None
    if sys.platform == "win32":
        default_timer = time.time()
    else:
        default_timer = time.time()

    s = default_timer
    #Initialize the primary seq
    old_seq = neh(matrice)
    old_seq = old_seq[0]
    old_makeSpan = makespan(old_seq,matrice)
    #print("old sequence: ",old_seq)
    #print("old makespan: ",old_makeSpan)
    new_seq = []       
    delta_mk1 = 0
    #Initialize the temperature
    T = Ti
    Tf = Tf
    alpha = alpha
    # of iterations
    temp_cycle = 0
    while T >= Tf  :
        new_seq = old_seq.copy()
        job = new_seq.pop(randint(0,n-1))
        new_seq.insert(randint(0,n-1),job)
        new_make_span = makespan(new_seq,matrice)
        delta_mk1 = new_make_span - old_makeSpan
        if delta_mk1 <= 0:
            old_seq = new_seq
            old_makeSpan = new_make_span
        else :
            Aprob = np.exp(-(delta_mk1/T))
            if Aprob > np.random.uniform(0.5,0.9):
                old_seq = new_seq
                old_makeSpan = new_make_span
            else :
                #The solution is discarded
                pass
        T = T * alpha 
        temp_cycle += 1

    e = default_timer
    #Result Sequence
    seq = old_seq
    schedules = np.zeros((nb_machines, job_count), dtype=dict)
    # schedule first job alone first
    task = {"name": "job_{}".format(
        seq[0] + 1), "start_time": 0, "end_time": matrice[0][seq[0]]}
    schedules[0][0] = task
    for m_id in range(1, nb_machines):
        start_t = schedules[m_id - 1][0]["end_time"]
        end_t = start_t + matrice[m_id][0]
        task = {"name": "job_{}".format(
            seq[0] + 1), "start_time": start_t, "end_time": end_t}
        schedules[m_id][0] = task

    for index, job_id in enumerate(seq[1::]):
        start_t = schedules[0][index]["end_time"]
        end_t = start_t + matrice[0][job_id]
        task = {"name": "job_{}".format(
            job_id + 1), "start_time": start_t, "end_time": end_t}
        schedules[0][index + 1] = task
        for m_id in range(1, nb_machines):
            start_t = max(schedules[m_id][index]["end_time"],
                            schedules[m_id - 1][index + 1]["end_time"])
            end_t = start_t +matrice[m_id][job_id]
            task = {"name": "job_{}".format(
                job_id + 1), "start_time": start_t, "end_time": end_t}
            schedules[m_id][index + 1] = task
    t_t = e - s

    return seq, old_makeSpan

'''
if __name__ == '__main__':
    path = './data/ta20_20.txt'
    matrice = dataReader.read(path, 20)
    seq, makespan = simulated_annealing(matrice, Ti = 790,Tf = 3 ,alpha = 0.93)
    print(seq)
    #print(schedules)
    print(makespan)
    #print('new sequence :',seq,"\nNew_makespane",new_makeSpan,"\ntemps_Total : ",t_t)
'''