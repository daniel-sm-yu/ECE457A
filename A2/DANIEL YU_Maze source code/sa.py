import math
import random


def cost(solution):
    x1, x2 = solution
    a = (x1 - math.pi) * math.pi / 180
    b = (x2 - math.pi) * math.pi / 180
    return - math.cos(x1) * math.cos(x2) * math.exp(- a ** 2 - b ** 2)


def getNeighbor(solution, range=5):
    x, y = solution
    return (x + random.uniform(-range, range), y + random.uniform(-range, range))


# set curr solution to initial solution

# set curr temp to initial temp

# select a temp reduction function

# repeat
#     repeat
#         select a solution from the neighborhood
#         calculate change in cost
#         if cost is lower, accept new solition
#         else, apply prob function
#         decrease temp
#     until max iterations

# part i: generate 10 random initial points
points = []
for i in range(10):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    point = (x, y)
    points.append((cost(point), point))

points.sort()
for x in points:
    print(x)
