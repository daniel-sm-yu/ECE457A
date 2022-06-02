
# Breath-First Search

from maze import *

m = len(maze)
n = len(maze[0])
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(start, end):
    openList = [[start]]  # queue of paths
    closedList = []

    while openList:
        path = openList.pop(0)
        node = path[-1]

        i, j = node

        # check for i and j out of bounds, node is wall, and previously visited
        if i < 0 or i >= m or j < 0 or j >= n or maze[i][j] or node in closedList:
            continue

        closedList.append(node)

        if node == end:
            print("path: " + str(path))
            print("cost: " + str(len(path)))
            print("number of explored nodes: " + str(len(closedList)))

            # for a, b in path:
            #     maze[a][b] = 5
            # printMaze(maze)

            return

        for x, y in directions:
            openList.append(path + [(i + x, j + y)])


print("S to E1:")
bfs((11, 2), (19, 23))
print("S to E2:")
bfs((11, 2), (21, 2))
print("(0, 0) to (24, 24):")
bfs((0, 0), (24, 24))
