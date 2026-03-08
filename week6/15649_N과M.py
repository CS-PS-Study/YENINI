N,M = map(int, inpyt().split)
S = [0]*M
visited = [False]*N

def bcktrack(length):
    if length == M:
        print(' '.join((strx+1)for x in S))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            S[length] = i
            backtrack(length + 1)
            visited[i] = False

backtrack(0)