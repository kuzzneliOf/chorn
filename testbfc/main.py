n, s, f = tuple(map(int, input().split()))

graph = Graph()
edges = list(range(1, n + 1))

for i in edges:
    graph.addEdge(i)
angles = []

matrix = []

for i in range(n):
    matrix.append(tuple(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            angles.append(tuple([i+1,j+1]))

# angles = [(1, 2), (2, 1), (3, 1), (1, 3), (4, 2), (2, 4), (5, 1), (1, 5), (3, 4), (4, 3)]
for i in angles:
    graph.addAngle(i[0], i[1])
#
start = s
finish = f
queue = []
visited = []
queue.append([start, []])
results = []
while len(queue) > 0:
    current = queue.pop(0)
    if current[0] == finish:
        results.append(current[1])
    else:
        visited.append(current[0])
        for i in graph.neighbours(current[0]):
            if not i in visited:
                a = current[1].copy()
                a.append(current[0])
                queue.append((i, a))
print(min(list(map(len,results))))


