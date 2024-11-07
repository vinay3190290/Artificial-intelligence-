from collections import deque

def water_jug_problem(jug1, jug2, target):
    queue = deque([(0, 0, [])])
    visited = set((0, 0))
    while queue:
        a, b, path = queue.popleft()
        if a == target or b == target or a + b == target:
            return path + [(a, b)]
        for a_new, b_new in [(jug1, b), (a, jug2), (0, b), (a, 0), (a + min(b, jug1 - a), b - min(b, jug1 - a)), (a - min(a, jug2 - b), b + min(a, jug2 - b))]:
            if (a_new, b_new) not in visited:
                visited.add((a_new, b_new))
                queue.append((a_new, b_new, path + [(a, b)]))
    return None

jug1, jug2, target = 3, 5, 4
solution = water_jug_problem(jug1, jug2, target)
if solution:
    print("Solution found:")
    for i, (a, b) in enumerate(solution):
        print(f"Step {i}: {a} {b}")
else:
    print("No solution found.")