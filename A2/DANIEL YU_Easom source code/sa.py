import math
import random


def cost(solution):
    x1, x2 = solution
    a = (x1 - math.pi)
    b = (x2 - math.pi)

    return - math.cos(x1) * math.cos(x2) * math.exp(- a ** 2 - b ** 2)


def getNeighbor(solution, range=2):
    x, y = solution
    newX, newY = x + random.uniform(-range, range), y + \
        random.uniform(-range, range)

    while newX < -100 or newX > 100 or newY < -100 or newY > 100:
        newX, newY = x + random.uniform(-range, range), y + \
            random.uniform(-range, range)

    return (newX, newY)


def linear(temp, a):
    return temp - a


def geometric(temp, a):
    return temp * a


def slowDecrease(temp, b):
    return temp / (1 + b * temp)


def sa(initialSolution, initialTemp, annealingSchedule, annealingConst):
    solution = initialSolution
    temp = initialTemp

    while temp > (0.0001 * initialTemp):
        currCost = cost(solution)

        if currCost < -0.99:
            break

        # select a solution from the neighborhood
        nextSolution = getNeighbor(solution)
        nextCost = cost(nextSolution)
        changeInCost = nextCost - currCost

        while changeInCost >= 0 and random.random() > math.exp(- changeInCost / temp):
            nextSolution = getNeighbor(solution)
            nextCost = cost(nextSolution)
            changeInCost = nextCost - currCost

        solution = nextSolution
        temp = annealingSchedule(temp, annealingConst)

    return solution


# generate 10 random initial points
costAndPoints = []
for i in range(10):
    x = random.uniform(-100, 100)
    y = random.uniform(-100, 100)
    point = (x, y)
    costAndPoints.append((cost(point), point))

costAndPoints.sort()
_, point = costAndPoints[0]

variations = [(linear, 0.5), (linear, 1), (linear, 2),
              (geometric, 0.9), (geometric, 0.99), (geometric, 0.999),
              (slowDecrease, 0.001), (slowDecrease, 0.0005), (slowDecrease, 0.0001)]

print("initial solution: " + str(point) +
      " cost: " + str(cost(point)))

goodSolutions = []

# generate 10 random initial temps
for _ in range(10):
    temp = random.uniform(500, 1000)

    # try 3 schedule functions with 3 different alpha values
    for v in variations:
        schedule, const = v
        solution = sa(point, temp, schedule, const)

        if cost(solution) < 0:
            goodSolutions.append((cost(solution), [solution, v, temp]))

goodSolutions.sort()

for solution in goodSolutions:
    print(solution)
