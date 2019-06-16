import random

from characters import CHARACTERS


class Individual:

    def __init__(self, dna=None):
        self.dna = dna
        self.fitness = None

    def randomise(self, length):
        self.dna = ''.join(random.choices(CHARACTERS, k=length))
        return self

    def set_fitness(self, target_phrase):
        fitness = 1
        for c1, c2 in zip(self.dna, target_phrase):
            if c1 is c2:
                fitness += 1
        self.fitness = fitness

    def matches_target_phrase(self, target_phrase):
        return self.dna == target_phrase

    def reproduce(self, other):
        dna = ''
        for c1, c2 in zip(self.dna, other.dna):
            dna += random.choice([c1, c2])
        return Individual(dna)

    def mutate(self):
        i = random.choice(range(len(self.dna)))
        list_dna = list(self.dna)
        list_dna[i] = random.choice(CHARACTERS)
        self.dna = ''.join(list_dna)
