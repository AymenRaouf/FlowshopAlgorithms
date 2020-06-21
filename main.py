from algorithme_genetique import genetic
from algo_genetique_recherche_locale import genetic_rt
from neh import neh
from cds import CDS
from makespan import makespan

import data as dataReader
import matplotlib.pyplot as plt
from random import shuffle, randrange, sample, random
from time import time
import numpy as np

path = './data/ta20_20.txt'

# Matrice des Jobs
matrice = dataReader.read(path, 20)

matrice = np.array(matrice)
machine_count, job_count = matrice.shape

print('Algorithme CDS :')
start = time()
result = CDS(matrice)
end = time()
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
print('  Temps d\'execution : {:.6}s'.format(end - start))


print('Algorithme NEH :')
start = time()
result = neh(matrice)
end = time()
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
print('  Temps d\'execution : {:.6}s'.format(end - start))

# Taille de la population pour les algorithmes hybrides
population_size = 50
# Generer une les individus de la population aleatoirement
initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual

print('Algorithme Hybride :')
start = time()
result = genetic_rt(matrice, initPop, population_size, 0.1, 200)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))

print('Algorithme Genetique :')
start = time()
result = genetic(matrice, initPop, population_size, 0.1, 200)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))