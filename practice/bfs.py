from collections import defaultdict, deque

def bfs_shortest_path(edges, start):
    graph = defaultdict(list)

    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print(graph)

    # 2. Initialize tracking tools
    queue = deque([(start, 0)])  # Stores tuples of (current_node, distance)
    visited = {start}  # Set for O(1) tracking of visited nodes
    distances = {}
    

    while queue:
        print(queue)
        node, dist = queue.popleft()
        print(node,dist)
        distances[node] = dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                print(f'visited: {visited}')
                queue.append((neighbor, dist + 1))

    return distances



# --- Test Run ---
# Connections: A-B, B-C, A-C, C-D
network = [("A", "B"), ("B", "C"), ("A", "C"), ("C", "D")]
print(f'Return Type {bfs_shortest_path(network, start="A")} ')