import random
random.seed(42)

class Population:
    def __init__(self, value) -> None:
        self.value = value
        self.population = []

    def create_population(self, nb_nodes):
        positions = []
        for i in range(nb_nodes):
            positions.append({i +1: (random.randrange(5000), random.randrange(5000))})
        random.shuffle(positions)
        return positions


root = Population({0, (0, 0)})
print(root.create_population(4))

