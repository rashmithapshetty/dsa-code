graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}

visited = []

def dfs(visited,graph,node):
    visited.append(node)
    print(node, end=" ")
    
    for neighbour in graph[node]:
        if neighbour not in visited:
           dfs(visited,graph,neighbour)
            
dfs(visited,graph,'A')