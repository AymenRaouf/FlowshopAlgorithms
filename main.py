from algorithme_genetique import genetic
from algo_genetique_recherche_locale import genetic_rt
from neh import neh
from cds import CDS
from Simulated_annealing import simulated_annealing
from makespan import makespan

import data as dataReader
import matplotlib.pyplot as plt
from random import shuffle, randrange, sample, random
from time import time
import numpy as np

#path = './data/ta20_20.txt'
path = './data/ta100_10_1.txt'
pathList = [
	'./data/ta20_5_1.txt',
	'./data/ta20_20_1.txt',
	'./data/ta100_10_1.txt',
]
for path in pathList:
	if path == './data/ta20_5_1.txt':
		nbLignes = 5
	elif path == './data/ta20_20_1.txt':
		nbLignes = 20
	elif path == './data/ta100_10_1.txt':
		nbLignes = 10
	# Matrice des Jobs
	matrice = dataReader.read(path, nbLignes)

	matrice = np.array(matrice)
	machine_count, job_count = matrice.shape
	print('{} machines et {} jobs'.format(machine_count, job_count))

	print('Algorithme CDS :')
	start = time()
	result = CDS(matrice)
	end = time()
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	print('  Temps d\'execution : {:.6}s\n'.format(end - start))


	print('Algorithme NEH :')
	start = time()
	result = neh(matrice)
	end = time()
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	print('  Temps d\'execution : {:.6}s\n'.format(end - start))

	print('Algorithme de Recuit Simulé :')
	start = time()
	result = simulated_annealing(matrice, Ti = 790,Tf = 3 ,alpha = 0.93)
	end = time()
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	print('  Temps d\'execution : {:.6}s\n'.format(end - start))

	# Taille de la population pour les algorithmes hybrides
	population_size = 50
	# Generer une les individus de la population aleatoirement
	initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual

	print('Algorithme Genetique :')
	start = time()
	result = genetic(matrice, initPop, population_size, 0.1, 200)
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	end = time()
	print('  Temps d\'execution : {:.6}s\n\n'.format(end - start))

	print('Algorithme Hybride :')
	start = time()
	result = genetic_rt(matrice, initPop, population_size, 0.1, 200)
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	end = time()
	print('  Temps d\'execution : {:.6}s\n'.format(end - start))

	input()