with open('11/input.txt') as f:
    lines = f.read().splitlines()


def solve_part_1():
    # Parse the graph into an adjacency list
    adj = {}
    for line in lines:
        if not line.strip(): continue
        if ': ' in line:
            src, dsts = line.split(': ')
            adj[src] = dsts.split(' ')
    
    # Memoization dictionary to store the number of paths from each node to 'out'
    # This avoids recomputing paths for nodes that are visited multiple times via different paths
    memo = {}

    def count_paths(node):
        # Base case: If 'out' is reached, one valid path is found
        if node == 'out':
            return 1
        
        # Return cached result (if available)
        if node in memo:
            return memo[node]
        
        total = 0
        # Iterate over all outgoing edges
        if node in adj:
            for neighbor in adj[node]:
                total += count_paths(neighbor)
        
        # Cache and return the result
        memo[node] = total
        return total

    return count_paths('you')


def solve_part_2():
    # Parse the graph into an adjacency list
    adj = {}
    for line in lines:
        if not line.strip(): continue
        if ': ' in line:
            src, dsts = line.split(': ')
            adj[src] = dsts.split(' ')
    
    # Memoization dictionary
    # Key: (node, visited_dac, visited_fft)
    # Value: number of paths to 'out'
    memo = {}

    def count_paths(node, visited_dac, visited_fft):
        # Update state based on current node
        if node == 'dac':
            visited_dac = True
        if node == 'fft':
            visited_fft = True
            
        # Base case: If 'out' is reached, only count if both 'dac' and 'fft' were visited
        if node == 'out':
            return 1 if (visited_dac and visited_fft) else 0
        
        state = (node, visited_dac, visited_fft)
        if state in memo:
            return memo[state]
        
        total = 0
        if node in adj:
            for neighbor in adj[node]:
                total += count_paths(neighbor, visited_dac, visited_fft)
        
        memo[state] = total
        return total
    
    return count_paths('svr', False, False)


if __name__ == '__main__':
    print(f"Part 1: {solve_part_1()}")
    print(f"Part 2: {solve_part_2()}")
