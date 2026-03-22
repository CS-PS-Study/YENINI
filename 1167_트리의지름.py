from collections import deque

# 노드 개수
N = int(input())

# 인접 리스트 (각 노드에 연결된 (노드, 거리) 저장)
A = [[] for _ in range(N + 1)]

# 입력 처리
for _ in range(N):
    Data = list(map(int, input().split()))
    
    index = 0
    S = Data[index]   # 시작 노드
    index += 1
    
    while True:
        E = Data[index]  # 연결된 노드
        if E == -1:      # 끝 표시
            break
        
        V = Data[index + 1]  # 거리
        A[S].append((E, V))  # (노드, 거리) 저장
        
        index += 2

# 거리 배열, 방문 배열
distance = [0] * (N + 1)
visited = [False] * (N + 1)

# BFS 함수
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    
    while queue:
        now_node = queue.popleft()
        
        for i in A[now_node]:   # (다음 노드, 거리)
            next_node = i[0]
            weight = i[1]
            
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                
                # 현재까지 거리 + 간선 가중치
                distance[next_node] = distance[now_node] + weight

# 1번 노드에서 BFS
BFS(1)

# 가장 먼 노드 찾기
Max = 1
for i in range(2, N + 1):
    if distance[Max] < distance[i]:
        Max = i

# 다시 초기화
distance = [0] * (N + 1)
visited = [False] * (N + 1)

# 가장 먼 노드에서 다시 BFS
BFS(Max)

# 거리 중 최댓값이 트리의 지름
print(max(distance))