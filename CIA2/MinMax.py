def minimax(depth, nodeIndex, isMaximizingPlayer, values):
    if depth == 3:
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values)
            best = max(best, val)
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values)
            best = min(best, val)
        return best

if __name__ == "__main__":
    n = int(input("Enter the number of values (should be 8 for a complete binary tree of depth 3): "))
    
    if n != 8:
        print("The number of values must be 8.")
    else:
        values = []
        print("Enter the values (space-separated): ")
        values = list(map(int, input().split()))

        if len(values) != n:
            print("You must enter exactly 8 values.")
        else:
            optimalValue = minimax(0, 0, True, values)
            print(f"Optimal value using Minimax: {optimalValue}")
