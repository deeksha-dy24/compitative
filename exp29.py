import heapq

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, c, t = map(int, input().split())
    graph[u].append((v, c, t))

src, dest, maxTime = map(int, input().split())

# dist[node][time] = min cost (optimized using dict)
visited = {}

pq = [(0, 0, src)]  # (cost, time, node)

while pq:
    cost, time, node = heapq.heappop(pq)

    # ✅ If destination reached
    if node == dest:
        print(cost)
        break

    # ✅ Skip worse states
    if (node in visited and visited[node] <= time):
        continue

    visited[node] = time

    for nei, c, t in graph[node]:
        newTime = time + t
        newCost = cost + c

        if newTime <= maxTime:
            heapq.heappush(pq, (newCost, newTime, nei))

else:
    print(-1)