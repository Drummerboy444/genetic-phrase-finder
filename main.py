from darwin import Darwin


population_size = 100
mutation_chance = 0.1
target_phrase = 'Hello World!'

darwin = Darwin(target_phrase, population_size, mutation_chance)
answer_data = darwin.evolve()

print()
print(f"Answer: \"{answer_data['individual'].dna}\"")
print(f"Generation: {answer_data['generation']}")
print(f"Total individuals: {answer_data['total_individuals']}")
