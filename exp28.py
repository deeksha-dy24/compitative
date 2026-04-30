import heapq

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))   # Directed graph

src, dest = map(int, input().split())

dist = {i: float('inf') for i in range(1, n + 1)}
dist[src] = 0

pq = [(0, src)]

while pq:
    d, node = heapq.heappop(pq)

    # ✅ Skip outdated entries
    if d > dist[node]:
        continue

    for nei, w in graph[node]:
        if d + w < dist[nei]:
            dist[nei] = d + w
            heapq.heappush(pq, (dist[nei], nei))

# ✅ Handle unreachable case
if dist[dest] == float('inf'):
    print(-1)
else:
    print(dist[dest])