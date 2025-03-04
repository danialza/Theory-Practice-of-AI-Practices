E = 0
C = 1
S = 2

start_stable = [C, C, C, E, S, S, S]
goal_stable = [S, S, S, E, C, C, C]

# Only Moves => CE 10 / ES 02 / CSE 120 / ECS 012


def main(stable):
    empty = stable.index(E)
    candidate = [empty-2, empty-1 , empty+1, empty+2]
    # valid_candidate = []

    # for e in candidate:
    #     if e >=0 and e < len(stable):
    #         valid_candidate.append(e)
    
    # same as upper code
    candidate = [e for e in candidate if e >= 0 and e < len(stable)]

    movements = [c for c in candidate if
                stable[c:c+2] == [C, E] or
                stable[c-1:c+1] == [E, S] or
                stable[c-2:c+1] == [E, C, S] or
                stable[c:c+3] == [C, S, E]
    ]   

    # Change Process

    for m in movements:
        temp_stable = stable[:]
        temp_stable[m],temp_stable[empty]= temp_stable[empty],temp_stable[m]
        yield temp_stable
                   
def recursion(stable):
    #Base Case
    if stable == goal_stable:
        print("We Got The Answer")
        return [stable]
    for stable in main(stable):
       sol = recursion(stable)
       if sol:
           return [stable] + sol

for s in recursion(start_stable):
    print (s)


# if __name__ == "__main__" :
#     recursion(stable=start_stable)