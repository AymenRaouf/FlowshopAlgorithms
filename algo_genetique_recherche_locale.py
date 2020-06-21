from random import shuffle, randrange, sample, random
from time import time
from makespan import makespan
import data as dataReader
import matplotlib.pyplot as plt


def genetic_rt(data, populationInitiale, taille_population = 100, taux_mut = 0.1, maxIterations = 1000, limit = 0):
    population_size = taille_population
    taux_mutation = taux_mut
    job_count = len(data[0])
    #print('jobs = {}   machines = {} '.format(job_count, len(data)))
    population_avec_qualite = evaluer_qualite(populationInitiale, data)


    score = 9999999
    iteration = 0

    repetitionSolution = 0
    individuRepete = []
    while repetitionSolution <= 10 and iteration < maxIterations:
        iteration += 1

        parents = choisir_parents(population_avec_qualite)

        enfants = croisement(parents)

        mutation_rt(enfants, taux_mutation, data)


        population_avec_qualite = union(population_avec_qualite, evaluer_qualite(enfants, data))
        meilleurIndividu = choisir_meilleur(population_avec_qualite)

        if meilleurIndividu[1] < score:
            score = meilleurIndividu[1]
            #print('new : {} makespan = {}'.format(meilleurIndividu[0], meilleurIndividu[1]))
        if meilleurIndividu[0] == individuRepete:
            repetitionSolution += 1
        else:
            repetitionSolution = 0
            individuRepete = meilleurIndividu[0]

    return (meilleurIndividu[0], meilleurIndividu[1], iteration)

def evaluer_qualite(population, data):
    return [(individual, makespan(individual, data)) for individual in population]

def choisir_parents(population):
    parents = []
    for _ in range(0, len(population)):
        # Prendre un echantillon aleatoire
        echantillon = sample(population, 5)
        parents.append(choisir_meilleur(echantillon))
    return parents

def croisement(parents):
    shuffle(parents)
    enfants = []
    for i in range(1, len(parents), 2):
        enfants += merge(parents[i - 1][0], parents[i][0])
    return enfants

def mutation_rt(enfants, taux_mutation, data):
    for i in range(len(enfants)):
        enfant = enfants[i]
        if random() <= taux_mutation:
            enfants[i] = amelioration_locale(enfant, data)
            '''
            left = randrange(0, len(enfant))
            right = randrange(left, len(enfant))
           
            tmp = enfant[left]
            enfant[left] = enfant[right]
            enfant[right] = tmp
            enfants[i] = enfant
            '''
        #else:
            #enfants[i] = amelioration_locale(enfant, data)

def amelioration_locale(individu, data):
    qualite_initiale = makespan(individu, data)
    voisins = []
    for _ in range(5):
        voisin = swap(individu)
        voisins.append((voisin, makespan(voisin, data)))

    meilleurVoisin = choisir_meilleur(voisins)
    
    if(meilleurVoisin[1] < qualite_initiale):
        individu = meilleurVoisin[0]
    return individu


def swap(individu):
    resultat = individu[:]
    i = randrange(len(individu))
    j = randrange(len(individu))
    tmp = resultat[i]
    resultat[i] = resultat[j]
    resultat[j] = tmp
    return resultat



def union(parents, enfants):
    both = parents + enfants
    both.sort(key=lambda x: x[1])
    return both[:len(parents)]

def choisir_meilleur(population):
    return min(population, key=lambda x: x[1])

def translate(x, d):
    while x in d and x != d[x]:
        x = d[x]
    return x

def merge(a, b):
    length = len(a)
    left = randrange(0, length + 1)
    right = randrange(left, length + 1)
    
    a2 = a[left:right]
    b2 = b[left:right]
    d = dict(zip(a2, b2))
    d_inv = dict(zip(b2, a2))
   
    enfant1 = list(map(lambda x: translate(x, d_inv), a[0:left])) + b2 + list(map(lambda x: translate(x, d_inv), a[right:length + 1]))
    enfant2 = list(map(lambda x: translate(x, d), b[0:left])) + a2 + list(map(lambda x: translate(x, d), b[right:length + 1]))
    
    return [enfant1, enfant2]

'''
path = './data/ta20_20.txt'
matrice = dataReader.read(path, 20)

population_size = 100
job_count = 20

# Generer une les individus de la population aleatoirement
initPop = [sample(list(range(1, job_count + 1)), job_count) for _ in range(0, population_size)] # same repeated individual


start = time()
#result = genetic(matrice, initPop, 100, 0.1, 200, limit=2400)
result = genetic_rt(matrice, initPop, 100, 0.1, 200, limit=2400)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))
'''
'''
print('Generation,Makespan')
for i in range(len(x)):
    print('{},{}'.format(x[i], y[i]))
plt.plot(x,y)
plt.xlabel('Generation')
plt.ylabel('Makespan')
plt.show()
'''
'''


start = time()
result = genetic(matrice, initPop, 100, 0.1, 200, limit=2400)
print('  Ordre : {}'.format(result[0]))
print('  Makespan : {}'.format(result[1]))
end = time()
print('  Temps d\'execution : {:.6}s'.format(end - start))
'''