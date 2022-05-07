# Solving search problems

## Search algorithm
    1. If the frontier is empty - exit, there's no solution. (It may happen when all nodes that were added to the frontier were explored and no new ones were added, which means every explored path was a dead end.)
    2. Remove the node from the frontier and consider (explore) it. Which node is chosen is determined by the search algorithm used.
    3. Add all neighboring nodes (those that can be reached from this node and wasn't explored before) to the frontier, checking if any of them contain the goal state. If any of them do contain it, return the solution and exit. If not return current node to the explored set.

## DFS (Depth-First Search)
Explores one path till it exhausts. Then chooses the last unexplored path and does the same. Uses **stack** data structure (last-in first-out).

## BFS (Breadth-First Search)
Explores multiple paths at the same time, taking one step in each possible directon before taking the second step in each direction. Uses **queue** data structure (first-in first-out).

## Greedy Best-First Search
Explores the node closest to the goal which is determined by the heuristic function h(n). The function estimates how close the node is to the goal. In a maze, the function can be one that relies on the Manhattan distance between the node and the goal.

## A* Search
Like the Greedy Best-First Search, A* Search relies on heuristic function h(n) (estimated cost from the node to the goal), but also considers the distance g(n) (accrued cost) until current location.

# NOTE TO SELF
Do like in maze with queue instead of stack