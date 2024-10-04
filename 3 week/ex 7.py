def solve_sys(N, M):
    A=[]
    X=[]
    Y=[]
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(N):
        a=[]
        for q in range(M - 1):
            a.append(A[i][q])
        X.append(a)
    for i in range(N):
        Y.append(A[i][-1])
    ans=np.linalg.solve(X, Y)
    print(ans)

N = int(input())
M = int(input())
solve_sys(N, M)