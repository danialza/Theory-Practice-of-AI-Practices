
# def hanoi(n, start, goal, spare):
#     if n == 1:  # Base case: Only one disk
#         print(start, "->", goal)
#         return
#     hanoi(n - 1, start, spare, goal)  # Move (n-1) disks to spare
#     print(start, "->", goal)  # Move nth disk to goal
#     hanoi(n - 1, spare, goal, start)  # Move (n-1) disks to goal

# # Solve for 4 disks
# hanoi(4, 1, 2, 3)

# def insertion(e, s):
#     for i in range(len(s) + 1):
#         yield s[:i] + [e] + s[i:]

# def perm(s):
#     if s == []:
#         yield []
#     else:
#         e, s1 = s[0], s[1:]
#         for s1p in perm(s1):
#             for p in insertion(e, s1p):
#                 yield p

# for p in perm([1,2,3]):  
#     print(p)  # Output: all possible orderings of [1,2,3]






# Ok lets do and create permutation for on list [1,2,3,4]

# select one form the list 
def my_list(list_asli):
    for i in list_asli:
        print(i)

# Calling the function with a list
my_list([1, 2, 3, 4])