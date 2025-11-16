import random
import string


TARGET = "GENETICS"
POPULATION_SIZE = 200
MUTATION_RATE = 0.02
VALID_CHARS = string.ascii_uppercase + ' '
TAERGET_LEN =  len(TARGET)

def generate_individual():
    return ''.join(random.choice(VALID_CHARS) for _ in range(TAERGET_LEN))

def caculate_fitness(individual):
    score = 0
    for i in range(TAERGET_LEN):
        if individual[i] == TARGET[i]:
            score += 1
    return score

def selection(population, fitnesses):
    
    total_fitness = sum(fitnesses)

    if total_fitness == 0:
        return random.choice(population), random.choice(population)
    
    probabilities = [f / total_fitness for f in fitnesses]

    parent1 = random.choice(population, weights = probabilities, k=1)[0]
    parent2 = random.choice(population, weights = probabilities, k=1)[0]

    return parent1, parent2

