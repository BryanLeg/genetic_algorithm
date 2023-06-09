import random
from math import sqrt
random.seed(42)

class Population:
    def __init__(self, value, nb_nodes) -> None:
        self.value = value
        self.nb_nodes = nb_nodes
        self.population = []
        self.nodes = self.create_nodes_list()

    def create_nodes_list(self) -> list:
        positions = []
        for i in range(self.nb_nodes):
            positions.append({i + 1: (random.randrange(5000), random.randrange(5000))})
        return positions

    def create_population(self, nb_paths) -> list:
        paths = []
        nodes = self.nodes
        for i in range(nb_paths):
            path = []
            random.shuffle(nodes)
            path += nodes
            path.insert(0, self.value)
            paths.append(path)
        self.population = paths
        return paths

    def get_distances(self) -> list:
        population = self.population
        distances = []
        for path in population:
            distance = 0
            temp_list = []
            for point in path:
                position = []
                for value in point.values():
                    position = value

                if len(temp_list) > 0:
                    distance += sqrt((position[0] - temp_list[0])**2 + (position[1] - temp_list[1])**2)
                temp_list = position
            distances.append(distance)
        return distances
    
    def get_shortest_path(self):
        distances = self.get_distances()
        population = self.population
        index = distances.index(distances[0])
        return population[index], distances[0]
    
    def selection(self) -> list:
        selection = []
        distances = self.get_distances()
        population = self.population
        copy_distances = distances.copy()
        copy_distances.sort()
        for i in range(0, len(self.population)//3):
            index = distances.index(copy_distances[i])
            selection.append(population[index])
        self.population = selection
        return self.population
    
    def crossbreeding(self) -> list:
        crossbreeding = []
        population = self.population
        
        def takes_half(path):
            half_path = []
            for i in range(0, len(path) //2):
                half_path.append(path[i])
            return half_path

        for _ in range(2):
            new_path = []
            for path in population:
                if population.index(path) != 0:
                    indexes = [x for x in range(0, len(population))]
                    indexes.remove(population.index(path))
                    first_parent = takes_half(path)
                    second_parent = population[random.choice(indexes)]
                    for i in range(len(path)):
                        if second_parent[i] not in first_parent:
                            first_parent.append(second_parent[i])
                    new_path.append(first_parent) 
                else:
                    new_path.append(path)
            crossbreeding += new_path
        self.population += crossbreeding
        return self.population
    
    def mutation(self, mutation_probability) -> list:
        population = self.population
        for path in population:
            if population.index(path) != 0:
                indexes = [x for x in range(1, 5)]
                if random.randint(0, 100) <= mutation_probability:
                    index_1 = random.choice(indexes)
                    indexes.remove(index_1)
                    index_2 = random.choice(indexes)
                    path[index_1], path[index_2] = path[index_2], path[index_1]
        return population

    def evolution(self, mutation_probability, nb_cycle):
        if nb_cycle > 0:
            self.selection()
            self.crossbreeding()
            self.mutation(mutation_probability)
            self.evolution(mutation_probability, nb_cycle - 1)
        return self.get_shortest_path()
            


root = Population({0: (0, 0)}, 5)
root.create_population(1000)
print(root.evolution(5, 100))
