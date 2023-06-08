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

    def selection(self) -> list:
        population = self.population
        distances = []
        selection = []
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
        copy_distances = distances.copy()
        copy_distances.sort()
        for i in range(0, len(self.population)//3):
            index = distances.index(copy_distances[i])
            selection.append(population[index])
        self.population = selection
    
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
                indexes = [x for x in range(0, len(population))]
                indexes.remove(population.index(path))
                first_parent = takes_half(path)
                second_parent = population[random.choice(indexes)]
                for i in range(len(path)):
                    if second_parent[i] not in first_parent:
                        first_parent.append(second_parent[i])
                new_path.append(first_parent) 
            crossbreeding += new_path
        
        self.population.append(crossbreeding)
    
root = Population({0: (0, 0)}, 4)
root.create_population(10)
print(root.population)
root.selection()
print(root.population)
root.crossbreeding()
print(root.population)
