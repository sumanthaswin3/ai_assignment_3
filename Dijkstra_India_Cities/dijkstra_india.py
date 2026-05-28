import csv
import heapq
from collections import defaultdict


def load_graph_from_csv(filename):
    graph = defaultdict(list)

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            source = row["source"].strip()
            destination = row["destination"].strip()
            distance = int(row["distance"])

            # undirected graph
            graph[source].append((destination, distance))
            graph[destination].append((source, distance))

    return graph


def dijkstra(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        current_distance, current_city, path = heapq.heappop(priority_queue)

        if current_city in visited:
            continue

        visited.add(current_city)
        path = path + [current_city]

        if current_city == goal:
            return current_distance, path, visited

        for neighbor, distance in graph[current_city]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (current_distance + distance, neighbor, path)
                )

    return float("inf"), [], visited


def main():
    print("=== Dijkstra's Algorithm for Indian Cities ===")

    graph = load_graph_from_csv("cities_distances.csv")

    print("\nAvailable cities:")
    print(", ".join(sorted(graph.keys())))

    start = input("\nEnter start city: ").strip()
    goal = input("Enter goal city: ").strip()

    if start not in graph or goal not in graph:
        print("\nError: One or both cities are not in the dataset.")
        return

    shortest_distance, shortest_path, visited_nodes = dijkstra(graph, start, goal)

    if shortest_distance == float("inf"):
        print("\nNo path found between the given cities.")
    else:
        print("\nShortest Path:", " -> ".join(shortest_path))
        print("Total Distance:", shortest_distance, "km")
        print("Visited Nodes:", len(visited_nodes))


if __name__ == "__main__":
    main()
