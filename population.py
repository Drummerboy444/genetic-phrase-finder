import random

from individual import Individual


class Population:

    def __init__(self, individuals=None):
        self.individuals = individuals

    def randomise(self, phrase_length, population_size):
        self.individuals = [Individual().randomise(phrase_length) for _ in range(population_size)]
        return self

    def set_fitnesses(self, target_phrase):
        for individual in self.individuals:
            individual.set_fitness(target_phrase)

    def get_fittest(self):
        fittest = None
        best_fitness = -1
        for individual in self.individuals:
            if individual.fitness > best_fitness:
                best_fitness = individual.fitness
                fittest = individual
        return fittest

    def evolve_next_population(self, population_size):
        gene_pool = self.create_gene_pool()
        new_individuals = []
        for _ in range(population_size):
            parents = random.sample(gene_pool, 2)
            new_individuals.append(parents[0].reproduce(parents[1]))
        return Population(new_individuals)

    def create_gene_pool(self):
        pool = []
        for individual in self.individuals:
            pool.extend([individual] * individual.fitness)
        return pool

    def mutate(self, chance):
        for individual in self.individuals:
            if random.random() < chance:
                individual.mutate()
