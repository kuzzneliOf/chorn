from bfs import Graph

graph = Graph()
edges = [1, 2, 3, 4, 5]
for i in edges:
    graph.addEdge(i)
angles = [(1, 2), (2, 1), (3, 1), (1, 3), (4, 2), (2, 4), (5, 1), (1, 5), (3, 4), (4, 3)]
for i in angles:
    graph.addAngle(i[0], i[1])

start = 4
aim = 5
queue = []
visited = []
queue.append([start, []])
results = []
while len(queue) > 0:
    current = queue.pop(0)
    if current[0] == aim:
        current[1].append(aim)
        results.append(current[1])
    else:
        visited.append(current[0])
        for i in graph.neighbours(current[0]):
            if not i in visited:
                a = current[1].copy()
                a.append(current[0])
                queue.append((i, a))
print(results)