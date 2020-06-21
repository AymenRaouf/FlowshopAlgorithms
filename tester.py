from algorithme_genetique import genetic
from algo_genetique_recherche_locale import genetic_rt
from neh import neh
import data as dataReader
import matplotlib.pyplot as plt
from random import shuffle, randrange, sample, random
from time import time
from makespan import makespan
import numpy as np

path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)

matrice = np.array(matrice)

population_size = 50
job_count = 20

# for stat
x = [x for x in range(1, 6)]
tempsAG = []
tempsHY = []
makespanAG = []
makespanHY = []
nbIterAG = []
nbIterHY = []

for _ in range(1):

	print('Algorithme NEH :')
	start = time()
	result = neh(matrice)
	end = time()
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	print('  Temps d\'execution : {:.6}s'.format(end - start))

	# Generer une les individus de la population aleatoirement
	#initPop = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual
	initPop = [sample(list(range(0, job_count)), job_count) for _ in range(0, population_size)] # same repeated individual

	print('Algorithme Hybride :')
	start = time()
	#result = genetic(matrice, initPop, 100, 0.1, 200, limit=2400)
	result = genetic_rt(matrice, initPop, population_size, 0.1, 200, limit=2400)
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	end = time()
	print('  Temps d\'execution : {:.6}s'.format(end - start))

	tempsHY.append(end - start)
	makespanHY.append(result[1])
	nbIterHY.append(result[2])

	print('Algorithme Genetique :')
	start = time()
	result = genetic(matrice, initPop, population_size, 0.1, 200, limit=2400)
	print('  Ordre : {}'.format(result[0]))
	print('  Makespan : {}'.format(result[1]))
	end = time()
	print('  Temps d\'execution : {:.6}s'.format(end - start))
	tempsAG.append(end - start)
	makespanAG.append(result[1])
	nbIterAG.append(result[2])
	print()


plt.plot(x, makespanAG, label='AG')
plt.plot(x, makespanHY, label='HY')
plt.xlabel('Test')
plt.ylabel('Makespan')
plt.legend()
plt.show()


plt.plot(x, tempsAG, label='AG')
plt.plot(x, tempsHY, label='HY')
plt.xlabel('Test')
plt.ylabel('Temps d\'execution')
plt.legend()
plt.show()

plt.plot(x, nbIterAG, label='AG')
plt.plot(x, nbIterHY, label='HY')
plt.xlabel('Test')
plt.ylabel('Nombre d\'iterations')
plt.legend()
plt.show()
