import math
import random


def cost(solution):
    x1, x2 = solution
    a = (x1 - math.pi) ** 2
    b = (x2 - math.pi) ** 2
    return - math.cos(x1) * math.cos(x2) * math.exp(- a - b)


def getNeighbor(solution, range=5):
    x, y = solution
    return (x + random.randint(-range, range), y + random.randint(-range, range))


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

# print(cost((3, 2)))

# grid = [[0 for _ in range(50)] for _ in range(50)]

# for i in range(900):
#     x, y = getNeighbor((15, 15))
#     grid[x][y] = 1

# grid[15][15] = 8

# for row in grid:
#     print(row)
