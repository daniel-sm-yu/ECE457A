distance = [
    [0,1,2,3,4,1,2,3,4,5,2,3,4,5,6,3,4,5,6,7],
    [1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5,6],
    [2,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5,4,3,4,5],
    [3,2,1,0,1,4,3,2,1,2,5,4,3,2,3,6,5,4,3,4],
    [4,3,2,1,0,5,4,3,2,1,6,5,4,3,2,7,6,5,4,3],
    [1,2,3,4,5,0,1,2,3,4,1,2,3,4,5,2,3,4,5,6],
    [2,1,2,3,4,1,0,1,2,3,2,1,2,3,4,3,2,3,4,5],
    [3,2,1,2,3,2,1,0,1,2,3,2,1,2,3,4,3,2,3,4],
    [4,3,2,1,2,3,2,1,0,1,4,3,2,1,2,5,4,3,2,3],
    [5,4,3,2,1,4,3,2,1,0,5,4,3,2,1,6,5,4,3,2],
    [2,3,4,5,6,1,2,3,4,5,0,1,2,3,4,1,2,3,4,5],
    [3,2,3,4,5,2,1,2,3,4,1,0,1,2,3,2,1,2,3,4],
    [4,3,2,3,4,3,2,1,2,3,2,1,0,1,2,3,2,1,2,3],
    [5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,4,3,2,1,2],
    [6,5,4,3,2,5,4,3,2,1,4,3,2,1,0,5,4,3,2,1],
    [3,4,5,6,7,2,3,4,5,6,1,2,3,4,5,0,1,2,3,4],
    [4,3,4,5,6,3,2,3,4,5,2,1,2,3,4,1,0,1,2,3],
    [5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1,2],
    [6,5,4,3,4,5,4,3,2,3,4,3,2,1,2,3,2,1,0,1],
    [7,6,5,4,3,6,5,4,3,2,5,4,3,2,1,4,3,2,1,0],
]

flow = [
    [0,0,5,0,5,2,10,3,1,5,5,5,0,0,5,4,4,0,0,1],
    [0,0,3,10,5,1,5,1,2,4,2,5,0,10,10,3,0,5,10,5],
    [5,3,0,2,0,5,2,4,4,5,0,0,0,5,1,0,0,5,0,0],
    [0,10,2,0,1,0,5,2,1,0,10,2,2,0,2,1,5,2,5,5],
    [5,5,0,1,0,5,6,5,2,5,2,0,5,1,1,1,5,2,5,1],
    [2,1,5,0,5,0,5,2,1,6,0,0,10,0,2,0,1,0,1,5],
    [10,5,2,5,6,5,0,0,0,0,5,10,2,2,5,1,2,1,0,10],
    [3,1,4,2,5,2,0,0,1,1,10,10,2,0,10,2,5,2,2,10],
    [1,2,4,1,2,1,0,1,0,2,0,3,5,5,0,5,0,0,0,2],
    [5,4,5,0,5,6,0,1,2,0,5,5,0,5,1,0,0,5,5,2],
    [5,2,0,10,2,0,5,10,0,5,0,5,2,5,1,10,0,2,2,5],
    [5,5,0,2,0,0,10,10,3,5,5,0,2,10,5,0,1,1,2,5],
    [0,0,0,2,5,10,2,2,5,0,2,2,0,2,2,1,0,0,0,5],
    [0,10,5,0,1,0,2,0,5,5,5,10,2,0,5,5,1,5,5,0],
    [5,10,1,2,1,2,5,10,0,1,1,5,2,5,0,3,0,5,10,10],
    [4,3,0,1,1,0,1,2,5,0,10,0,1,5,3,0,0,0,2,0],
    [4,0,0,5,5,1,2,5,0,0,0,1,0,1,0,0,0,5,2,0],
    [0,5,5,2,2,0,1,2,0,5,2,1,0,5,5,0,5,0,1,1],
    [0,10,0,5,5,1,0,2,0,5,2,2,0,5,10,2,2,1,0,6],
    [1,5,0,5,1,5,10,10,2,2,5,5,5,0,10,0,0,1,6,0],
]

# encode solution as a 20-element permutation list, value is department number
n = 20
# tabu list size 
tabuTenure = 5
# stopping criterion
maxIterations = 100

# tabu structure
tabu = [[0 for _ in range(n)] for _ in range(n)]

def decrementTabu():
    for i in range(n):
        for j in range(n):
            tabu[i][j] = max(0, tabu[i][j] - 1)

def cost(solution):
    cost = 0

    for i in range(n):
        for j in range(i + 1, n):
            # distance is between location (indices)
            d = distance[i][j]
            # flow is between departments (value)
            department1 = solution[i] - 1
            department2 = solution[j] - 1 
            f = flow[department1][department2]

            cost += d * f

    return cost

def fullNeighborhood(solution):
    neighborsAndSwaps = []

    for i in range(n):
        for j in range(i + 1, n):
            neighbor = solution[:i] + [solution[j]] + solution[i + 1:j] + [solution[i]] + solution[j + 1:]
            swap = (i, j)
            neighborsAndSwaps.append((neighbor, swap))

    return neighborsAndSwaps

def move(neighborsAndSwaps):
    neighborsAndSwaps.sort(key=lambda x: cost(x[0]))
    return neighborsAndSwaps[0]

def TS(initialSolution):
    solution = initialSolution
    bestSolution = initialSolution
    bestSolutionCost = cost(initialSolution)

    for _ in range(maxIterations):
        # create a candidate list of solutions
        candidateSolutions = fullNeighborhood(solution)

        # evaluate solutions and choose the best admissable solution
        solution, swap = move(candidateSolutions)
        solutionCost = cost(solution)

        if solutionCost < bestSolutionCost:
            bestSolution = solution
            bestSolutionCost = solutionCost

        # update tabu
        decrementTabu()
        tabu[swap[0]][swap[1]] = tabuTenure
    
    return bestSolution

initialSolution = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
bestSolution = TS(initialSolution)

print(bestSolution)
print("cost:", cost(bestSolution))