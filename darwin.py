from population import Population


class Darwin:

    def __init__(self, target_phrase, population_size, mutation_chance):
        self.target_phrase = target_phrase
        self.population_size = population_size
        self.mutation_chance = mutation_chance
        self.population = Population().randomise(len(target_phrase), population_size)
        self.population.set_fitnesses(target_phrase)
        self.current_fittest = self.population.get_fittest()

    def evolve(self):
        generation = 0
        while not self.current_fittest.matches_target_phrase(self.target_phrase):
            print(f'Generation: {generation}. Current fittest: {self.current_fittest.dna}')
            self.next_generation()
            generation += 1

        return {
            'individual': self.current_fittest,
            'generation': generation,
            'total_individuals': self.population_size * (generation + 1)
        }

    def next_generation(self):
        self.population = self.population.evolve_next_population(self.population_size)
        self.population.mutate(self.mutation_chance)
        self.population.set_fitnesses(self.target_phrase)
        self.current_fittest = self.population.get_fittest()
