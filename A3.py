# 2.1

import random

# Different Nim Variants

def nim_2(n):
# up to 2
    return random.choice(range(1, min(n,2)+1))

def nim_4(n):
# 1 to 4 stick
    return random.choice(range(1, min(n,4)+1))

def nim_last_loses(n):
    taken = n % 4
    if taken == 0:  
        return random.choice(range(1, min(n, 4) + 1))
    return taken 

def nim_human(n, max_remove=3, last_loses=False):
    while True:
        taken = int(input(f"There are {n} sticks. How many do you take? (1-{max_remove}) "))
        if taken in range(1, min(n, max_remove) + 1):
            return taken
        print("Illegal move.")


# Select Players and Variants

# Better than solution we have !!!
nim_variants = {
    "nim_2": nim_2,
    "nim_4": nim_4,
    "nim_best": nim_last_loses,
    "nim_human": nim_human
}

def select_players():
    players = []
    while len(players) < 2:
        print("These are the available players: %s" % "/".join(nim_variants.keys()))
        # Better : print(f"These are the available players: {'/'.join(nim_variants.keys())}")
        p = input("Select a player: ").strip()
        if p not in nim_variants.keys():
            print("Invalid selection. Try again.")
            continue
        players.append(p)

    print(f"Player {players[0]} vs Player {players[1]}.")
    return players

# Game Controller - Handles Different Rules

def nim_game():
    n = int(input("Enter the number of sticks: "))
    game_type = input("Choose a game variant (normal/nim_2/nim_4/last_loses): ").strip().lower()

    max_remove = 3
    last_loses = False

    if game_type == "nim_2":
        max_remove = 2
    elif game_type == "nim_4":
        max_remove = 4
    elif game_type == "last_loses":
        last_loses = True

    player1, player2 = select_players()
    
    players = { "nim_2": nim_2, "nim_4": nim_4, "nim_best": nim_last_loses, "nim_human": lambda n: nim_human(n, max_remove, last_loses) }
    
    current, other = player1, player2  # First player starts

    print(f"\nStarting Nim Game ({game_type}) with {n} sticks!\n")

    while n > 0:
        print(f"Sticks remaining: {n}")

        move = players[current](n)  # Get player move
        print(f"{current} removes {move} sticks.")

        n -= move  # Update game state
        if n == 0:  # Check if the game ends
            if last_loses:
                print(f"{current} loses the game! 🎭")
            else:
                print(f"{other} wins the game! 🎉")
            break

        current, other = other, current  # Switch turn

# Run the game
nim_game()


# 2.2

# ??? Not Found

# Define the opposite side of the river
other_side = {"left": "right", "right": "left"}

# Function to generate all possible moves (one or two travelers)
def select_travellers(candidates):
    """Generate all possible valid moves for the boat (1 or 2 travelers)."""
    for first in range(len(candidates)):
        yield [candidates[first]]  # One traveler
    for first in range(len(candidates)):
        for second in range(first + 1, len(candidates)):
            yield [candidates[first], candidates[second]]  # Two travelers

# Function to check if a state is safe
def safe(state):
    """Ensure no sidekick is left alone without their hero."""
    person_side, _ = state  # Extract current positions

    for side in ["left", "right"]:
        # Find all sidekicks on this side
        sidekicks = [index for (person, index) in person_side if person == "kick" and person_side[person, index] == side]

        # Find all heroes on this side
        heroes = [index for (person, index) in person_side if person == "hero" and person_side[person, index] == side]

        # Ensure no sidekick is alone **without their own hero**
        for kick in sidekicks:
            if kick not in heroes:  # If this sidekick's hero is missing, it's unsafe
                return False

    return True  # The state is safe

# Class defining the Hero/Sidekick problem (2 Heroes, 2 Sidekicks)
class Hero_Sidekick:
    def start(self):
        """Define the initial state: All heroes and sidekicks start on the left."""
        return {(person, index): "left" for person in ["hero", "kick"] for index in [1, 2]}, "left"

    def goal(self, state):
        """Check if all characters are on the right side (goal state)."""
        person_side, _ = state
        return set(person_side[person] for person in person_side) == {"right"}

    def succ(self, state):
        """Generate valid successor states."""
        person_side, boat = state  # Extract current positions

        # Identify people on the boat's side
        person_with_boat = [p for p in person_side if person_side[p] == boat]

        for traveller_group in select_travellers(person_with_boat):
            new_side = person_side.copy()  # Copy current state
            for traveller in traveller_group:
                new_side[traveller] = other_side[person_side[traveller]]  # Move travelers

            new_state = new_side, other_side[boat]  # Update boat's position

            if safe(new_state):  # Check if the move is valid
                yield new_state  # Return valid next state

