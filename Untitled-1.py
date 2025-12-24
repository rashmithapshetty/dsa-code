from collections import deque 

def bfs(graph,start,goal):
    visited=set()
    queue=deque([[start]])
    if start == goal:
        return[start]
    while queue:
        path=queue.popleft()
        node=path[-1]
        if node not in visited:
            visited.add(node)
            
            for neighbour in graph[node]:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    return new_path
    return None
#Example graph
graph ={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}  
start = 'A'
goal = 'F'
path = bfs(graph,start,goal)
print(f"Path from {start} to {goal}:{path}")      
