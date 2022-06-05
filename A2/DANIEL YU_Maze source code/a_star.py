
# A* Search

from copy import deepcopy
from maze import *
import heapq

m = len(maze)
n = len(maze[0])
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def a_star(start, end):
    # queue of tuples of heuristic and path
    openList = [(distance(start, end), [start])]
    closedList = []

    while openList:
        _, path = heapq.heappop(openList)
        node = path[-1]
        i, j = node

        # check for i and j out of bounds, node is wall, and previously visited
        if i < 0 or i >= m or j < 0 or j >= n or maze[i][j] or node in closedList:
            continue

        if node == end:
            print("path: " + str(path))
            print("cost: " + str(len(path)))
            print("number of explored nodes: " + str(len(closedList)))

            mazeCopy = deepcopy(maze)
            step = 2
            for a, b in path:
                mazeCopy[a][b] = step
                step += 1
            printMaze(mazeCopy)

            return

        closedList.append(node)

        for x, y in directions:
            nextNode = (i + x, j + y)
            heapq.heappush(
                openList, (distance(nextNode, end), path + [nextNode])
            )


print("S to E1:")
a_star((11, 2), (19, 23))
print("S to E2:")
a_star((11, 2), (21, 2))
print("(0, 0) to (24, 24):")
a_star((0, 0), (24, 24))
