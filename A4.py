class HeroSidekickBFS:
    def __init__(self):
        self.other_side = {"left": "right", "right": "left"}

    def start(self):
        """All heroes and sidekicks start on the left."""
        return {(person, index): "left" for person in ["hero", "kick"] for index in [1, 2]}, "left"

    def goal(self, state):
        """Check if all characters are on the right side."""
        person_side, _ = state
        return all(pos == "right" for pos in person_side.values())

    def safe(self, state):
        """Ensure no sidekick is left alone with another hero."""
        person_side, _ = state
        for side in ["left", "right"]:
            sidekicks = [idx for (person, idx) in person_side if person == "kick" and person_side[(person, idx)] == side]
            heroes = [idx for (person, idx) in person_side if person == "hero" and person_side[(person, idx)] == side]
            for kick in sidekicks:
                if kick not in heroes:
                    return False
        return True

    def successors(self, state):
        """Generate valid successor states."""
        person_side, boat = state
        candidates = [p for p in person_side if person_side[p] == boat]

        for p1 in candidates:
            for p2 in candidates:
                if p1 == p2:
                    continue
                new_side = person_side.copy()
                new_side[p1], new_side[p2] = self.other_side[boat], self.other_side[boat]
                new_state = new_side, self.other_side[boat]
                if self.safe(new_state):
                    yield new_state

    def bfs(self):
        """Breadth-First Search Implementation."""
        from collections import deque
        start_state = self.start()
        queue = deque([(start_state, [])])
        visited = set()

        while queue:
            state, path = queue.popleft()
            if self.goal(state):
                return path + [state]
            visited.add(tuple(state[0].items()))
            for next_state in self.successors(state):
                if tuple(next_state[0].items()) not in visited:
                    queue.append((next_state, path + [state]))

        return None

# Running BFS
solver = HeroSidekickBFS()
solution = solver.bfs()
print("Solution Path:", solution)


# 3.2

def count_search_nodes(search_algorithm):
    solver = HeroSidekickBFS()
    visited = set()
    queue = [(solver.start(), [])]
    
    while queue:
        state, path = queue.pop(0) if search_algorithm == "BFS" else queue.pop()
        visited.add(tuple(state[0].items()))
        
        if solver.goal(state):
            return len(visited)
        
        for next_state in solver.successors(state):
            if tuple(next_state[0].items()) not in visited:
                queue.append((next_state, path + [state]))

# Count nodes tested in DFS and BFS
bfs_nodes = count_search_nodes("BFS")
dfs_nodes = count_search_nodes("DFS")

print(f"Positions tested - BFS: {bfs_nodes}, DFS: {dfs_nodes}")


# 3.3

import heapq

class HeroSidekickAStar(HeroSidekickBFS):
    def heuristic(self, state):
        """Estimate remaining moves (number of people not on the right side)."""
        person_side, _ = state
        return sum(1 for pos in person_side.values() if pos == "left")

    def astar(self):
        """A* Search Implementation."""
        start_state = self.start()
        queue = [(self.heuristic(start_state), 0, start_state, [])]
        visited = set()

        while queue:
            _, cost, state, path = heapq.heappop(queue)
            if self.goal(state):
                return path + [state]
            visited.add(tuple(state[0].items()))
            for next_state in self.successors(state):
                if tuple(next_state[0].items()) not in visited:
                    heapq.heappush(queue, (self.heuristic(next_state) + cost + 1, cost + 1, next_state, path + [state]))

        return None

# Running A* Search
solver = HeroSidekickAStar()
solution = solver.astar()
print("A* Solution Path:", solution)


# 3.4

class SixCoins:
    GOAL_STATE = (1, 1, 1, 0, 0, 0)

    def __init__(self, start_state):
        self.start_state = start_state

    def heuristic(self, state):
        """Estimate remaining swaps needed."""
        return sum(abs(state[i] - self.GOAL_STATE[i]) for i in range(6))

    def successors(self, state):
        """Generate valid successor states by swapping adjacent coins."""
        state = list(state)
        for i in range(5):
            if state[i] != state[i+1]:  # Swap only if different
                new_state = state[:]
                new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
                yield tuple(new_state)

    def best_first_search(self):
        """Best-First Search using heuristic."""
        queue = [(self.heuristic(self.start_state), self.start_state, [])]
        visited = set()

        while queue:
            _, state, path = heapq.heappop(queue)
            if state == self.GOAL_STATE:
                return path + [state]
            visited.add(state)
            for next_state in self.successors(state):
                if next_state not in visited:
                    heapq.heappush(queue, (self.heuristic(next_state), next_state, path + [state]))

        return None

# Running Search for 6-Coins Problem
solver = SixCoins((0, 0, 0, 1, 1, 1))
solution = solver.best_first_search()
print("6-Coins Solution Path:", solution)


# 3.5 

def minimax(n, is_max_turn):
    """Minimax algorithm for Nim (1-heap)."""
    if n == 0:
        return -1 if is_max_turn else 1  # If it's MAX's turn and no move left, MIN wins

    best_score = -float("inf") if is_max_turn else float("inf")
    
    for move in range(1, min(4, n + 1)):  # Legal moves: 1-3
        score = minimax(n - move, not is_max_turn)
        if is_max_turn:
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    return best_score

# Running Minimax for Nim with 5 sticks
print("Minimax Decision for 5 sticks:", minimax(5, True))

# 3.6

import random

class NimMonteCarlo:
    def __init__(self, simulations=1000):
        self.simulations = simulations  # Number of simulations per move

    def simulate_game(self, n, move):
        """Simulate a game starting from n sticks after making 'move'."""
        n -= move  # Apply the move
        player = False  # False = AI, True = Opponent

        while n > 0:
            move = random.choice(range(1, min(4, n + 1)))  # Random valid move
            n -= move
            player = not player  # Switch player

        return not player  # Return True if AI wins

    def best_move(self, n):
        """Use Monte Carlo simulations to find the best move."""
        move_scores = {move: 0 for move in range(1, min(4, n + 1))}  # Track wins per move

        for move in move_scores.keys():
            for _ in range(self.simulations):
                if self.simulate_game(n, move):
                    move_scores[move] += 1  # Count wins

        best_move = max(move_scores, key=move_scores.get)  # Select move with most wins
        return best_move

# Running Monte Carlo for Nim with 10 sticks
nim_ai = NimMonteCarlo(simulations=500)
best_choice = nim_ai.best_move(10)
print(f"Monte Carlo's best move for 10 sticks: {best_choice}")
