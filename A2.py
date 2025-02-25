#! /usr/bin/python3

import random

################################################################
#
# Three basic players
#
################################################################

def nim_minimal(n):
    return 1  # 1 is always a legal move, unless we already lost

def nim(n):
    # Note: n is guaranteed to be at least 1
    return random.choice(range(1, min(n,3)+1))

def nim_best(n):
    taken = n % 4
    if taken:
        return taken
    else:  # taken is 0, we lose - just take randomly
        return random.choice(range(1, min(n,3)+1))

def nim_human(n):
    while True:  # Get input until it's legal
        taken = int(input(f"There are {n} sticks. How many do you take? (1/2/3) "))
        if taken in range(1, min(n,3)+1):
            return taken
        print("Illegal move.")

################################################################
#
# Player candidates
#
################################################################

# These are the available functions for players
player_pool = [nim_minimal, nim, nim_best, nim_human]

# Transform into a dictionary with function names mapped to functions
player_pool = { p.__name__: p for p in player_pool }

def select_players():
    players = []  # We need two players
    while len(players) < 2:
        print("These are the players: %s" % "/".join(player_pool.keys()))
        p = input("Name one: ").strip()
        if p not in player_pool.keys():
            print("Not a valid player. Select again.")
            continue
        players.append(p)

    print(f"Player {players[0]} begins, player {players[1]} plays second.")
    return players

################################################################
#################################################################
#
# Game controller
#
################################################################

def game():
    while True:
        n = int(input("Heap size? "))
        if n > 0: 
            break  # Accept only positive values

    current, other = tuple(select_players())  # Choose players

    # Game loop
    while n > 0:
        print(f"Heap has {n} sticks.")
        taken = player_pool[current](n)  # Current player takes a move
        print(f"{current} takes {taken} sticks.\n")
        n -= taken  # Update heap
        current, other = other, current  # Switch turns
    print(f"{current} has lost.")  # The last player to play loses

# Run the game
game()




# Nim Game

# import random

# def nim_game():
#     # Step 1: Initialize the game
#     n = int(input("Enter the number of sticks: "))  # User sets the number of sticks
#     player_turn = True  # True = Human's turn, False = AI's turn

#     print(f"\nStarting Nim Game with {n} sticks!")
    
#     # Step 2: Game loop
#     while n > 0:
#         print(f"\nSticks remaining: {n}")

#         # Step 3: Player's Turn
#         if player_turn:
#             move = int(input("Your turn! Pick 1, 2, or 3 sticks: "))
#             while move not in [1, 2, 3] or move > n:
#                 print("Invalid move. Pick between 1 and 3 sticks.")
#                 move = int(input("Your turn! Pick 1, 2, or 3 sticks: "))
#         else:
#             # Step 4: AI's Turn (Optimal Strategy)
#             move = optimal_move(n)
#             print(f"AI removes {move} sticks.")

#         # Step 5: Update the game state
#         n -= move
#         player_turn = not player_turn  # Switch turn

#     # Step 6: Determine winner
#     if player_turn:
#         print("\nAI wins! Better luck next time. 🤖")
#     else:
#         print("\nCongratulations! You win! 🎉")

# def optimal_move(n):
#     if n % 4 == 0:
#         return random.choice([1, 2, 3])  # Random move when no forced win
#     else:
#         return n % 4  # Leaves opponent with a multiple of 4

# # Run the game
# nim_game()