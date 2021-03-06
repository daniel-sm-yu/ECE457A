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


def simplePSO(max_iterations, population_size, w, c):  # c = c1 = c2
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
            x_r1 = random.random()
            y_r1 = random.random()
            x_r2 = random.random()
            y_r2 = random.random()

            # x velocity
            x_personal_term = c * x_r1 * (x_personal_best - particle.x)
            x_global_term = c * x_r2 * (x_global_best - particle.x)
            particle.x_velocity = w * particle.x_velocity + x_personal_term + x_global_term

            # y velocity
            y_personal_term = c * y_r1 * (y_personal_best - particle.y)
            y_global_term = c * y_r2 * (y_global_best - particle.y)
            particle.y_velocity = w * particle.y_velocity + y_personal_term + y_global_term

            # ensure velocity is within speed limit
            particle.x_velocity = max(-4, particle.x_velocity)
            particle.x_velocity = min(4, particle.x_velocity)

            particle.y_velocity = max(-4, particle.y_velocity)
            particle.y_velocity = min(4, particle.y_velocity)

            print(particle.x_velocity)
            print(particle.y_velocity)

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

    print(best_fitnesses[-1])
    print(global_best)

    plt.plot(avg_fitnesses)
    plt.title('simple PSO average fitness')
    plt.ylabel('average fitness')
    plt.xlabel('iteration')
    plt.show()

    plt.plot(best_fitnesses)
    plt.title('simple PSO best fitness')
    plt.ylabel('best fitness')
    plt.xlabel('iteration')
    plt.show()


w = 0.792
c = 1.4944
simplePSO(50, 10, w, c)
