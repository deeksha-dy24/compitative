parent = []
rank = []

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Path compression
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    
    if rootX != rootY:
        # Union by rank
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Input
n, m = map(int, input().split())

parent = list(range(n + 1))
rank = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

# Count components
components = len(set(find(i) for i in range(1, n + 1)))

print(components - 1)