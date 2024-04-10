from collections import deque

def dfs(V):
    stack = [V]
    visit[V] = True
    while stack:
        V = stack.pop()
        print(V, end = ' ')
        for i in sorted(arr[V], reverse=True):
            if not visit[i]:
                stack.append(i)
                visit[i] = True
                 
                
def bfs(V):
    queue = deque([V])
    visit[V] = True
    while queue:
        V = queue.popleft()
        print(V, end = ' ')
        for i in sorted(arr[V]):            
            if not visit[i]:
                queue.append(i)
                visit[i] = True
                
N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visit = [False] * (N + 1)
                    
dfs(V)
print()
   
visit = [False] * (N + 1)
bfs(V)