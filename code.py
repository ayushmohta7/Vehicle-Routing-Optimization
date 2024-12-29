import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Define the problem parameters
num_locations = 20  # Number of locations (excluding the depot)
locations = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_locations)]  # Randomly generate coordinates for locations
depot = (50, 50)  # Coordinates of the depot
num_vehicles = 3  # Number of vehicles available

# Define the fitness structure (minimize distance and balance penalty)
creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
creator.create("Individual", list, fitness=creator.FitnessMin)

# Set up the genetic algorithm components
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(num_locations), num_locations)  # Generate a random permutation of locations
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)  # Create an individual as a permutation of locations
toolbox.register("population", tools.initRepeat, list, toolbox.individual)  # Create a population of individuals

# Define the fitness evaluation function
def evalVRP(individual):
    total_distance = 0
    distances = []  # List to track the distance traveled by each vehicle

    # Divide the route among the vehicles and calculate the distances
    for i in range(num_vehicles):
        vehicle_route = [depot] + [locations[individual[j]] for j in range(i, len(individual), num_vehicles)] + [depot]
        vehicle_distance = sum(np.linalg.norm(np.array(vehicle_route[k + 1]) - np.array(vehicle_route[k])) for k in range(len(vehicle_route) - 1))
        total_distance += vehicle_distance
        distances.append(vehicle_distance)

    balance_penalty = np.std(distances)  # Standard deviation of distances as a balance penalty
    return total_distance, balance_penalty

# Register the genetic algorithm operators
toolbox.register("evaluate", evalVRP)  # Register the evaluation function
toolbox.register("mate", tools.cxPartialyMatched)  # Crossover for permutation representation
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)  # Mutation by shuffling indices
toolbox.register("select", tools.selTournament, tournsize=3)  # Tournament selection

# Function to visualize the routes
def plot_routes(individual, title="Routes"):
    plt.figure()
    for (x, y) in locations:
        plt.plot(x, y, 'bo')  # Plot locations as blue dots
    plt.plot(depot[0], depot[1], 'rs')  # Plot the depot as a red square

    for i in range(num_vehicles):
        vehicle_route = [depot] + [locations[individual[j]] for j in range(i, len(individual), num_vehicles)] + [depot]
        plt.plot(*zip(*vehicle_route), '-')  # Plot the route for each vehicle

    plt.title(title)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()

# Main function to run the genetic algorithm
def main():
    random.seed(42)  # Set seed for reproducibility
    pop = toolbox.population(n=300)  # Create an initial population
    hof = tools.HallOfFame(1)  # Store the best solution found

    # Set up statistics tracking
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)  # Track the average fitness
    stats.register("min", np.min)  # Track the minimum fitness

    # Run the genetic algorithm
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 300, stats=stats, halloffame=hof)

    # Visualize the best solution found
    plot_routes(hof[0], "Optimal Route")
    return pop, stats, hof

if __name__ == "__main__":
    main()
