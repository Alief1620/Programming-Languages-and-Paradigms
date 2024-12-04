from collections import deque


def bfsTask(graph, start, end):
    queue = deque(start)
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end:
            return path, len(path)
        else:
            for adjacent in graph.get(node, []):
                queue.append(list(path) + [adjacent])


graph = {
    '1': ['2', '3', '5'],
    '2': ['1', '4'],
    '3': ['1', '5', '6'],
    '4': ['2', '7'],
    '5': ['1', '3', '7'],
    '6': ['3', '8'],
    '7': ['4', '5', '8'],
    '8': ['6', '7'],
}
print(bfsTask(graph, '1', '4'))
