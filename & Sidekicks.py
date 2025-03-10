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


class Hero_Token(Hero):
    def token(self, state):
        pairs = sorted(state[0].items())
        return tuple(pairs), state[1]

def depth_first_search_hashed(problem, node, visited=set()):
    token = problem.token(node)
    if token in visited:
        return None
    visited.add(token)
    if problem.goal(node):
        return [node]
    for n_succ in problem.suc(node):
        sol = depth_first_search_hashed(problem, n_succ, visited)
        if sol:
            sol = [node] + sol
            return sol

h = Hero_Token()
path = depth_first_search_hashed(h, h.start())
print(path)                