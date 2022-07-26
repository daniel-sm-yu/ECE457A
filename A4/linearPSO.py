import random
import matplotlib.pyplot as plt


def cost(xAndY):
    x, y = xAndY
    return 4 * x**2 - 2.1 * x**4 + (x**6)/3 + x*y - 4 * y**2 + 4 * y**4


def particleCost(particle):
    x = particle.x
    y = particle.y
    return 4 * x**2 - 2.1 * x**4 + (x**6)/3 + x*y - 4 * y**2 + 4 * y**4


class Particle:
    def __init__(self):
        self.x = random.uniform(-5, 5)
        self.y = random.uniform(-5, 5)
        self.x_velocity = random.uniform(-0.5, 0.5)
        self.y_velocity = random.uniform(-0.5, 0.5)
        self.personal_best = (self.x, self.y)


def linearPSO(max_iterations, population_size, w, c):  # c = c1 = c2
    swarm = [Particle() for _ in range(population_size)]
    global_best = (swarm[0].x, swarm[0].y)
    avg_fitnesses = []
    best_fitnesses = []

    for _ in range(max_iterations):
        sum_fitness = 0

        for particle in swarm:
            curr_cost = particleCost(particle)
            sum_fitness += curr_cost

            # update personal best
            if curr_cost < cost(particle.personal_best):
                particle.personal_best = (particle.x, particle.y)

            # update global best
            if curr_cost < cost(global_best):
                global_best = (particle.x, particle.y)

            # calculate velocity
            x_personal_best, y_personal_best = particle.personal_best
            x_global_best, y_global_best = global_best

            # generate r values
            r1 = random.random()
            r2 = random.random()

            # x velocity
            x_personal_term = c * r1 * (x_personal_best - particle.x)
            x_global_term = c * r2 * (x_global_best - particle.x)
            particle.x_velocity = w * particle.x_velocity + x_personal_term * x_global_term

            # y velocity
            y_personal_term = c * r1 * (y_personal_best - particle.y)
            y_global_term = c * r2 * (y_global_best - particle.y)
            particle.y_velocity = w * particle.y_velocity + y_personal_term * y_global_term

            # calculate position
            particle.x += particle.x_velocity
            particle.y += particle.y_velocity

            # ensure position is within range
            particle.x = max(-5, particle.x)
            particle.x = min(5, particle.x)

            particle.y = max(-5, particle.y)
            particle.y = min(5, particle.y)

        avg_fitness = sum_fitness / population_size
        avg_fitnesses.append(avg_fitness)
        best_fitnesses.append(cost(global_best))

    print(avg_fitnesses)
    print(best_fitnesses)

    plt.plot(avg_fitnesses)
    plt.title('linear PSO average fitness')
    plt.ylabel('average fitness')
    plt.xlabel('iteration')
    plt.show()

    plt.plot(best_fitnesses)
    plt.title('linear PSO best fitness')
    plt.ylabel('best fitness')
    plt.xlabel('iteration')
    plt.show()


w = 0.792
c = 1.4944
linearPSO(50, 25, w, c)
