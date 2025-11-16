import random
import string


TARGET = "BANGLADESH"
POPULATION_SIZE = 200
MUTATION_RATE = 0.02
VALID_CHARS = string.ascii_uppercase + ' '
TARGET_LEN =  len(TARGET)

def generate_individual():
    return ''.join(random.choice(VALID_CHARS) for _ in range(TARGET_LEN))

def calculate_fitness(individual):
    score = 0
    for i in range(TARGET_LEN):
        if individual[i] == TARGET[i]:
            score += 1
    return score

def selection(population, fitnesses):
    
    total_fitness = sum(fitnesses)

    if total_fitness == 0:
        return random.choice(population), random.choice(population)
    
    probabilities = [f / total_fitness for f in fitnesses]

    parent1 = random.choices(population, weights = probabilities, k=1)[0]
    parent2 = random.choices(population, weights = probabilities, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    split_point = random.randint(1, TARGET_LEN - 1)

    offspring1 = parent1[:split_point] + parent2[split_point:]
    offspring2 = parent2[:split_point] + parent1[split_point:]

    return offspring1, offspring2

def mutation(individual):
   mutated_list = list(individual) 
   for i in range(TARGET_LEN):
       if random.random() < MUTATION_RATE:
           mutated_list[i] = random.choice(VALID_CHARS)
   return "".join(mutated_list)


def genetic_algorithm():

    population = [generate_individual() for _ in range(POPULATION_SIZE)]
    generation = 0

    print(f"Target: **{TARGET}** (Length: {TARGET_LEN})")
    print(f"Population Size: {POPULATION_SIZE}, Mutation Rate: {MUTATION_RATE}")
    print("-" * 30)

    while True:
        fitnesses = [calculate_fitness(individual) for individual in population]
        best_individual = max(zip(population, fitnesses), key = lambda x: x[1])

        current_best_string = best_individual[0]
        max_fitness = best_individual[1]

        # Display progress every 10 generations
        if generation % 10 == 0 or max_fitness == TARGET_LEN:
             print(f"Gen {generation}: Best String = '{current_best_string}', Fitness = {max_fitness}/{TARGET_LEN}")

        if max_fitness == TARGET_LEN:
            print("-" * 30)
            print(f"🎉 **Success!** Target found in Generation {generation}.")
            print(f"Final String: '{current_best_string}'")
            break

        # 4. Create New Population (Next Generation)
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            # 5. Selection
            parent1, parent2 = selection(population, fitnesses)
            
            # 6. Crossover
            offspring1, offspring2 = crossover(parent1, parent2)
            
            # 7. Mutation
            offspring1 = mutation(offspring1)
            offspring2 = mutation(offspring2)
            
            new_population.extend([offspring1, offspring2])
        
        # Update population and generation count
        population = new_population
        generation += 1
        
        # Safety break for extremely long runs
        if generation > 5000:
            print("\nStopped after 5000 generations without perfect match.")
            break

genetic_algorithm()