import heapq
from collections import namedtuple

Node = namedtuple('Node', 'state, parent, cost, depth')

def manhattan_distance(state):
    return sum(abs((tile - 1) % 3 - i % 3) + abs((tile - 1) // 3 - i // 3) for i, tile in enumerate(state) if tile != 0)

def a_star_search(initial_state):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    frontier = [Node(initial_state, None, 0, 0)]
    explored = set()
    while frontier:
        current = heapq.heappop(frontier)
        explored.add(tuple(current.state))
        if current.state == goal_state:
            path = [current.state]
            while current.parent:
                current = current.parent
                path.append(current.state)
            return path[::-1]
        for neighbor in [swap(current.state, current.state.index(0), i) for i in range(9) if abs(i - current.state.index(0)) in [1, 3]]:
            if tuple(neighbor) not in explored:
                heapq.heappush(frontier, Node(neighbor, current, current.cost + 1, current.depth + 1))
    return None

def swap(state, i, j):
    state_list = state.copy()
    state_list[i], state_list[j] = state_list[j], state_list[i]
    return state_list

if __name__ == '__main__':
    initial_state = [1, 5, 3, 4, 0, 2, 7, 6, 8]
    solution = a_star_search(initial_state)
    if solution:
        for i, state in enumerate(solution):
            print(f"Step {i}:")
            for j in range(3):
                print(f"{state[j*3]:2} {state[j*3+1]:2} {state[j*3+2]:2}")
            print()
    else:
        print("No solution found.")