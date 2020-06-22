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
#from makespan import makespan
import numpy as np



path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)

matrice = np.array(matrice)

population_size = 50
job_count = 20

# for stat
x = [x for x in range(1, 7)]

tempsNEH = []
tempsCDS = []
tempsSA = []
tempsAG = []
tempsHY = []

makespanNEH = []
makespanCDS = []
makespanSA = []
makespanAG = []
makespanHY = []

nbIterAG = []
nbIterHY = []

for nbOfJobs in [50, 50, 50]:
	for instance in [1, 2]:
		path = './data/ta{}_10_{}.txt'.format(nbOfJobs, instance)
		matrice = dataReader.read(path, 10)
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
		tempsCDS.append(end - start)
		makespanCDS.append(result[1])


		print('Algorithme NEH :')
		start = time()
		result = neh(matrice)
		end = time()
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		print('  Temps d\'execution : {:.6}s\n'.format(end - start))
		tempsNEH.append(end - start)
		makespanNEH.append(result[1])

		print('Algorithme de Recuit Simulé :')
		start = time()
		result = simulated_annealing(matrice, Ti = 790,Tf = 3 ,alpha = 0.93)
		end = time()
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		print('  Temps d\'execution : {:.6}s\n'.format(end - start))
		tempsSA.append(end - start)
		makespanSA.append(result[1])

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
		tempsAG.append(end - start)
		makespanAG.append(result[1])
		nbIterAG.append(result[2])

		print('Algorithme Hybride :')
		start = time()
		result = genetic_rt(matrice, initPop, population_size, 0.1, 200)
		print('  Ordre : {}'.format(result[0]))
		print('  Makespan : {}'.format(result[1]))
		end = time()
		print('  Temps d\'execution : {:.6}s\n'.format(end - start))
		tempsHY.append(end - start)
		makespanHY.append(result[1])
		nbIterHY.append(result[2])

'''

#CDS
plt.plot(x, makespanCDS, label='CDS')
plt.xlabel('Test')
plt.ylabel('Makespan')
plt.legend()
plt.show()

plt.plot(x, tempsCDS, label='CDS')
plt.xlabel('Test')
plt.ylabel('Temps d\'execution')
plt.legend()
plt.show()

#NEH
plt.plot(x, makespanNEH, label='NEH')
plt.xlabel('Test')
plt.ylabel('Makespan')
plt.legend()
plt.show()

plt.plot(x, tempsNEH, label='NEH')
plt.xlabel('Test')
plt.ylabel('Temps d\'execution')
plt.legend()
plt.show()


#SA
plt.plot(x, makespanSA, label='SA')
plt.xlabel('Test')
plt.ylabel('Makespan')
plt.legend()
plt.show()

plt.plot(x, tempsSA, label='SA')
plt.xlabel('Test')
plt.ylabel('Temps d\'execution')
plt.legend()
plt.show()

#AG
plt.plot(x, makespanAG, label='AG')
plt.xlabel('Test')
plt.ylabel('Makespan')
plt.legend()
plt.show()

plt.plot(x, tempsAG, label='AG')
plt.xlabel('Test')
plt.ylabel('Temps d\'execution')
plt.legend()
plt.show()

#HY
plt.plot(x, makespanHY, label='HY')
plt.xlabel('Test')
plt.ylabel('Makespan')
plt.legend()
plt.show()

plt.plot(x, tempsHY, label='HY')
plt.xlabel('Test')
plt.ylabel('Temps d\'execution')
plt.legend()
plt.show()

'''

plt.plot(x, makespanCDS, label='CDS')
plt.plot(x, makespanNEH, label='NEH')
plt.plot(x, makespanSA, label='Recuit Simulé')
plt.plot(x, makespanAG, label='AG')
plt.plot(x, makespanHY, label='HY')

plt.xlabel('Test')
plt.ylabel('Makespan')
plt.legend()
plt.show()


plt.plot(x, tempsCDS, label='CDS')
plt.plot(x, tempsNEH, label='NEH')
plt.plot(x, tempsSA, label='Recuit Simulé')
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
