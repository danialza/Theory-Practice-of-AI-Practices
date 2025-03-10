# # Search in Python

# class Game:
#     def start(self):
#         pass
#     def goal(self,state):
#         pass
#     def successer(self,state):
#         pass

# # State : 
# # ({
# #     ('kick', 1): 'left',
# #     ('kick', 2): 'left',
# #     ('kick', 3): 'left',
# #     ('hero', 1): 'left',
# #     ('hero', 2): 'left',
# #     ('hero', 3): 'left'
# # }, "left")

# # Hero & Sidekicks 
# def select_traveller(candidates):
#     for first in range(len(candidates)):
#         yield [candidates[first]]
    
#     for first in range(len(candidates)):
#         for second in range(first+1 , len(candidates)):
#             yield [candidates[first], candidates[second]]

# other_side = {"left" : "right", "right":"left"}

# def safe(state):
#     person_side, _ = state
#     for side in ["left","right"]:
#         lone_kik = [index for (person,index) in person_side
#                     if person == "kick"
#                     if person_side[(person,index)] == side
#                     if person_side[("hero",index)] != side]
#         present_hero = [index for (person,index) in person_side
#                         if person == "hero"
#                         if person_side[(person,index)] == side]
        
#         if lone_kik and present_hero:
#             return False
#     return True


# class Hero:
#     def start(self):
#         return {(person, index):"left"
#                 for person in ["hero","kick"]
#                 for index in [1,2,3]
#                 },"left"

#     def goal(self,state):
#         person_side, _ = state
#         return set(person_side.values()) == {"right"}

#     def suc(self,state):
#         person_side, boat = state
#         people_with_boat = [p for p in person_side if person_side[p] == boat]

#         for travelers in select_traveller(people_with_boat):
#             new_side = person_side.copy()
#             for traveler in travelers:
#                 new_side[traveler] = other_side[boat]

#             new_state = (new_side, other_side[boat])
#             if safe(new_state):
#                 yield new_state

# class HeroToken1():
#     def token(self, state):
#         pairs = sorted(state[0].items())
#         return tuple(pairs), state[1]

# def depth_first_search_hashed(problem, node, visited=set()):
#     token = problem.token(node)
#     if token in visited:
#         return None
#     visited.add(token)
#     if problem.goal(node):
#         return [node]
#     for n_succ in problem.suc(node):
#         sol = depth_first_search_hashed(problem, n_succ, visited)
#         if sol:
#             sol = [node] + sol
#             return sol

# h = HeroToken1(Hero)
# path = depth_first_search_hashed(h, h.start())
# print(path)

# # # DFS Code

# # def depth_first_search(problem, node):
# #     if problem.goal == node:
# #         return (f"We Are Done, {[node]}")
# #     for n_succ in problem.succ(node):
# #         sol = depth_first_search(problem,n_succ)
# #         if sol:
# #             sol = [node] + sol
# #             return sol

# # h = Hero()
# # print(depth_first_search(h, h.start()))




# # set token for path

# # State : 
# # ({
# #     ('kick', 1): 'left',
# #     ('kick', 2): 'left',
# #     ('kick', 3): 'left',
# #     ('hero', 1): 'left',
# #     ('hero', 2): 'left',
# #     ('hero', 3): 'left'
# # }, "left")







# # Hero & Sidekicks 
# def select_traveller(candidates):
#     for first in range(len(candidates)):
#         yield [candidates[first]]
    
#     for first in range(len(candidates)):
#         for second in range(first+1 , len(candidates)):
#             yield [candidates[first], candidates[second]]

# other_side = {"left" : "right", "right":"left"}

# def safe(state):
#     person_side, _ = state
#     for side in ["left","right"]:
#         lone_kik = [index for (person,index) in person_side
#                     if person == "kick"
#                     if person_side[(person,index)] == side
#                     if person_side[("hero",index)] != side]
#         present_hero = [index for (person,index) in person_side
#                         if person == "hero"
#                         if person_side[(person,index)] == side]
        
#         if lone_kik and present_hero:
#             return False
#     return True


# class Hero:
#     def start(self):
#         return {(person, index):"left"
#                 for person in ["hero","kick"]
#                 for index in [1,2,3]
#                 },"left"

#     def goal(self,state):
#         person_side, _ = state
#         return set(person_side.values()) == {"right"}

