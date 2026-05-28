import heapq
import random

GRID_SIZE = 70


def generate_grid(density):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    obstacle_count = int(GRID_SIZE * GRID_SIZE * density)

    for _ in range(obstacle_count):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        grid[x][y] = 1

    return grid


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors(node):
    x, y = node

    moves = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    valid = []

    for nx, ny in moves:
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            valid.append((nx, ny))

    return valid


def astar(grid, start, goal):

    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {}
    cost_so_far = {}

    came_from[start] = None
    cost_so_far[start] = 0

    nodes_expanded = 0

    while frontier:

        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        nodes_expanded += 1

        for next_node in neighbors(current):

            if grid[next_node[0]][next_node[1]] == 1:
                continue

            new_cost = cost_so_far[current] + 1

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:

                cost_so_far[next_node] = new_cost

                priority = new_cost + heuristic(goal, next_node)

                heapq.heappush(frontier, (priority, next_node))

                came_from[next_node] = current

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = came_from.get(node)

    path.reverse()

    return path, nodes_expanded


def main():

    print("UGV Path Planning with Static Obstacles")

    density_levels = {
        "low": 0.1,
        "medium": 0.2,
        "high": 0.3
    }

    level = input("Choose obstacle density (low/medium/high): ").lower()

    if level not in density_levels:
        print("Invalid density level")
        return

    grid = generate_grid(density_levels[level])

    start = (0, 0)
    goal = (69, 69)

    path, nodes = astar(grid, start, goal)

    print("\nStart:", start)
    print("Goal:", goal)
    print("Path Length:", len(path))
    print("Nodes Expanded:", nodes)
    print("Path:", path)


if __name__ == "__main__":
    main()
