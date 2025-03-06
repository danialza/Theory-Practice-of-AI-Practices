import random
# 1.1 

def nim_min(n):
    return 1

def nim(n):
    return random.randint(1,min(3,n))

def nim_best(n):
    if n >= 4:
        return random.randint(1,min(3,n))
    return n % 4

def nim_human(n):
    while True:
        move = int(input(f"There are {n} sticks, How many stick you pick? "))
        if 1 < move < 4:
            return move
        print("Invalid Move! ")

all_players =[nim_min, nim, nim_best, nim_human]
all_players = {p.__name__:p for p in all_players}

def select_player():  
    players = []  
    for i in range(2):
        while True:
            player = input(f"Please select your {i+1} players! Our Available Players: {'/'.join(all_players.keys())} ")
            if player in all_players.keys():
                players.append(player)
                break
            else:
                print("Please input Valid Player Name!!")
    return players

def game():
    
    while True:
        n = int(input("Please input stick Numbers: "))
        if n > 0:
            break
        else:
            print("Please input Valit Number of Stick!")
    
    players = select_player()
    player1,player2 = players[0],players[1]

    # Game Play Start 

    while n >0 :
        print(f"There are {n} sticks remaining.")
        take = all_players[player1](n)
        print(f"Player {player1} take {take} Stick(s)")
        n = n - take
        player1, player2 = player2,player1
    print (f"Player {player1} has lost!! Sorry")

# Game Runner     
# game()



# ################################################################
# #
# # three basic players. ||| Solution From Uni
# #
# ################################################################
# def nim_minimal(n):
#     return 1 # 1 is always a legal move,
# # unless we already lost
# def nim(n):
# # note: n is guaranteed to be at least 1
#     return random.choice(range(1, min(n,3)+1))
# def nim_best(n):
#     taken = n % 4
#     if taken:
#         return taken
#     else: # taken is 0, we lose - just take randomly
#     # pick randomly 1 or more
#     # but never more than either limit of sticks, 3
#     # or available sticks, n
#         return random.choice(range(1, min(n,3)+1))

# def nim_human(n):
#     while True: # get input until it’s legal
#         taken = int(input("There are %d sticks. How many do you take? (1/2/3) " %n))
#     if taken in range(1, min(n,3)+1):
#        return taken
#     print("Illegal move.")
# ################################################################
# #
# # player candidates
# #
# ################################################################
# # these are the functions
# player_pool = [nim_minimal, nim, nim_best, nim_human]
# # transform into a dictionary with function name mapping to
# # function
# player_pool = { p.__name__:p for p in player_pool }
# def select_players():
#     players = [] # we need two
#     # select the players
#     while len(players) < 2:
#     # select more players
#         print("These are the players: %s" % "/".join(player_pool.keys()))
#         p = input("Name one: ")
#         if p not in player_pool.keys():
#             print("Not a valid player. Select again: ")
#             continue
#         players.append(p)
#     print("Player %s begins, player %s plays second." % tuple(players))
#     return players
# def game():
#     while True:
#         n = int(input("Heap size? "))
#         if n > 0: break # accept only positive
#     current, other = tuple(select_players()) # tuple with two elements
#     # game runs
#     while n > 0: # as long as there are sticks in the heap
#         print("Heap has %d sticks." % n)
#         taken = player_pool[current](n) # carry out move; guaranteed legal
#         print("%s takes %d sticks.\n" % (current, taken))
#         n -= taken # update heap
#         current, other = other, current # now it’s the other player’s turn
#         print("%s has lost." % current)


# 1.2

def sort4(x,y,z,u):
    if x>y:
        x,y = y,x
    if z>u:
        z,u = u,z
    if y>u:
        y,u = u,y
    if x>z:
        x,z=z,x
    if y>z:
        y,z=z,y
    return x,y,z,u

print(sort4(20,30,10,30))

def insertion(e, s):
    for i in range(len(s)+1):
        yield s[:i] + [e] + s[i:]

def perm(s):
    if s == []:
        yield []
    else:
        e, s1 = s[0], s[1:]
        for s1p in perm(s1):
            for p in insertion(e,s1p):
                yield p

# for p in perm([1,2,3,4]): print(p)

fourlist = list(range(1,4+1))
print (fourlist)
for unsorted in perm(fourlist):
    s = list(sort4(*unsorted)) # unpack
    print("Unsorted:", unsorted, "Sorting","Ok" if s == fourlist else "Wrong!")