# Implementing Depth-First Search (DFS) manually without deque
def depth_first_search(problem):
    """Perform DFS to find a solution path without using external libraries."""
    stack = [(problem.start(), [])]  # Stack holds (current state, path taken)
    visited = []  # Using a list instead of a set to track visited states

    while stack:
        current_state, path = stack.pop()  # Manually handling the stack

        if problem.goal(current_state):
            return path + [current_state]  # Solution found

        visited.append(current_state)  # Mark state as visited

        for next_state in problem.succ(current_state):
            if next_state not in visited:  # Ensure no revisits
                stack.append((next_state, path + [current_state]))

    return None  # No solution found

# Solve the problem with DFS
h = Hero_Sidekick()
solution_path = depth_first_search(h)

# Convert the solution path to a readable format
if solution_path:
    print("Solution Found! Steps to solve the Hero/Sidekick problem:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}: {state}")
else:
    print("No solution found!")


# 2.3

# Define the goal state for the 6-Coins Problem
GOAL_STATE = (1, 1, 1, 0, 0, 0)  # Example: First 3 coins should be 1 (heads), last 3 should be 0 (tails)

# Define possible moves (swap adjacent coins)
MOVES = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]  # Allowed swaps between adjacent positions

# Function to generate valid successor states
def generate_successors(state):
    """Generate all possible next states by swapping adjacent coins."""
    successors = []
    state = list(state)  # Convert tuple to list for modification

    for i, j in MOVES:
        new_state = state[:]  # Copy the current state
        new_state[i], new_state[j] = new_state[j], new_state[i]  # Swap two adjacent coins
        successors.append(tuple(new_state))  # Store new state as a tuple

    return successors

# Implementing Depth-First Search (DFS) manually
def dfs_6_coins(start_state, path=None, visited=None):
    """Perform DFS to find a sequence of moves to reach the goal state."""
    if path is None:
        path = []
    if visited is None:
        visited = []

    # If the current state is the goal, return the path
    if start_state == GOAL_STATE:
        return path + [start_state]

    # Mark the current state as visited
    visited.append(start_state)

    # Generate all valid next states
    for next_state in generate_successors(start_state):
        if next_state not in visited:  # Avoid revisiting states
            sol = dfs_6_coins(next_state, path + [start_state], visited)
            if sol:
                return sol  # Return the solution path if found

    return None  # No solution found

# Define the initial state
initial_state = (0, 0, 0, 1, 1, 1)  # Example: First 3 coins are tails, last 3 are heads

# Solve the 6-Coins Problem
solution_path = dfs_6_coins(initial_state)

# Convert the solution path to a readable format
if solution_path:
    print("Solution Found! Steps to transform the coins:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}: {state}")
else:
    print("No solution found!")


# 2.4

# Define the goal state for the Car Passing Puzzle
GOAL_STATE = (1, 1, 1, 0, 0, 0)  # Example: First 3 cars should be in the first 3 positions

# Define possible moves (move a car forward)
MOVES = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]  # Allowed forward moves

# Function to generate valid successor states
def generate_successors(state):
    """Generate all possible next states by moving cars forward."""
    successors = []
    state = list(state)  # Convert tuple to list for modification

    for i, j in MOVES:
        if state[i] == 1 and state[j] == 0:  # Move only if a car is present and the space is empty
            new_state = state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]  # Move the car forward
            successors.append(tuple(new_state))  # Store new state as a tuple

    return successors

# Implementing Depth-First Search (DFS) manually
def dfs_car_puzzle(start_state, path=None, visited=None):
    """Perform DFS to find a sequence of moves to reach the goal state."""
    if path is None:
        path = []
    if visited is None:
        visited = []

    # If the current state is the goal, return the path
    if start_state == GOAL_STATE:
        return path + [start_state]

    # Mark the current state as visited
    visited.append(start_state)

    # Generate all valid next states
    for next_state in generate_successors(start_state):
        if next_state not in visited:  # Avoid revisiting states
            sol = dfs_car_puzzle(next_state, path + [start_state], visited)
            if sol:
                return sol  # Return the solution path if found

    return None  # No solution found

# Define the initial state
initial_state = (0, 0, 0, 1, 1, 1)  # Example: First 3 spaces are empty, last 3 have cars

# Solve the Car Passing Puzzle
solution_path = dfs_car_puzzle(initial_state)

# Convert the solution path to a readable format
if solution_path:
    print("Solution Found! Steps to solve the Car Passing Puzzle:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}: {state}")
else:
    print("No solution found!")
