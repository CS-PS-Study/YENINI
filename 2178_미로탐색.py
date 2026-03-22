from collections import deque

# 상하좌우 이동 (오른쪽, 아래, 왼쪽, 위)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# N: 행, M: 열
N, M = map(int, input().split())

# 지도 배열
A = [[0] * M for _ in range(N)]

# 방문 체크 배열
visited = [[False] * M for _ in range(N)]

# 입력 받기 (문자열 → 숫자 리스트)
for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j] = int(numbers[j])

# BFS 함수 (시작 좌표 i, j)
def BFS(i, j):
    queue = deque()
    queue.append((i, j))      # 시작 좌표 넣기
    visited[i][j] = True      # 방문 처리

    while queue:
        now = queue.popleft()  # 현재 위치
        
        for k in range(4):     # 4방향 탐색
            x = now[0] + dx[k]
            y = now[1] + dy[k]

            # 좌표 범위 체크
            if x >= 0 and y >= 0 and x < N and y < M:
                
                # 길이 있고(1), 방문 안 했으면
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    
                    # 거리 업데이트 (이전 칸 + 1)
                    A[x][y] = A[now[0]][now[1]] + 1
                    
                    queue.append((x, y))

# (0, 0)에서 시작
BFS(0, 0)

# 도착지까지 최소 거리 출력
print(A[N - 1][M - 1])