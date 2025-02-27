# 4.1

def minimax(n, is_max):
    if n == 0:
        return -1 if is_max else 1  # Losing move for current player

    scores = []
    for move in range(1, min(4, n+1)):  # Can remove 1-3 sticks
        scores.append(minimax(n - move, not is_max))

    return max(scores) if is_max else min(scores)

def nim_best_move(n):
    for move in range(1, min(4, n+1)):
        if minimax(n - move, False) == 1:
            return move
    return 1  # Default move if no optimal choice

# Play the game
sticks = 10
while sticks > 0:
    move = nim_best_move(sticks)
    print(f"Computer removes {move} sticks.")
    sticks -= move
    if sticks == 0:
        print("Computer wins!")
        break


# 4.2

probability = 1 / 3  # One boy-boy case out of three possibilities
print(f"Probability of both children being boys: {probability}")


# 4.3 

from math import comb

def probability_k_boys(k, n=5):
    return comb(n, k) * (0.5 ** n)

# Compute probabilities
for k in range(6):
    print(f"P({k} boys) = {probability_k_boys(k):.4f}")


# 4.4

def probability_k_boys_general(k, n):
    return comb(n, k) * (0.5 ** n)

n = int(input("Enter the number of children: "))
for k in range(n + 1):
    print(f"P({k} boys out of {n}) = {probability_k_boys_general(k, n):.4f}")
