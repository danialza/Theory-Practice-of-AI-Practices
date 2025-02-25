for i in range(3, 11):
    print(i)

for i in range(2, 12, 2):
    print(i)

mylist = [1, "jack", 5.0, 6, 9, 13]
for item in mylist:
    print(item)

for index, item in enumerate(mylist):
    print(index, item)

mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
mylist = [x for x in mylist if x == 3]
print(mylist)  # Output: [3, 3.0, 3, 3.0]


evens = [x for x in range(2, 21) if x % 2 == 0]

squares = [(x, x**2) for x in range(1, 11)]

divisors = [x for x in range(1, 37) if 36 % x == 0]

pairs = [(i, j) for i in range(1, 11) for j in range(1, 11) if j % i == 0 and i + j <= 50]

mylist = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
filtered = [x for x in mylist if x == 3]

def sqr(x):
    return x**2


def modify(li):
    li[-1] = "modified"

def left():
    print("left")

def right():
    print("right")

def walk():
    for i in range(10):
        if i % 2 == 0:
            left()
        else:
            right()

walk()


def sort4(a, b, c, d):
    nums = [a, b, c, d]
    sorted_nums = []
    
    while nums:
        smallest = min(nums)  
        sorted_nums.append(smallest)  
        nums.remove(smallest)  

    return tuple(sorted_nums)

print(sort4(4, 1, 3, 2)) 

def sort4(a, b, c, d):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if a > d:
        a, d = d, a
    if b > c:
        b, c = c, b
    if b > d:
        b, d = d, b
    if c > d:
        c, d = d, c

    return (a, b, c, d)

def hanoi(n, start, goal, temp):
    if n == 1:
        print(f"Move disk from {start} to {goal}")
    else:
        hanoi(n-1, start, temp, goal)
        print(f"Move disk from {start} to {goal}") 
        hanoi(n-1, temp, goal, start)  

hanoi(3, "A", "C", "B")


def hanoi_4_pegs(n, start, goal, temp1, temp2):
    if n == 1:
        print(f"Move disk from {start} to {goal}")
    elif n == 2:
        print(f"Move disk from {start} to {temp1}")
        print(f"Move disk from {start} to {goal}")
        print(f"Move disk from {temp1} to {goal}")
    else:
        k = n - int((2 * n) ** 0.5)  
        hanoi_4_pegs(k, start, temp2, temp1, goal)  
        hanoi(n - k, start, goal, temp1)  
        hanoi_4_pegs(k, temp2, goal, start, temp1) 

hanoi_4_pegs(4, "A", "D", "B", "C")

# without formulla :

def hanoi_4_pegs_iterative(n):
    stack = [(n, "A", "D", "B", "C")]  # Initial state (disks, start, goal, temp1, temp2)
    moves = []  # Store the moves

    while stack:
        num_disks, start, goal, temp1, temp2 = stack.pop()  # Get the latest task
        
        if num_disks == 1:
            moves.append(f"Move disk from {start} to {goal}")  # Base case
        elif num_disks == 2:
            # Direct move strategy for 2 disks
            moves.append(f"Move disk from {start} to {temp1}")
            moves.append(f"Move disk from {start} to {goal}")
            moves.append(f"Move disk from {temp1} to {goal}")
        else:
            # Finding the optimal split k
            k = num_disks - int((2 * num_disks) ** 0.5)  

            # Step 1: Move k disks to an intermediate peg
            stack.append((k, temp2, goal, start, temp1))
            # Step 2: Move n-k disks to the goal peg using classic 3-peg approach
            stack.append((num_disks - k, start, goal, temp1))  
            # Step 3: Move k disks from intermediate peg to goal
            stack.append((k, temp2, goal, start, temp1))  

    return moves

# Running the function for n=4 disks
moves = hanoi_4_pegs_iterative(4)
for move in moves:
    print(move)