#     def suc(self,state):
#         person_side, boat = state
#         people_with_boat = [p for p in person_side if person_side[p] == boat]

#         for travelers in select_traveller(people_with_boat):
#             new_side = person_side.copy()
#             for traveler in travelers:
#                 new_side[traveler] = other_side[boat]

#             new_state = (new_side, other_side[boat])
#             if safe(new_state):
#                 yield new_state

# class Hero_Token(Hero):
#     def token(self, state):
#         pairs = sorted(state[0].items())
#         return tuple(pairs), state[1]

# def depth_first_search_hashed(problem, node, visited=set()):
#     token = problem.token(node)
#     if token in visited:
#         return None
#     visited.add(token)
#     if problem.goal(node):
#         return [node]
#     for n_succ in problem.suc(node):
#         sol = depth_first_search_hashed(problem, n_succ, visited)
#         if sol:
#             sol = [node] + sol
#             return sol

# h = Hero_Token()
# path = depth_first_search_hashed(h, h.start())
# print(path)



# def dfs(graph, start, goal, path=None, visited=None):
#     # Initialize visited set and path list if not provided
#     if visited is None:
#         visited = set()
#     if path is None:
#         path = []
        
#     # Add current node to visited set and path list
#     visited.add(start)
#     path.append(start)
    
#     # Found the goal
#     if start == goal:
#         return path
        
#     # Explore neighbors
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             result = dfs(graph, neighbor, goal, path, visited)
#             if result:
#                 return result
                
#     # Backtrack
#     path.pop()
#     visited.remove(start)
#     return None

# # Example graph represented as adjacency list
# graph = {
#     'A': ['C', 'D'],  # Node A is connected to nodes C and D
#     'C': ['E'],       # Node C is connected to node E
#     'D': ['E'],       # Node D is connected to node E
#     'E': ['B'],       # Node E is connected to node B
#     'B': []           # Node B has no outgoing edges
# }

# # Find path from A to B
# path = dfs(graph, 'A', 'B')
# print("Path from A to B:", path)  # Will print the path found from A to B  # Will print the path found from A to B




# New Test For DFS

# Hero & Sidekicks 
def select_traveller(candidates):
    for first in range(len(candidates)):
        yield [candidates[first]]
    
    for first in range(len(candidates)):
        for second in range(first+1 , len(candidates)):
            yield [candidates[first], candidates[second]]

other_side = {"left" : "right", "right":"left"}

def safe(state):
    person_side, _ = state
    for side in ["left","right"]:
        lone_kik = [index for (person,index) in person_side
                    if person == "kick"
                    if person_side[(person,index)] == side
                    if person_side[("hero",index)] != side]
        present_hero = [index for (person,index) in person_side
                        if person == "hero"
                        if person_side[(person,index)] == side]
        
        if lone_kik and present_hero:
            return False
    return True


class Hero:
    def start(self):
        return {(person, index):"left"
                for person in ["hero","kick"]
                for index in [1,2,3]
                },"left"

    def goal(self,state):
        person_side, _ = state
        return set(person_side.values()) == {"right"}

    def suc(self,state):
        person_side, boat = state
        people_with_boat = [p for p in person_side if person_side[p] == boat]

        for travelers in select_traveller(people_with_boat):
            new_side = person_side.copy()
            for traveler in travelers:
                new_side[traveler] = other_side[boat]

            new_state = (new_side, other_side[boat])
            if safe(new_state):
                yield new_state

# def dfs(problem, node, visited=None):

#     if visited is None:
#         visited = set()

#     hashable_node = (tuple(sorted(node[0].items())), node[1])

#     if problem.goal(node):
#         return [node]

#     if hashable_node in visited:
#         return None

#     visited.add(hashable_node)

#     for p in problem.suc(node):
#         sol = dfs(problem , p , visited)
#         if sol:
#             return [node] + sol

#     return None

def dfs(problem, node, visited=None):

    if visited is None:
        visited = set()

    people_State, boat = node

    if problem.goal(node):
        return [node]

    if people_State in visited:
        return None

    visited.add(people_State)

    for p in problem.suc(node):
        sol = dfs(problem , p , visited)
        if sol:
            return [node] + sol

    return None


h = Hero()
start_stated = h.start()
path = dfs(h, start_stated)
print(path)
