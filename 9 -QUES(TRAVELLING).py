import itertools
import math
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)
def tsp_brute_force(cities):
    num_cities = len(cities)
    min_distance = float('inf')
    optimal_tour = None
    for tour in itertools.permutations(range(num_cities)):
        tour_distance = 0
        for i in range(num_cities - 1):
            city1 = cities[tour[i]]
            city2 = cities[tour[i + 1]]
            tour_distance += distance(city1, city2)
        # Add distance from last city back to first city
        tour_distance += distance(cities[tour[-1]], cities[tour[0]])
        if tour_distance < min_distance:
            min_distance = tour_distance
            optimal_tour = tour
    return optimal_tour, min_distance
cities = [
    (0, 0),  # City 0
    (10, 0),  # City 1
    (5, 5),  # City 2
    (0, 10),  # City 3
    (10, 10)  # City 4
]
optimal_tour, min_distance = tsp_brute_force(cities)
print("Optimal Tour:", optimal_tour)
print("Total Distance:", min_distance)