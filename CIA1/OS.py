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


def oracle_search(graph, start, goal, heuristic):
    path = [start]
    current = start
    total_cost = 0

    while current != goal:
        neighbors = graph[current]

        next_node = min(neighbors, key=lambda x: total_cost + neighbors[x] + heuristic[x])
        
        path.append(next_node)
        total_cost += neighbors[next_node]
        current = next_node

        if current == goal:
            break

    print(f"Oracle Search Best Path: {path} with cost {total_cost}")
    return path, total_cost


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

    graph, heuristic = read_graph_from_file(input_file)
    path, cost = oracle_search(graph, start_vertex, goal_vertex, heuristic)
    save_result_to_file(path, cost, result_file, "Oracle Search")
