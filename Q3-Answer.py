# 3.1 no Library 

def bfs(start, goal, successors):
    queue = [[start]]  # Using a list instead of deque
    visited = set()  # Track visited states

    while queue:
        path = queue.pop(0)  # Remove the first element (FIFO)
        state = path[-1]

        if state == goal:
            return path  # Return the shortest path

        if state not in visited:
            visited.add(state)
            for next_state in successors(state):
                queue.append(path + [next_state])  # Add new path to queue

    return None  # No solution found

# Example Usage: Hero/Sidekick Problem
def hero_successors(state):
    # Define valid moves (example)
    return [state + 1, state - 1] if 0 <= state <= 10 else []

start_state = 0
goal_state = 5
solution = bfs(start_state, goal_state, hero_successors)
print("BFS Solution Path:", solution)


# 3.1

from collections import deque

def bfs(start, goal, successors):
    queue = deque([[start]])  # Queue stores paths
    visited = set()  # Track visited states

    while queue:
        path = queue.popleft()
        state = path[-1]

        if state == goal:
            return path  # Return the shortest path

        if state not in visited:
            visited.add(state)
            for next_state in successors(state):
                queue.append(path + [next_state])

    return None  # No solution found

# Example Usage
def hero_successors(state):
    # Define valid moves (example)
    return [state + 1, state - 1] if 0 <= state <= 10 else []

start_state = 0
goal_state = 5
solution = bfs(start_state, goal_state, hero_successors)
print("BFS Solution Path:", solution)

# 3.2

def dfs(start, goal, successors, visited=set()):
    if start == goal:
        return [start]
    visited.add(start)

    for next_state in successors(start):
        if next_state not in visited:
            result = dfs(next_state, goal, successors, visited)
            if result:
                return [start] + result

    return None  # No solution found

# Counting evaluations
def count_evaluations(search_fn, start, goal):
    visited = set()
    search_fn(start, goal, hero_successors, visited)
    return len(visited)

bfs_evaluations = count_evaluations(bfs, start_state, goal_state)
dfs_evaluations = count_evaluations(dfs, start_state, goal_state)

print("BFS Evaluated Positions:", bfs_evaluations)
print("DFS Evaluated Positions:", dfs_evaluations)


# 3.3

import heapq

def a_star(start, goal, successors, heuristic):
    queue = [(heuristic(start, goal), [start])]  # Priority queue
    visited = set()

    while queue:
        _, path = heapq.heappop(queue)
        state = path[-1]

        if state == goal:
            return path  # Solution found

        if state not in visited:
            visited.add(state)
            for next_state in successors(state):
                cost = len(path) + heuristic(next_state, goal)
                heapq.heappush(queue, (cost, path + [next_state]))

    return None  # No solution found

# Simple heuristic: Distance to goal
def heuristic(state, goal):
    return abs(goal - state)

solution = a_star(start_state, goal_state, hero_successors, heuristic)
print("A* Solution Path:", solution)

# 3.4

def six_coins_successors(state):
    new_states = []
    for i in range(len(state) - 1):
        if state[i] == 1 and state[i + 1] == 2:
            new_state = state[:i] + [2, 1] + state[i + 2:]
            new_states.append(new_state)
    return new_states

start_state = [1, 1, 1, 2, 2, 2]  # Example starting arrangement
goal_state = [2, 2, 2, 1, 1, 1]

solution = bfs(start_state, goal_state, six_coins_successors)
print("6-Coins BFS Solution Path:", solution)

# 3.5

def minimax(n, is_max):
    if n == 0:
        return -1 if is_max else 1  # Losing move for current player

    scores = []
    for move in range(1, min(4, n+1)):
        scores.append(minimax(n - move, not is_max))

    return max(scores) if is_max else min(scores)

def nim_best_move(n):
    for move in range(1, min(4, n+1)):
        if minimax(n - move, False) == 1:
            return move
    return 1  # Default move if no optimal choice

# Test
sticks = 10
while sticks > 0:
    move = nim_best_move(sticks)
    print(f"Computer removes {move} sticks.")
    sticks -= move
    if sticks == 0:
        print("Computer wins!")
        break


# 3.6

def minimax_tree(node, is_max):
    if isinstance(node, int):  # Terminal node
        return node

    left, right = node  # Assume binary tree
    left_val = minimax_tree(left, not is_max)
    right_val = minimax_tree(right, not is_max)

    return max(left_val, right_val) if is_max else min(left_val, right_val)

# Example tree (replace with actual values from PDF)
game_tree = ((3, 5), (2, 9))  # MAX picks the highest value
print("Optimal Move:", minimax_tree(game_tree, True))
