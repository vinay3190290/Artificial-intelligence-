import heapq

class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.g = float('inf')
        self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def a_star_search(graph, start, goal):
    open_list = [start]
    closed_list = set()

    start.g = 0
    start.f = start.heuristic

    while open_list:
        current = heapq.heappop(open_list)
        closed_list.add(current)

        if current.name == goal:
            path = []
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1]

        for neighbor, cost in graph[current.name].items():
            if neighbor!= 'heuristic':
                if neighbor not in [node.name for node in closed_list]:
                    neighbor_node = Node(neighbor, graph[neighbor]['heuristic'])
                    tentative_g = current.g + cost
                    if tentative_g < neighbor_node.g:
                        neighbor_node.g = tentative_g
                        neighbor_node.f = tentative_g + neighbor_node.heuristic
                        neighbor_node.parent = current
                        heapq.heappush(open_list, neighbor_node)

    return None

graph = {
    'A': {'B': 1, 'C': 4, 'heuristic': 5},
    'B': {'A': 1, 'C': 2, 'D': 5, 'heuristic': 3},
    'C': {'A': 4, 'B': 2, 'D': 1, 'heuristic': 2},
    'D': {'B': 5, 'C': 1, 'heuristic': 0}
}

start_node = Node('A', graph['A']['heuristic'])
goal_node = Node('D', graph['D']['heuristic'])

path = a_star_search(graph, start_node, goal_node.name)
print("Shortest Path:", path)