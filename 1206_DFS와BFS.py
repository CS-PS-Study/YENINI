from collections import deque

# N: 노드 개수, M: 간선 개수, Start: 시작 노드
N, M, Start = map(int, input().split())

# 인접 리스트 생성 (1번부터 N번까지 사용)
A = [[] for _ in range(N + 1)]

# 간선 정보 입력 (양방향 그래프)
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)  # s → e
    A[e].append(s)  # e → s

# 작은 번호부터 방문하기 위해 정렬
for i in range(N + 1):
    A[i].sort()

# DFS 함수 (깊이 우선 탐색)
def DFS(v):
    print(v, end=' ')        # 현재 노드 출력
    visited[v] = True        # 방문 처리
    
    for i in A[v]:           # 연결된 노드 탐색
        if not visited[i]:   # 아직 방문 안 했으면
            DFS(i)           # 재귀 호출

# 방문 배열 초기화
visited = [False] * (N + 1)

# DFS 실행
DFS(Start)

print()  # 줄바꿈

# BFS 함수 (너비 우선 탐색)
def BFS(v):
    queue = deque()
    queue.append(v)          # 시작 노드 삽입
    visited[v] = True        # 방문 처리
    
    while queue:
        now_node = queue.popleft()  # 큐에서 하나 꺼냄
        print(now_node, end=' ')
        
        for i in A[now_node]:       # 연결된 노드 확인
            if not visited[i]:      # 방문 안 했으면
                visited[i] = True   # 방문 처리
                queue.append(i)     # 큐에 삽입

# 방문 배열 다시 초기화
visited = [False] * (N + 1)

# BFS 실행
BFS(Start)