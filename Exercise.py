
# def hanoi(n, start, goal, spare):
#     if n == 1:  # Base case: Only one disk
#         print(start, "->", goal)
#         return
#     hanoi(n - 1, start, spare, goal)  # Move (n-1) disks to spare
#     print(start, "->", goal)  # Move nth disk to goal
#     hanoi(n - 1, spare, goal, start)  # Move (n-1) disks to goal

# # Solve for 4 disks
# hanoi(4, 1, 2, 3)

# Ok lets do and create permutation for on list [1,2,3,4]
# Permutations (Recursive) Example

# # select one form the list 
# def changer(e,s):
#     for i in range(len(s)+1):
#         change = s[:i] + [e] + s[i:]
#         yield change

# def my_list(list_asli):
#     if list_asli == []:
#         yield []
#     else:
#         e = list_asli[0]
#         s1 = list_asli[1:]
#         for s2 in my_list(s1):
#             for p in changer(e, s2):
#                 yield(p)

# # Calling the function with a list
# for s in my_list([1, 2, 3, 4]):
#     print(s)
# # my_list([1, 2])
# # my_list([1])


# # Cow= 1 & Sheep= 2

# state = [1, 1, 1, 1, 0, 2, 2, 2, 2]
# goal = [2, 2, 2, 2, 0, 1, 1, 1, 1]

# def goaler():
#     spaceindex = state.index(0)
#     moves = [spaceindex-2, spaceindex-1,spaceindex+1,spaceindex+2]
#     print(spaceindex)
#     print(moves)


# goaler()

E = 0
C = 1
S = 2

start_stable = [C, C, C, E, S, S, S]
goal_stable = [S, S, S, E, C, C, C]

# start_stable = [C, C, C, C, E, S, S, S, S]
# goal_stable = [S, S, S, S, E, C, C, C, C]

# start_stable = [C, C, C,C, C, C,C, C, C,C, C, C, E, S, S, S, S, S, S, S, S, S]
# goal_stable = [S, S, S,S, S, S,S, S, S, E, C, C, C, C, C, C, C, C, C, C, C, C]


def successors(stable):
    # find empty spot
    empty = stable.index(E)
    # generate list of unfiltered candidate positions
    candidates = [empty-2, empty-1, empty+1, empty+2]
    # keep only those which are inside the stable
    
    candidates = [sms for sms in candidates if sms >= 0 and sms < len(stable)]

    # for c in candidates:
    #     if c >= 0 and c < len(stable):  
    #         valid_candidates.append(c)

    # Cows can always move right, Sheep always left, and from two fields
    # apart, they have to jump over an opposite animal
    candidates = [c for c in candidates if
                    stable[c:c+2] == [C, E] or # cow can move right
                    stable[c-1:c+1] == [E, S] or # sheep can move left
                    stable[c:c+3] == [C, S, E] or # cow jumps over sheep
                    stable[c-2:c+1] == [E, C, S]] # sheep jumps over cow
    
    # make sure that all these entries are occupied
    # (not necessary for operation, just better style)
    assert not [c for c in candidates if stable[c] == E]
    for c in candidates:
        new_stable = stable[:] # make a copy
    # move the candidate into empty pos
        new_stable[c], new_stable[empty] = new_stable[empty], new_stable[c]
        yield new_stable # remember where we were

def solution(stable):
    if stable == goal_stable:
        return [stable]
    # else, depth first
    for new_stable in successors(stable):
        # print new_stable
        sol = solution(new_stable)
        if sol:
            return [stable] + sol
        
for s in solution(start_stable):
    print (s)

