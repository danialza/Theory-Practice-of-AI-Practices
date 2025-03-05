# 0.1

# 0.2
i = 1
print(type(i))
i += 3
print(i)

# 0.3
mylist = [1, 2, 3, 4, 5]
mylist[0]
mylist[3]

mylist.remove(3)
print (mylist)

mylist = [1, 2, 3, 4, 5]
mylist.pop(2)
print (mylist)

mylist = [1, 2, 3, 4, 5]
del mylist[2]
print (mylist)

mylist = [1, 2, 3, 4, 5]
mylist[2:3] = []
print (mylist)

# 0.4

for i in range(3,11):
    print (i)

for i in range(1,12):
    if i%2 == 0:
        print (i)    

for i in range(0,12,2):
    print (i)        

mylist4 = [1, "jack", 5.0, 6, 9, 13]
for i in mylist4:
    print(i)

for i, entry in enumerate(mylist4):
    print(i, entry)

mylist42 = [2, 3, 5, 3.0, 7, 3, 9, 3.0]

i = 0 
while i < len(mylist42):
    if not float(mylist42[i]) == 3.0:
        mylist42.pop(i)
    else:
        i += 1   
print(mylist42)

# 0.5

mylist51 = []
# for i in range (2,21):
#     if i % 2 == 0:
#         mylist5.append(i)
mylist51 = [i for i in range(2,21) if i%2==0]
print (mylist51)    

mylist52 = []
# for i in range(1,11):
#     answer = (i,i*i)
#     mylist51.append(answer) 
mylist52 = [(i,i*i) for i in range(1,11)]
print(mylist52)

mylist53 = [i for i in range(1,37) if 36%i == 0]
print(mylist53)

mylist54 = [(i,j) for i in range(1,11) 
                  for j in range(1,11) if
                  i+j<50 and i%j==0 and j%i==0]
print(mylist54)

mylist55 = [2, 3, 5, 3.0, 7, 3, 9, 3.0]
new_list55 = [i for i in mylist55 if float(i) == 3]

# 0.6

def sqr(x):
    return x*x

li = [1,2,3,4]
def modify(li):
    li[-1] = "modified"
    return li
print (modify(li))

# 6.3  => 3 - 2 - None

a = 3
def fun(a):
    print(a)
print(a)
print(fun(2))

# Ram Num - 6

def right():
    print ("right")

def left():
    print("left")

def walk():
    for i in range(0,10,2):
        left()
        right()
        i+=1

def walk_1():
    print("walk 1")
    for i in range(0,10,2):
    # each iteration prints twice, so we step twice
        left()
        right()

walk()


# 7

# 1 - 1 - 1
# Ram Position - 1 - 2 - 3

# 8 

notsort = [1,2,3,4]
def sort4(li):
    d = len(li)
    for i in range(d):
        for j in range(d-1):
            if li[i] > li[j]:
                li[i],li[j] = li[j],li[i]
    return(li)

sort4(notsort)

# 9

#! /usr/bin/python3
def hanoi(n, start, goal, ignore):
    if n == 1:
        print(start, "->", goal)
        return
    hanoi(n-1, start, ignore, goal)
    print(start, "->", goal)
    hanoi(n-1, ignore, goal, start)
hanoi(4, 1, 3, 2)

def hanoi4(n, start, goal, free1, free2 ):
    if n == 1:
        print(start,"->",goal)
        return
    hanoi(n-1, start, free1, goal, free2)
    print(start,"->",goal)
    hanoi(n-2,goal, free2, free1, goal )
    print(start,"->",goal)
    hanoi(n-3, free2, goal, free1, start)

hanoi4(4,1,4,2,3)

# def hanoi_4_pegs(n, source, target, auxiliary1, auxiliary2):
#     if n == 0:
#         return
#     if n == 1:
#         print(f"Move disk {n} from {source} to {target}")
#         return
    
#     # Finding optimal k using Frame-Stewart algorithm
#     k = n // 2
    
#     # Step 1: Move top k disks to an auxiliary peg
#     hanoi_4_pegs(k, source, auxiliary1, auxiliary2, target)
    
#     # Step 2: Move remaining (n-k) disks to target peg using 3 pegs
#     hanoi_4_pegs(n - k, source, target, auxiliary2, auxiliary1)
    
#     # Step 3: Move k disks from auxiliary peg to target peg
#     hanoi_4_pegs(k, auxiliary1, target, source, auxiliary2)

# # Example: Solve Tower of Hanoi with 4 pegs and 4 disks
# n = 4
# hanoi_4_pegs(n, 'A', 'D', 'B', 'C')