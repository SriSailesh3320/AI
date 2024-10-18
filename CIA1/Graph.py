def input_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))

    for _ in range(num_vertices):
        vertex = input("Enter vertex name: ")
        graph[vertex] = {}
        num_edges = int(input(f"Enter the number of edges from {vertex}: "))
        
        for _ in range(num_edges):
            neighbor = input(f"Enter the neighbor of {vertex}: ")
            cost = int(input(f"Enter the cost to {neighbor}: "))
            graph[vertex][neighbor] = cost
    
    return graph

def input_heuristics():
    heuristic = {}
    num_vertices = int(input("Enter the number of vertices for heuristic values: "))

    for _ in range(num_vertices):
        vertex = input("Enter vertex name: ")
        value = int(input(f"Enter the heuristic value for {vertex}: "))
        heuristic[vertex] = value

    return heuristic

def save_to_file(graph, heuristic, output_file):
    with open(output_file, 'w') as f:
        f.write("Graph Structure:\n")
        for vertex, neighbors in graph.items():
            f.write(f"{vertex}: {neighbors}\n")
        
        f.write("\nHeuristic Values:\n")
        for vertex, value in heuristic.items():
            f.write(f"{vertex}: {value}\n")
    
    print(f"Graph and heuristics saved to {output_file}")

if __name__ == "__main__":
    graph = input_graph()
    heuristic = input_heuristics()
    output_file = input("Enter the output file name (e.g., output.txt): ")
    
    save_to_file(graph, heuristic, output_file)
