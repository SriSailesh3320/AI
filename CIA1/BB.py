def read_graph_from_file(file_name):
    graph = {}
    heuristic = {}
    reading_heuristic = False

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.startswith("Heuristic Values:"):
                reading_heuristic = True
                continue

            if reading_heuristic:
                try:
                    vertex, value = line.split(": ")
                    heuristic[vertex] = int(value)
                except ValueError:
                    print(f"Skipping malformed line in heuristic section: {line}")
            else:
                try:
                    vertex, neighbors_str = line.split(": ", 1)
                    neighbors = eval(neighbors_str)  
                    graph[vertex] = neighbors
                except ValueError:
                    print(f"Skipping malformed line in graph section: {line}")

    return graph, heuristic

def branch_and_bound(graph, start, goal):
    queue = [(0, start, [start])]
    best_path = None
    min_cost = float('inf')

    while queue:
        current_cost, node, path = queue.pop(0)

        if node == goal:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        for neighbor, cost in graph[node].items():
            if neighbor not in path:
                queue.append((current_cost + cost, neighbor, path + [neighbor]))
                queue = sorted(queue, key=lambda x: x[0])

    return best_path, min_cost

def save_result_to_file(path, cost, output_file, search_type):
    with open(output_file, 'w') as file:
        if path:
            file.write(f"{search_type} Best Path: {path} with cost {cost}\n")
        else:
            file.write(f"{search_type} No path found.\n")
    print(f"Result saved to {output_file}")


if __name__ == "__main__":
    input_file = input("Enter the input file name (e.g., graph_output.txt): ")
    start_vertex = input("Enter the start vertex: ")
    goal_vertex = input("Enter the goal vertex: ")
    result_file = input("Enter the result output file name (e.g., result.txt): ")

    graph, _ = read_graph_from_file(input_file)
    path, cost = branch_and_bound(graph, start_vertex, goal_vertex)
    save_result_to_file(path, cost, result_file, "Branch and Bound")
