
# Depth-First Search

from copy import deepcopy
from maze import *

m = len(maze)
n = len(maze[0])
directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def dfs(start, end):
    openList = [[start]]  # stack of paths
    closedList = []

    while openList:
        path = openList.pop()
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
            openList.append(path + [(i + x, j + y)])


print("S to E1:")
dfs((11, 2), (19, 23))
print("S to E2:")
dfs((11, 2), (21, 2))
print("(0, 0) to (24, 24):")
dfs((0, 0), (24, 24))
