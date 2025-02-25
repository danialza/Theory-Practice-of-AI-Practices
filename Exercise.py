
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

# select one form the list 
def changer(e,s):
    for i in range(len(s)+1):
        change = s[:i] + [e] + s[i:]
        yield change

def my_list(list_asli):
    if list_asli == []:
        yield []
    else:
        e = list_asli[0]
        s1 = list_asli[1:]
        for s2 in my_list(s1):
            for p in changer(e, s2):
                yield(p)

# Calling the function with a list
for s in my_list([1, 2, 3, 4]):
    print(s)
# my_list([1, 2])
# my_list([1])
