from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0:
            return False
        if self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.boat != 0 and self.boat != 1:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if self.missionaries > self.cannibals and self.missionaries < 3:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0

    def __str__(self):
        return f"Missionaries: {self.missionaries}, Cannibals: {self.cannibals}, Boat: {self.boat}"

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

def apply_action(state, action):
    new_state = State(state.missionaries, state.cannibals, state.boat)
    if action == "move 2 missionaries":
        new_state.missionaries -= 2
        new_state.boat = 1 - new_state.boat
    elif action == "move 1 missionary":
        new_state.missionaries -= 1
        new_state.boat = 1 - new_state.boat
    elif action == "move 2 cannibals":
        new_state.cannibals -= 2
        new_state.boat = 1 - new_state.boat
    elif action == "move 1 cannibal":
        new_state.cannibals -= 1
        new_state.boat = 1 - new_state.boat
    return new_state

def bfs():
    queue = deque([(State(3, 3, 0), [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state.is_goal():
            return path + ["goal"]
        if state not in visited:
            visited.add(state)
            for action in ["move 2 missionaries", "move 1 missionary", "move 2 cannibals", "move 1 cannibal"]:
                new_state = apply_action(state, action)
                if new_state.is_valid():
                    queue.append((new_state, path + [action]))
    return None

solution = bfs()
if solution:
    print("SOLUTION FOUND:")
    for i, action in enumerate(solution):
        print(f"Step {i+1}: {action}")
else:
    print("NO SOLUTION FOUND")