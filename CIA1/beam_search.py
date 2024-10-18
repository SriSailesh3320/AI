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

def beam_search(graph, start, goal, heuristic, beam_width=2):
    queue = [(start, [start], 0)]
    best_path = None
    min_cost = float('inf')

    while queue:
        next_level = []
        for node, path, current_cost in queue:
            if node == goal:
                if current_cost < min_cost:
                    min_cost = current_cost
                    best_path = path
                continue

            neighbors = sorted(graph[node].items(), key=lambda x: heuristic[x[0]])
            next_level.extend([(neighbor, path + [neighbor], current_cost + cost) for neighbor, cost in neighbors])

        queue = sorted(next_level, key=lambda x: heuristic[x[0]])[:beam_width]

    return best_path, min_cost

def save_result_to_file(path, cost, output_file):
    with open(output_file, 'w') as file:
        if path:
            file.write(f"Beam Search Best Path: {path} with cost {cost}\n")
        else:
            file.write("No path found.\n")
    print(f"Result saved to {output_file}")

if __name__ == "__main__":
    input_file = input("Enter the input file name (e.g., output.txt): ")
    start_vertex = input("Enter the start vertex: ")
    goal_vertex = input("Enter the goal vertex: ")
    result_file = input("Enter the result output file name (e.g., result.txt): ")
    beam_width = int(input("Enter the beam width (e.g., 2): "))

    graph, heuristic = read_graph_from_file(input_file)
    path, cost = beam_search(graph, start_vertex, goal_vertex, heuristic, beam_width)
    save_result_to_file(path, cost, result_file)
