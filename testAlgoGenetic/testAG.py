from algorithme_genetique import genetic
from algo_genetique_recherche_locale import genetic_rt
from neh import neh
import data as dataReader
import matplotlib.pyplot as plt
from random import shuffle, randrange, sample, random
from time import time
from makespan import makespan
import numpy as np

def varier_taille_population():
	x = []
	tempsPop30 = []
	tempsPop50 = []
	tempsPop80 = []
	tempsPop100 = []

	makesPop30 = []
	makesPop50 = []
	makesPop80 = []
	makesPop100 = []

	nbIterPop30 = []
	nbIterPop50 = []
	nbIterPop80 = []
	nbIterPop100 = []

	for _ in range(1, 9):
		x.append(_)
		path = './data/ta20_20_{}.txt'.format(_)
		matrice = dataReader.read(path, 20)
		matrice = np.array(matrice)

		#job_count = 20
		machine_count, job_count = matrice.shape
		print('iteration : {}'.format(_))
		print('{}:{}'.format(machine_count, job_count))
		#initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual

		# POP30
		population_size = 30
		initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual
		start = time()
		result = genetic(matrice, initPop, population_size, 0.1, 200, limit=0)
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		end = time()
		print('  Temps d\'execution : {:.6}s'.format(end - start))
		tempsPop30.append(end - start)
		makesPop30.append(result[1])
		nbIterPop30.append(result[2])
		print()

		# POP50
		population_size = 50
		initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual
		start = time()
		result = genetic(matrice, initPop, population_size, 0.1, 200, limit=0)
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		end = time()
		print('  Temps d\'execution : {:.6}s'.format(end - start))
		tempsPop50.append(end - start)
		makesPop50.append(result[1])
		nbIterPop50.append(result[2])
		print()

		# POP80
		population_size = 80
		initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual
		start = time()
		result = genetic(matrice, initPop, population_size, 0.1, 200, limit=0)
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		end = time()
		print('  Temps d\'execution : {:.6}s'.format(end - start))
		tempsPop80.append(end - start)
		makesPop80.append(result[1])
		nbIterPop80.append(result[2])
		print()

		# POP100
		population_size = 100
		initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual
		start = time()
		result = genetic(matrice, initPop, population_size, 0.1, 200, limit=0)
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		end = time()
		print('  Temps d\'execution : {:.6}s'.format(end - start))
		tempsPop100.append(end - start)
		makesPop100.append(result[1])
		nbIterPop100.append(result[2])
		print()

	plt.plot(x, makesPop30, label='30')
	plt.plot(x, makesPop50, label='50')
	plt.plot(x, makesPop80, label='80')
	plt.plot(x, makesPop100, label='100')
	plt.xlabel('Test')
	plt.ylabel('Makespan')
	plt.legend()
	plt.show()

	plt.plot(x, tempsPop30, label='30')
	plt.plot(x, tempsPop50, label='50')
	plt.plot(x, tempsPop80, label='80')
	plt.plot(x, tempsPop100, label='100')
	plt.xlabel('Test')
	plt.ylabel('Temps d\'execution')
	plt.legend()
	plt.show()

	plt.plot(x, nbIterPop30, label='30')
	plt.plot(x, nbIterPop50, label='50')
	plt.plot(x, nbIterPop80, label='80')
	plt.plot(x, nbIterPop100, label='100')
	plt.xlabel('Test')
	plt.ylabel('Nombre d\'iterations')
	plt.legend()
	plt.show()

varier_taille_population()