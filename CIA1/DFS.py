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


def dfs(graph, start, goal, path=None, visited=None, cost=0):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path.append(start)
    visited.add(start)

    if start == goal:
        return path, cost

    for neighbor, edge_cost in graph[start].items():
        if neighbor not in visited:
            result, result_cost = dfs(graph, neighbor, goal, path, visited, cost + edge_cost)
            if result:
                return result, result_cost

    path.pop()
    return None, cost


def save_result_to_file(path, cost, output_file, search_type):
    with open(output_file, 'w') as file:
        if path:
            file.write(f"{search_type} Path: {path} with cost {cost}\n")
        else:
            file.write(f"{search_type} No path found.\n")
    print(f"Result saved to {output_file}")


if __name__ == "__main__":
    input_file = input("Enter the input file name (e.g., graph_output.txt): ")
    start_vertex = input("Enter the start vertex: ")
    goal_vertex = input("Enter the goal vertex: ")
    result_file = input("Enter the result output file name (e.g., result.txt): ")

    graph, heuristic = read_graph_from_file(input_file)
    path, cost = dfs(graph, start_vertex, goal_vertex)
    save_result_to_file(path, cost, result_file, "DFS")
